# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 17:53:15 2023

@author: Vasiliy Stepanov
"""
import os
import json
import torch
from diffusers import StableDiffusionPipeline
import gradio as gr

device = 'cuda' if torch.cuda.is_available() else 'cpu'
if device=='cpu':
    print('GPU not found, using CPU!')

try:
    f = open('config.json', 'r')
    config = json.load(f)
except FileNotFoundError:
    print('File not found')


def get_checkpoints_list(path):
    flist = os.listdir(path)
    extentions = ['.safetensors', '.ckpt']
    checkpoints = [file for file in flist if os.path.splitext(file)[1] in extentions]
    if len(checkpoints) == 0:
        raise FileNotFoundError()
        print('Put Stable Diffusion cpkt or safetensors checkpoints to folder!')
    return checkpoints


class CheckPoint():
    def __init__(self, config):
        self.path = config['checkpoints_folder']
        self.checkpoints = get_checkpoints_list(self.path)
        self.load_checkpoint(self.checkpoints[0])
        self.max_width = config['max_width']
        self.max_height = config['max_height']
        self.min_width = config['min_width']
        self.min_height = config['min_height']

    def load_checkpoint(self, filename):
        try:
            self.pipe = StableDiffusionPipeline.from_single_file(self.path+'/'+filename,
                                                                 #torch_dtype=torch.float16,
                                                                 use_safetensors=True)
            self.pipe = self.pipe.to(device)
            print(f'Checkpoint {self.path + filename} loaded!')
        except Warning:
            print('Checkpoint corrupted!')

        return filename

    def generate_image(self, positive_prompt, negative_prompt, width,
                       height, g_scale, manual_seed, steps):
        generator = torch.Generator(device=device)
        seed = generator.seed() if manual_seed == -1 else manual_seed
        generator = generator.manual_seed(seed)

        image = self.pipe(prompt=positive_prompt, negative_prompt=negative_prompt,
                          generator=generator,
                          num_inference_steps=steps,
                          height=(height//8)*8, width=(width//8)*8,
                          g_scale=g_scale).images[0]
        return image


chk = CheckPoint(config)
simple_sd = gr.Blocks(title='Simple Stable Diffusion UI')

with simple_sd:
    with gr.Row():
        with gr.Column():
            models = gr.Dropdown(choices=chk.checkpoints, value=chk.checkpoints[0],
                                 label='Checkpoint', interactive=True)
            positive_prompt = gr.Textbox(label='Prompt', autofocus=True, lines=2)
            negative_prompt = gr.Textbox(label='Negative prompt', lines=2)
            width = gr.Slider(label='Width', value=512, minimum=64, maximum=2048, step=8)
            height = gr.Slider(label='Height', value=512, minimum=64, maximum=2048, step=8)
            with gr.Accordion(label='Advanced settings', open=False):
                with gr.Row():
                    with gr.Column():
                        g_scale = gr.Slider(label='Guidance scale', value=7.5,
                                            minimum=1, maximum=20)
                        steps = gr.Slider(label='Sampling steps', value=40,
                                          minimum=1, maximum=100, step=1)
                    with gr.Column():
                        seed = gr.Number(label='Seed', value=-1, precision=0, interactive=True,
                                         minimum=-1)
                        reset_seed = gr.Button(value='Reset seed')
            button = gr.Button('Generate')

        with gr.Column():
            out = gr.Image()

    button.click(chk.generate_image, inputs=[positive_prompt,
                                             negative_prompt,
                                             width, height, g_scale, seed, steps],
                 outputs=out, queue=True)

    reset_seed.click(lambda x: -1, inputs=seed, outputs=seed, show_progress=False)

    models.input(chk.load_checkpoint, inputs=[models], outputs=[models],
                 show_progress='full', queue=True)


if __name__ == '__main__':
    simple_sd.queue(max_size=1)
    simple_sd.launch(server_name = '0.0.0.0')
