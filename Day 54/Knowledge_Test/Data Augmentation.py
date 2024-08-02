import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

img = load_img('00832_00.jpg')  # Change to your image path
x = img_to_array(img)  # Convert image to numpy array
x = np.expand_dims(x, axis=0)  # Add one more dimension


datagen = ImageDataGenerator(
    rotation_range=40,   # Rotate the image by up to 40 degrees
    width_shift_range=0.2,  # Shift the image width-wise by up to 20%
    height_shift_range=0.2, # Shift the image height-wise by up to 20%
    shear_range=0.2,     # Shear transformation
    zoom_range=0.2,      # Zoom into the image by up to 20%
    horizontal_flip=True,  # Flip the image horizontally
    fill_mode='nearest'  # Fill in missing pixels with the nearest filled value
)


# Generate augmented images
i = 0
for batch in datagen.flow(x, batch_size=1):
    plt.figure(i)
    imgplot = plt.imshow(array_to_img(batch[0]))
    i += 1
    if i % 4 == 0:  # Display 4 images
        break

plt.show()