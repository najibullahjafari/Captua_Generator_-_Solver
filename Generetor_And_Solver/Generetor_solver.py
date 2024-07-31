# Import libs

from PIL import Image, ImageDraw, ImageFont
import numpy as np
from random import randint, choice, uniform
import string
import time
import os

# Setting for the image
colors = {
    "black": 0x1c1c1c,
    "white": 0xfcfcfc,
}
image_width = 250
image_height = 70
font_size = 50
characters = [5, 5]

# to generete a five char text


def get_text():
    out_string = ""
    for i in range(randint(characters[0], characters[1])):
        out_string += choice(string.ascii_letters + "0123456789")
    return out_string


# Draw pixels


def draw_pixel(draw, x, y, thickness):
    if thickness > 1:
        draw.line([(x, y), (x + thickness * ([1, -1][randint(0, 1)]), y + thickness *
                  ([1, -1][randint(0, 1)]))], fill=colors["black"], width=thickness)
    else:
        draw.line([(x, y), (x, y)], fill=colors["black"])


# Adds noise by drawing random pixels on the image.


def add_noise(draw, amount, thickness):
    for i in range(int(amount)):
        draw_pixel(draw, randint(0, image_width),
                   randint(0, image_height), thickness)


# Add lines:


def add_lines(draw, amount, thickness):
    thickness = 1
    wiggle_room_thickness = 2
    for i in range(int(amount)):
        wiggle_thickness = randint(
            thickness, thickness + wiggle_room_thickness)
        draw.line([(randint(0, image_width), randint(0, image_height)), (randint(
            0, image_width), randint(0, image_height))], fill=colors["black"], width=wiggle_thickness)


# Draw characters:


def draw_characters(draw, image, text):
    # Use default font
    font_size = 30
    wiggle_room_width = 48 - len(text) * 6
    wiggle_room_height = 13
    width_padding = 30
    wiggle_room_font_size = 10
    rotation_degrees = 20
    wiggle_room_rotation_percent = 0.4
    spacing_width = (image_width - width_padding) / len(text)
    next_letter_pos = width_padding / 2

    for character in text:
        wiggle_width = uniform(0, wiggle_room_width)
        wiggle_height = uniform(0, wiggle_room_height)
        wiggle_font_size = uniform(
            font_size - wiggle_room_font_size / 2, font_size + wiggle_room_font_size / 2)
        wiggle_rotation_degrees = rotation_degrees * \
            uniform(-wiggle_room_rotation_percent,
                    wiggle_room_rotation_percent)
        font = ImageFont.load_default()
        character_image = Image.new("RGB", (image_height, image_height), 255)
        draw = ImageDraw.Draw(character_image)
        draw.rectangle([0, 0, image_height, image_height],
                       fill=colors["white"])
        draw.text((wiggle_width, wiggle_height), character,
                  fill=colors["black"], font=font)
        character_image = character_image.rotate(
            wiggle_rotation_degrees, expand=True, fillcolor="white")
        image.paste(character_image, (int(next_letter_pos), 0))
        next_letter_pos += spacing_width
    return True


# Main script
num_samples = input("How many images do you want to generate? ")
text_done = []
start = time.time()
# Ensure the output directory exists
output_dir = "./output/"
os.makedirs(output_dir, exist_ok=True)

for i in range():
    image = Image.new('RGB', (image_width, image_height))
    draw = ImageDraw.Draw(image)
    draw.rectangle([0, 0, image_width, image_height], fill=colors["white"])
    text = get_text()
    if text in text_done:
        print("Skipped")
        continue

    if not draw_characters(draw, image, text):
        continue

    text_done.append(text)

    add_noise(draw, amount=int(image_width * image_height * 0.001), thickness=1)
    add_noise(draw, amount=int(image_width * image_height * 0.001), thickness=2)
    add_noise(draw, amount=int(image_width * image_height * 0.001), thickness=3)
    add_lines(draw, amount=1, thickness=2)
    add_lines(draw, amount=1, thickness=3)

    # Save and display the image
    image_path = os.path.join(output_dir, f"{text}.jpg")
    image.save(image_path)
    display(image)

end = time.time()
print(f"Operation completed. Time taken: {end - start} seconds")
