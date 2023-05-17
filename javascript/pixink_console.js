onUiLoaded(() => {
    let iframeUrl = '';
    const iframe = gradioApp().getElementById('pixink-iframe');
    window.addEventListener('message', (event) => {
        if(event.data.type === 'url') {
            iframeUrl = event.data.data;
            gradioApp().getElementById('url-box').value = iframeUrl;
        }
    });
    window.share = function() {
        if (navigator.share) {
            navigator.share({
              title: '片绘社区',
              text: '快来看看我发现了什么好东西！',
              url: iframeUrl,
            }).then(() => console.log('share done')).catch((error) => alert('分享时发生未知错误！'));
          } else {
            alert('您的浏览器不支持该分享');
        }
    }
    window.home = function() {
        iframe.contentWindow.location.href = 'https://pix.ink';
        gradioApp().getElementById('url-box').value = 'https://pix.ink';
    }
});
