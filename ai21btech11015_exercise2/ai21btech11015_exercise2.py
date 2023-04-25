from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt

# (step:1) loading the image information into a numpy nd-array
img = imread(fname='scenery.png')

# (step:2) Printing the number fo pixels in the given image
print(img.shape)

#(step:3) converting image to individual channel and printing its maximum intensity value and its index)
print('Image   :   Maximum intensity \t   Index')
for i in range(3):
     channel = np.zeros(img.shape,dtype='uint8')
     channel[:,:,i]=img[:,:,i]
     plt.imshow(channel)
     intensity = np.amax(channel)
     indx = np.where(channel == np.amax(channel))
     if i == 0:
          print(f'Red \t: \t {intensity}  \t\t {indx[0][0],indx[1][0]}')
          plt.title('Red channel')
          plt.axis(False)
          plt.savefig('Figs/red.png')
     elif i == 1:
          print(f'Green \t: \t {intensity} \t\t {indx[0][0],indx[1][0]}')
          plt.title('Green channel') 
          plt.axis(False)
          plt.savefig('Figs/green.png')
     else:
          print(f'Blue \t: \t {intensity} \t\t {indx[0][0],indx[1][0]}')
          plt.title('Blue channel')
          plt.axis(False)
          plt.savefig('Figs/blue.png')
     plt.show()

#(step:4)transformations.
def mul_img(orginal,transformed,name):
     fig, ax = plt.subplots(1 , 2)
     ax[0].imshow(orginal,cmap='gray')
     ax[0].set_title("Original")
     ax[1].imshow(transformed, cmap='gray')
     ax[1].set_title(name)
     ax[0].axis(False)
     ax[1].axis(False)
     plt.tight_layout()
     plt.savefig(f'Figs/{name}.png')
     plt.show()

# converting image into grayscale
gray_image = rgb2gray(img)
mul_img(img, gray_image, "Gray image")
print(f'Mean of original image array {img.mean()}')
print(f'Mean of transformed image array {gray_image.mean()}')

# Flipping image horizantally
horizontal_flip = img[:, ::-1]
mul_img(img,horizontal_flip,"Horizantally flipped")

# Flipping image vertically
vertical_flip = img[::-1, :]
mul_img(img, vertical_flip, 'Vertically flipped')