import os
import imageio

directory = 'training_samples'
images = []

for epoch in range(1000):
    if epoch % 5 == 0:
        images.append(imageio.imread(os.path.join(directory, 'Epoch{}.png'.format(epoch))))


gif_name = 'training_progress_1.gif'
imageio.mimsave(gif_name, images, duration=[0.2 for i in images])
