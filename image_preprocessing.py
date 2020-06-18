import os
from PIL import Image
from shutil import copyfile, rmtree

pokemon_dataset_dir = 'raw_dataset'
processing_dataset_dir = 'processing_dataset'
white_background_dir = processing_dataset_dir + '/white_background'
flip_dir = processing_dataset_dir + '/flip'
rotate_dir = processing_dataset_dir + '/rotate'
combined_dir = 'training_dataset'


if not os.path.exists(white_background_dir):
    os.makedirs(white_background_dir)
if not os.path.exists(flip_dir):
    os.makedirs(flip_dir)
if not os.path.exists(rotate_dir):
    os.makedirs(rotate_dir)
if not os.path.exists(combined_dir):
    os.makedirs(combined_dir)


# Converts images from RGBA to RGB
def rgba2rgb(image):
    convert_image = image.convert('RGBA') # Convert to RGBA to make sure it's a supported alpha channel
    new_img = Image.new("RGB", convert_image.size, (255, 255, 255))
    new_img.paste(convert_image, mask=convert_image.split()[3]) # 3 is the alpha channel
    return new_img


# Flips the images
def flip_image(image):
    new_img = image.transpose(Image.FLIP_LEFT_RIGHT)
    return new_img


# Rotates the images
def rotate_image(image, degree):
    new_img = image.convert('RGBA') # convert to RGBA to get transparent background
    new_img = new_img.rotate(degree)
    background = Image.new("RGB", new_img.size, (255, 255, 255))
    background.paste(new_img, mask=new_img.split()[3]) # 3 is the alpha channel
    return background


# Creates RGB images
for each in os.listdir(pokemon_dataset_dir):
    img = Image.open(pokemon_dataset_dir + '/' + each, 'r')
    img.load()
    rgb_img = rgba2rgb(img)
    rgb_img.save(white_background_dir + '/' + each[:-3] + 'jpg', 'JPEG', quality=100)

# Creates flipped RGB images
for each in os.listdir(white_background_dir):
    img = Image.open(white_background_dir + '/' + each, 'r')
    img.load()
    flip_img = flip_image(img)
    flip_img.save(flip_dir + '/' + each[:-4] + '-f.jpg', 'JPEG', quality=100)

# Creates rotated images
for each in os.listdir(white_background_dir):
    img = Image.open(white_background_dir + '/' + each, 'r')
    img.load()
    for deg in range(5, 20, 5):
        rotated_ccwr = rotate_image(img, deg)
        rotated_ccwr.save(rotate_dir + '/' + each[:-4] + '_ccwr{}.jpg'.format(deg), 'JPEG', quality=100)

        rotated_cwr = rotate_image(img, -deg)
        rotated_cwr.save(rotate_dir + '/' + each[:-4] + '_cwr{}.jpg'.format(deg), 'JPEG', quality=100)

# Creates rotated + flipped images
for each in os.listdir(flip_dir):
    img = Image.open(flip_dir + '/' + each, 'r')
    img.load()
    for deg in range(5, 20, 5):
        rotated_ccwr = rotate_image(img, deg)
        rotated_ccwr.save(rotate_dir + '/' + each[:-4] + '_ccwr{}.jpg'.format(deg), 'JPEG', quality=100)

        rotated_cwr = rotate_image(img, -deg)
        rotated_cwr.save(rotate_dir + '/' + each[:-4] + '_cwr{}.jpg'.format(deg), 'JPEG', quality=100)

for subdir, dirs, files in os.walk(processing_dataset_dir):
    for file in files:
        copyfile(os.path.join(subdir, file), os.path.join(combined_dir, file))

rmtree(processing_dataset_dir)
