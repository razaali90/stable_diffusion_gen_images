# -*- coding: utf-8 -*-

!pip install accelerate

!pip install diffusers==0.18.2

!pip install invisible-watermark

!pip install transformers

from diffusers import DiffusionPipeline
import torch

pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.to("cuda")

# if using torch < 2.0
# pipe.enable_xformers_memory_efficient_attention()

prompt = "A Car racer driving BMW in snowy track"

images = pipe(prompt=prompt).images[0]

images

prompt = "A girl reading book in the room under a candle light"

images = pipe(prompt=prompt).images[0]

images

