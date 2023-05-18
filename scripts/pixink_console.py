import torch
import os
import shutil
import time
import stat
import gradio as gr
import modules.extras
import modules.ui
from modules.shared import opts, cmd_opts
from modules import shared, scripts
from modules import script_callbacks
from pathlib import Path
from typing import List, Tuple
from urllib.parse import urlparse, unquote_plus

work_dir = os.getcwd()

if '\\' in work_dir:
    model_dir_lora = work_dir + '\\models\\Lora\\'
    model_dir_sd = work_dir + '\\models\\Stable-diffusion\\'
else:
    model_dir = work_dir + '/models/Lora'
    model_dir_sd = work_dir + '/models/Stable-diffusion'

def get_file_name_to_download(url):
    parsed_url = urlparse(url)
    return unquote_plus(os.path.basename(parsed_url.scheme + '://' + parsed_url.netloc + parsed_url.path))

def make_download_path(dir, name):
    if '\\' in work_dir:
        return dir + '\\' + name
    else:
        return dir + '/' + name

html = '''
<button style="border-radius: var(--button-large-radius);padding: var(--button-large-padding);font-weight: var(--button-large-text-weight);font-size: var(--button-large-text-size); border: var(--button-border-width) solid var(--button-secondary-border-color);background: var(--button-secondary-background-fill);color: var(--button-secondary-text-color);\" onclick=\"back();\">上一页</button>
<button style="margin-left: 4px;border-radius: var(--button-large-radius);padding: var(--button-large-padding);font-weight: var(--button-large-text-weight);font-size: var(--button-large-text-size); border: var(--button-border-width) solid var(--button-secondary-border-color);background: var(--button-secondary-background-fill);color: var(--button-secondary-text-color);\" onclick=\"forward();\">下一页</button>
<textarea disabled data-testid="textbox" id="url-box" class="scroll-hide" placeholder="https://pix.ink/artwork/" rows="1" style="display:none;margin-left: 4px;overflow-y: scroll; height: 42px;width: 45vw !important;outline: none!important;box-shadow: var(--input-shadow);border: var(--input-border-width) solid var(--input-border-color);border-radius: var(--input-radius);background: var(--input-background-fill);padding: var(--input-padding);color: var(--body-text-color);font-weight: var(--input-text-weight);font-size: var(--input-text-size);line-height: var(--line-sm);"></textarea>
<button style="margin-left: 4px;border-radius: var(--button-large-radius);padding: var(--button-large-padding);font-weight: var(--button-large-text-weight);font-size: var(--button-large-text-size); border: var(--button-border-width) solid var(--button-secondary-border-color);background: var(--button-secondary-background-fill);color: var(--button-secondary-text-color);\" onclick=\"share();\">分享</button>
'''

iframe = '''
<iframe id="pixink-iframe" src="https://pix.ink/model?navbar=hidden" style="width: 95vw; height: 70vh;"></iframe>
'''

def download_lora(url):
    torch.hub.download_url_to_file(url, make_download_path(model_dir_lora, get_file_name_to_download(url)), hash_prefix=None, progress=True)
    return "done"

def download_sd(url):
    torch.hub.download_url_to_file(url, make_download_path(model_dir_sd, get_file_name_to_download(url)), hash_prefix=None, progress=True)
    return "done"

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as PixInk_Blocks:
        with gr.Tabs(elem_id="pix_tabs") as tabs:
            with gr.Tab("模型工坊", elem_id="pix_model"):
                gr.HTML(html)
            with gr.Tab("词条分享", elem_id="pix_prompt"):
                gr.HTML(html)
            with gr.Tab("绘图排行", elem_id="pix_artwork"):
                gr.HTML(html)
            with gr.Tab("技术驿站", elem_id="pix_tech"):
                gr.HTML(html)
            with gr.Tab("杂谈农场", elem_id="pix_water"):
                gr.HTML(html)
            with gr.Tab("Civitai", elem_id="civitai"):
                gr.HTML('')
        with gr.Blocks(analytics_enabled=False):
            gr.HTML(iframe)
            with gr.Row(elem_id="download_predict"):
                gr.Interface(fn=download_lora, inputs="text", outputs="text")
                gr.Interface(fn=download_sd, inputs="text", outputs="text")
    return [(PixInk_Blocks, "Pix Ink Console", "Pix Ink Console")]


script_callbacks.on_ui_tabs(on_ui_tabs)