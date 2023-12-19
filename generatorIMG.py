from datetime import datetime
import urllib.request
import json
import time
import os
import requests
import io
import base64
from PIL import Image


def get_local_ip(ip:str):
  return ip

out_dir = 'images'
os.makedirs(out_dir, exist_ok=True)

def get_prompt(prompt:str, neg_prompt:str):
    return {"prompt": prompt, "neg_prompt": neg_prompt}

def timestamp():
    return datetime.fromtimestamp(time.time()).strftime("%Y%m%d-%H%M%S")

def encode_file_to_base64(path):
    with open(path, 'rb') as file:
        return base64.b64encode(file.read()).decode('utf-8')

def decode_and_save_base64(base64_str, save_path):
    with open(save_path, "wb") as file:
        file.write(base64.b64decode(base64_str))

def model_sd(payload):
    response = requests.post(url=f'{get_local_ip("http://127.0.0.1:7860")}/sdapi/v1/options', json=payload)

def call_api(**payload):
    response = requests.post(url=f'{get_local_ip("http://127.0.0.1:7860")}/sdapi/v1/txt2img', json=payload)
    for index, image in enumerate(response.json()["images"]):
        save_path = os.path.join(out_dir, f'txt2img-{timestamp()}-{index}.png')
        decode_and_save_base64(image, save_path)


prompt = get_prompt("cute cat", "")

if __name__ == "__main__";
  payload = {
      "prompt": prompt["prompt"],  # extra networks also in prompts
      "negative_prompt": prompt["neg_prompt"],
      "seed": 1,
      "steps": 20,
      "width": 576,
      "height": 576,
      "cfg_scale": 7,
      "sampler_name": "DPM++ 2M Karras",
      "n_iter": 1,
      "batch_size": 1,
  }
  
  option_payload = {
    "sd_model_checkpoint": "dreamshaper_8.safetensors [879db523c3]",
  }
  
  model_sd(option_payload)
  call_api(**payload)
  
  init_images = [
    encode_file_to_base64(r"B:\path\to\img_1.png"),
    # encode_file_to_base64(r"B:\path\to\img_2.png"),
    # "https://image.can/also/be/a/http/url.png",
  ]
