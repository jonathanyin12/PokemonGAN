import imageio


filenames = []
for i in range(228):
    if i % 5 == 0:
        filenames.append('Generated Images/epoch{}.png'.format(i))

images = []
for filename in filenames:
    images.append(imageio.imread(filename))

times = []

for epoch in range(45):
    times.append(0.5)


imageio.mimsave('training_progress1.gif', images, duration=times)
