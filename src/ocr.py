from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import matplotlib.pyplot as plt
import os

processor = TrOCRProcessor.from_pretrained('microsoft/trocr-large-handwritten')
model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-large-handwritten')

ext = ('.jpg', '.png', '.jpeg')

#function that gets 'image names' from the './' directory (i.e. the directory this python file is in)
def image_get():
    image_arr = []
    for i in os.listdir():
        if(i.endswith(ext)):
            image_arr.append(i)
    image_arr.sort()
    return image_arr


# function that loads images and converts it to text
def image_load_converter(image_arr):
    # initializing generated_text variable
    generated_text = ""
    for i in image_arr:
        img = Image.open(i)
        img = img.convert('RGB')
        pixel_values = processor(images=img, return_tensors="pt").pixel_values
        generated_ids = model.generate(pixel_values, max_new_tokens=100)
        generated_text_i = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        generated_text = generated_text + " " + generated_text_i
    return generated_text