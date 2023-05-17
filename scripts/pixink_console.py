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

html = '''
<div style="display: flex; align-items: center;">
<button style="border-radius: var(--button-large-radius);padding: var(--button-large-padding);font-weight: var(--button-large-text-weight);font-size: var(--button-large-text-size); border: var(--button-border-width) solid var(--button-secondary-border-color);background: var(--button-secondary-background-fill);color: var(--button-secondary-text-color);\" onclick=\"window.history.back();\">上一页</button>
<button style="margin-left: 4px;border-radius: var(--button-large-radius);padding: var(--button-large-padding);font-weight: var(--button-large-text-weight);font-size: var(--button-large-text-size); border: var(--button-border-width) solid var(--button-secondary-border-color);background: var(--button-secondary-background-fill);color: var(--button-secondary-text-color);\" onclick=\"window.history.forward();\">下一页</button>
<textarea disabled data-testid="textbox" id="url-box" class="scroll-hide" placeholder="https://pix.ink/artwork/" rows="1" style="margin-left: 4px;overflow-y: scroll; height: 42px;width: 45vw !important;outline: none!important;box-shadow: var(--input-shadow);border: var(--input-border-width) solid var(--input-border-color);border-radius: var(--input-radius);background: var(--input-background-fill);padding: var(--input-padding);color: var(--body-text-color);font-weight: var(--input-text-weight);font-size: var(--input-text-size);line-height: var(--line-sm);"></textarea>
<button style="margin-left: 4px;border-radius: var(--button-large-radius);padding: var(--button-large-padding);font-weight: var(--button-large-text-weight);font-size: var(--button-large-text-size); border: var(--button-border-width) solid var(--button-secondary-border-color);background: var(--button-secondary-background-fill);color: var(--button-secondary-text-color);\" onclick=\"share();\">分享</button>
<button style="margin-left: 4px;border-radius: var(--button-large-radius);padding: var(--button-large-padding);font-weight: var(--button-large-text-weight);font-size: var(--button-large-text-size); border: var(--button-border-width) solid var(--button-secondary-border-color);background: var(--button-secondary-background-fill);color: var(--button-secondary-text-color);\" onclick=\"home();\">回主页</button>
</div>
<iframe id="pixink-iframe" src="https://pix.ink/artwork/" style="width: 95vw; height: 70vh;"></iframe>

'''

def upload_file(files):
    file_paths = [file.name for file in files]
    return file_paths

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as PixInk_Blocks:
            gr.HTML(html)
    return [(PixInk_Blocks, "片绘社区", "片绘社区")]


script_callbacks.on_ui_tabs(on_ui_tabs)