#input file  should *.jpeg
#output is a folder with the original image cut into squares and stored as *.png

import os
import sys
import glob
import cv2 as cv
import matplotlib.pyplot as plt
%matplotlib inline


image_name = glob.glob('*.jpeg')[0]  # find the first jpeg file in the folder


# input :: load image

processed_image = cv.imread(image_name)


# output::
# set the output folder
output_path = sys.path[0] + r'/' + image_name[:-5] + '_parts' + r'/'
# python path shit
output_path = output_path.replace('\\', '/')
# change to windows path shit
output_path = output_path.replace('/', '\\')

# output folder name
output_directory = image_name[:-5] + '_parts'
# create the folder
!mkdir $output_directory
# change to the outputfolder
os.chdir(output_directory)


print(f'The cut parts are stored at location {output_path}')
print(f'Dimensions of the original image : {processed_image.shape}')


bucket = 125 # square images 125 x 125 pixels
columns = int(processed_image.shape[0]/bucket)
rows = int(processed_image.shape[1]/bucket)
print(f'Number of columns: {columns}')
print(f'Number of rows: {rows}')
index = 0
fig = plt.figure(figsize=(16, 16))


# cut the image into squares of 125 x 125 size
for y in range(columns):
    start_y = y*bucket
    end_y = (y+1)*bucket
    for i in range(rows):
        index += 1
        start_x = i*bucket
        end_x = (i+1)*bucket
        fig.add_subplot(rows, columns, index)
        img = processed_image[start_y+1:end_y, start_x+1:end_x]
        plt.imshow(img)
        # name the parts
        partname = str(y) + str(i) + '.png'
        # save the parts
        cv.imwrite(partname, img)
#show all the cut parts
plt.show()