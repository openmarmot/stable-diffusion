# andrew christ
# python 3
# last update - Dec 27 2022
# install
# pip install --upgrade --user torch diffusers transformers scipy accelerate
# ref : https://huggingface.co/CompVis/stable-diffusion-v1-4
# ref : https://github.com/huggingface/diffusers



import torch
import datetime
from diffusers import StableDiffusionPipeline

import sys
import subprocess

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"


pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to(device)

imageViewerFromCommandLine = {'linux':'xdg-open','win32':'explorer','darwin':'open'}[sys.platform]

keep_going=True

while keep_going:
    prompt = input('Enter Prompt ([exit] to exit): ')
    if prompt=='exit':
        keep_going=False
    else:
        b=0
        while b<5:
            b+=1
            print('Generating..')
            image = pipe(prompt).images[0]
            filename = 'images/'+prompt.replace(' ','-')+'-'+str(datetime.datetime.now()).replace(',','-').replace(' ','-').replace(':','-').replace('.','')+'.png'
            print('saving file: '+filename)
            image.save(filename)
            subprocess.Popen([imageViewerFromCommandLine, filename])