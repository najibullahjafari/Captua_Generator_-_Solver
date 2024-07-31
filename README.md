Caputa solver using KNN and Open CV
What will do it?
This system will generete caputa images and then will solve and read the genereted images.

Tools and Libraries
PyTorch: An open-source machine learning framework that provides a seamless path from research to production. NumPy: A library for scientific computing in Python, used for numerical operations on arrays and matrices. Torchvision: A PyTorch library for computer vision tasks such as image classification, object detection, and segmentation. Pillow: A library for handling and manipulating images in Python. OpenCV: A library for computer vision tasks, used for image pre-processing in this project. Matplotlib: A data visualization library in Python, used for creating plots and charts.

Introduction
This project aims to explore the use of deep learning techniques, specifically a CNN-BiLSTM model, for solving text-based CAPTCHA tests. The goal is to understand the algorithms that could potentially crack CAPTCHA tests and use this knowledge to enhance CAPTCHA-generating systems and maintain a high level of network security. The CNN-BiLSTM model is chosen for its ability to recognize complicated alphanumeric characters and learn inherent features of text sequences in CAPTCHAs, allowing for accurate predictions on previously unseen CAPTCHAs.

Data Generation
This project uses a custom CAPTCHA generator written in Python to generate data for training and testing a machine learning model. The generator creates images with random alpha-numeric character combinations as labels, and applies random distortions and noise to the images to create a diverse and challenging dataset.

Output:
This script will generate the CAPTCHA images, save them, and display each image directly in your Jupyter notebook. The display(image) function call from IPython.display is used to show the image within the notebook.

1- First step we should install two pyton libiraries like pillow and numpy and neccessery libiraries
`
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from random import randint, choice, uniform
import string
import time
import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from random import randint, choice, uniform
import string
import time
import os`

2- We need to generete the caputa images

a- define the property of image
`colors = {
"black": 0x1c1c1c,
"white": 0xfcfcfc,
}
image_width = 250
image_height = 70
font_size = 50
characters = [5,5]
colors = {
"black": 0x1c1c1c,
"white": 0xfcfcfc,
}
image_width = 250
image_height = 70
font_size = 50
characters = [5,5]`
b- to generete afive char text
`
`
def get_text():
out_string = ""
for i in range(randint(characters[0], characters[1])):
out_string += choice(string.ascii_letters + "0123456789")
return out_string
c- Draw pixels`

`def draw*pixel(draw, x, y, thickness):
if thickness > 1:
draw.line([(x, y), (x + thickness * ([1, -1][randint(0, 1)]), y + thickness \_ ([1, -1][randint(0, 1)]))], fill=colors["black"], width=thickness)
else:
draw.line([(x, y), (x, y)], fill=colors["black"])
d- Adds noise by drawing random pixels on the image.
`
`
def add_noise(draw, amount, thickness):
for i in range(int(amount)):
draw_pixel(draw, randint(0, image_width), randint(0, image_height), thickness)
e- Add lines:`
def add_lines(draw, amount, thickness):
thickness = 1
wiggle_room_thickness = 2
for i in range(int(amount)):
wiggle_thickness = randint(thickness, thickness + wiggle_room_thickness)
draw.line([(randint(0, image_width), randint(0, image_height)), (randint(0, image_width), randint(0, image_height))], fill=colors["black"], width=wiggle_thickness)
f- Draw characters:
`
`
def draw_characters(draw, image, text):

font*size = 30
wiggle_room_width = 48 - len(text) * 6
wiggle*room_height = 13
width_padding = 30
wiggle_room_font_size = 10
rotation_degrees = 20
wiggle_room_rotation_percent = 0.4
spacing_width = (image_width - width_padding) / len(text)
next_letter_pos = width_padding / 2
​
for character in text:
wiggle_width = uniform(0, wiggle_room_width)
wiggle_height = uniform(0, wiggle_room_height)
wiggle_font_size = uniform(font_size - wiggle_room_font_size / 2, font_size + wiggle_room_font_size / 2)
wiggle_rotation_degrees = rotation_degrees * uniform(-wiggle_room_rotation_percent, wiggle_room_rotation_percent)
​
font = ImageFont.load_default()
​
character_image = Image.new("RGB", (image_height, image_height), 255)
draw = ImageDraw.Draw(character_image)
draw.rectangle([0, 0, image_height, image_height], fill=colors["white"])
draw.text((wiggle_width, wiggle_height), character, fill=colors["black"], font=font)
character_image = character_image.rotate(wiggle_rotation_degrees, expand=True, fillcolor="white")
image.paste(character_image, (int(next_letter_pos), 0))
next_letter_pos += spacing_width
return True
h- generete the image
`

# Main script

`
num_samples = input("How many images do you want to generate? ")
text_done = []
start = time.time()
​`

# Ensure the output directory exists

`
output*dir = "./output/"
os.makedirs(output_dir, exist_ok=True)
​
for i in range(int(num_samples)):
image = Image.new('RGB', (image_width, image_height))
draw = ImageDraw.Draw(image)
draw.rectangle([0, 0, image_width, image_height], fill=colors["white"])
​
text = get_text()
if text in text_done:
print("Skipped")
continue
​
if not draw_characters(draw, image, text):
continue
​
text_done.append(text)
​
add_noise(draw, amount=int(image_width * image*height * 0.001), thickness=1)
add*noise(draw, amount=int(image_width * image*height * 0.001), thickness=2)
add*noise(draw, amount=int(image_width * image*height * 0.001), thickness=3)
add_lines(draw, amount=1, thickness=2)
add_lines(draw, amount=1, thickness=3)
​`

# Save and display the image

`
image_path = os.path.join(output_dir, f"{text}.jpg")
image.save(image_path)
display(image)
​
end = time.time()
print(f"Operation completed. Time taken: {end - start} seconds")
How many images do you want to generate? 12

Operation completed. Time taken: 0.12555170059204102 seconds
Now to read the images and solve caputas to do this we need Tesseract lib which should be installed locally.

Tesseract
is an open-source Optical Character Recognition (OCR) engine developed by Google. It's highly effective for text extraction from images and PDFs. Here’s a comprehensive overview, including its documentation, installation, and usage: Tesseract OCR is widely used for various OCR tasks and supports multiple languages. It’s capable of recognizing text in images, converting scanned documents into machine-encoded text, and more.

Key Features
Multi-language Support: Tesseract supports over 100 languages and can recognize text in various scripts. Accuracy: It offers high accuracy for printed text and can be trained to recognize custom fonts or handwritten text. Versatility: Tesseract works with multiple image formats and can output text in several formats.

import pytesseract
from PIL import Image
import os
from IPython.display import display
​

# Path to the Tesseract executable

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
​

# Directory containing the generated CAPTCHA images

output_dir = "./output/"
​

# Ensure the output directory exists

if not os.path.exists(output_dir):
raise FileNotFoundError(f"The output directory '{output_dir}' does not exist.")
​

# List to store the results

results = []
​

# Read each image in the output directory and decode it using pytesseract

for image_name in os.listdir(output_dir):
if image_name.endswith('.jpg'):
image_path = os.path.join(output_dir, image_name)
image = Image.open(image_path)
decoded_text = pytesseract.image_to_string(image, config='--psm 8') # PSM 8: Treat the image as a single word
results.append((image_name, decoded_text.strip()))
​

# Display the results

for image_name, decoded_text in results:
print(f"Image: {image_name}, Decoded Text: {decoded_text}")
image_path = os.path.join(output_dir, image_name)
image = Image.open(image_path)
display(image)
​
Image: 0B5xX.jpg, Decoded Text: Pe

Image: 5UyhF.jpg, Decoded Text: ue

Image: 5YljE.jpg, Decoded Text: em anne
