from captcha.image import ImageCaptcha
import random

number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alphabet_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                              't', 'u', 'v', 'w', 'x', 'y', 'z']

def create_random_captcha_text(captcha_string_size=6):
    captcha_string_list = []
    base_char = alphabet_lowercase + number_list

    for i in range(captcha_string_size):
        char = random.choice(base_char)
        captcha_string_list.append(char)

    captcha_string = ''

    for item in captcha_string_list:
        captcha_string += str(item)

    return captcha_string

def create_random_digital_text(captcha_string_size=6):
    captcha_string_list = []

    for i in range(captcha_string_size):
        char = random.choice(number_list)
        captcha_string_list.append(char)

    captcha_string = ''

    for item in captcha_string_list:
        captcha_string += str(item)

    return captcha_string

def create_image_captcha(captcha_text):
    image_captcha = ImageCaptcha()
    image_file = "./captcha_" + captcha_text + ".png"
    image_captcha.write(captcha_text, image_file)

def create():
    captcha_text = create_random_captcha_text()
    create_image_captcha(captcha_text)

    return captcha_text

create()