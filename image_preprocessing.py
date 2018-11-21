import os
from PIL import Image

pokemon_dataset_dir = 'raw_dataset'
processed_dataset = 'processed_dataset'
white_background = processed_dataset + '/white_background'
flip = processed_dataset + '/flip'
rotate = processed_dataset + '/rotate'

current_dir = os.getcwd()
pokemon_dir = os.path.join(current_dir, pokemon_dataset_dir)
white_background_dir = os.path.join(current_dir, white_background)
flip_dir = os.path.join(current_dir, flip)
rotate_dir = os.path.join(current_dir, rotate)

if not os.path.exists(white_background_dir):
                os.makedirs(white_background_dir)
if not os.path.exists(flip_dir):
                os.makedirs(flip_dir)
if not os.path.exists(rotate_dir):
                os.makedirs(rotate_dir)


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
for each in os.listdir(pokemon_dir):
    img = Image.open(pokemon_dir + '/' + each, 'r')
    img.load()
    rgb_img = rgba2rgb(img)
    rgb_img.save(white_background + '/' + each[:-3] + 'jpg', 'JPEG', quality=100)

# Creates flipped RGB images
for each in os.listdir(white_background):
    img = Image.open(white_background + '/' + each, 'r')
    img.load()
    flip_img = flip_image(img)
    flip_img.save(flip + '/' + each[:-4] + '-f.jpg', 'JPEG', quality=100)

# Creates rotated images
for each in os.listdir(white_background_dir):
    img = Image.open(white_background_dir + '/' + each, 'r')
    img.load()
    rotate2deg = rotate_image(img, 2)
    rotate2deg.save(rotate + '/' + each[:-4] + '_ccwr2.jpg', 'JPEG', quality=100)
    rotate4deg = rotate_image(img, 4)
    rotate4deg.save(rotate + '/' + each[:-4] + '_ccwr4.jpg', 'JPEG', quality=100)
    rotate6deg = rotate_image(img, 6)
    rotate6deg.save(rotate + '/' + each[:-4] + '_ccwr6.jpg', 'JPEG', quality=100)
    rotate8deg = rotate_image(img, 8)
    rotate8deg.save(rotate + '/' + each[:-4] + '_ccwr8.jpg', 'JPEG', quality=100)
    rotate10deg = rotate_image(img, 10)
    rotate10deg.save(rotate + '/' + each[:-4] + '_ccwr10.jpg', 'JPEG', quality=100)

    rotate2degcw = rotate_image(img, -2)
    rotate2degcw.save(rotate + '/' + each[:-4] + '_cwr2.jpg', 'JPEG', quality=100)
    rotate4degcw = rotate_image(img, -4)
    rotate4degcw.save(rotate + '/' + each[:-4] + '_cwr4.jpg', 'JPEG', quality=100)
    rotate6degcw = rotate_image(img, -6)
    rotate6degcw.save(rotate + '/' + each[:-4] + '_cwr6.jpg', 'JPEG', quality=100)
    rotate8degcw = rotate_image(img, -8)
    rotate8degcw.save(rotate + '/' + each[:-4] + '_cwr8.jpg', 'JPEG', quality=100)
    rotate10degcw = rotate_image(img, -10)
    rotate10degcw.save(rotate + '/' + each[:-4] + '_cwr10.jpg', 'JPEG', quality=100)

# Creates rotated + flipped images
for each in os.listdir(flip_dir):
    img = Image.open(flip + '/' + each, 'r')
    img.load()
    rotate2deg = rotate_image(img, 2)
    rotate2deg.save(rotate + '/' + each[:-4] + '_ccwr2.jpg', 'JPEG', quality=100)
    rotate4deg = rotate_image(img, 4)
    rotate4deg.save(rotate + '/' + each[:-4] + '_ccwr4.jpg', 'JPEG', quality=100)
    rotate6deg = rotate_image(img, 6)
    rotate6deg.save(rotate + '/' + each[:-4] + '_ccwr6.jpg', 'JPEG', quality=100)
    rotate8deg = rotate_image(img, 8)
    rotate8deg.save(rotate + '/' + each[:-4] + '_ccwr8.jpg', 'JPEG', quality=100)
    rotate10deg = rotate_image(img, 10)
    rotate10deg.save(rotate + '/' + each[:-4] + '_ccwr10.jpg', 'JPEG', quality=100)

    rotate2degcw = rotate_image(img, -2)
    rotate2degcw.save(rotate + '/' + each[:-4] + '_cwr2.jpg', 'JPEG', quality=100)
    rotate4degcw = rotate_image(img, -4)
    rotate4degcw.save(rotate + '/' + each[:-4] + '_cwr4.jpg', 'JPEG', quality=100)
    rotate6degcw = rotate_image(img, -6)
    rotate6degcw.save(rotate + '/' + each[:-4] + '_cwr6.jpg', 'JPEG', quality=100)
    rotate8degcw = rotate_image(img, -8)
    rotate8degcw.save(rotate + '/' + each[:-4] + '_cwr8.jpg', 'JPEG', quality=100)
    rotate10degcw = rotate_image(img, -10)
    rotate10degcw.save(rotate + '/' + each[:-4] + '_cwr10.jpg', 'JPEG', quality=100)


