from os.path import isfile

import cv2
import sys
import os
import glob
import numpy as np
from PIL import Image

class FaceMirror:
    def __init__(self):
        self.side_choise = sys.argv[1] #face side parameter
        self.image_path = sys.argv[2] #path of the initial image
        self.cascade_path = sys.argv[3] #path of the haarcascade.xml file
        self.scale_factor = float(sys.argv[4]) #image scaling parameter
        self.folder_create('temp/')
        self.folder_create('temp/half/')
        self.folder_create('temp/shronk/')

        self.initial_image = cv2.imread(self.image_path)
        self.faces = self.face_detect(self.image_path,self.cascade_path)
        print("{} faces found".format(len(self.faces)))

        self.face_slice(self.side_choise)
        for image in os.listdir('temp/half/'):
            self.image_flip(image)
        self.image_overlay()

        self.temp_clear('half/')
        self.temp_clear('shronk/')

    def face_detect(self, image_path, cascade_path): #face detection in the given image using haarcascades
        face_cascade = cv2.CascadeClassifier(cascade_path)
        self.initial_image = cv2.imread(image_path)
        image_grayscale = cv2.cvtColor(self.initial_image, cv2.COLOR_BGR2GRAY)
        self.faces = face_cascade.detectMultiScale(
            image_grayscale,
            scaleFactor=self.scale_factor,
            minNeighbors=5,
            minSize=(20, 20)
        )

        print("{} faces found".format(len(self.faces)))
        return self.faces      

    def image_flip(self, image_path): #flipping the image by vertical axis
        try:
            image_obj = Image.open('temp/half/' + image_path)
            flipped_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
            flipped_image.save('temp/half/flip_{}'.format(image_path))

            image1 = Image.open('temp/half/' + image_path)
            image2 = Image.open('temp/half/flip_' + image_path)
            self.image_concat(image1, image2, image_path, self.side_choise)
        except:
            pass

    def image_concat(self, image1, image2, image, side): #concatenating two images of the same height horizontally
        if side == '-l':
            final = Image.new('RGB', (image1.width + image2.width, image1.height))
            final.paste(image1, (0,0))
            final.paste(image2, (image1.width, 0))
        elif side == '-r':
            final = Image.new('RGB', (image1.width + image2.width, image1.height))
            final.paste(image2, (0,0))
            final.paste(image1, (image2.width, 0))
        else:
            pass
        final.save('temp/shronk/{}'.format(image))

    def temp_clear(self, directory): #deleting the files in given directory
        files = glob.glob('temp/' + directory + '*')
        for f in files:
            os.remove(f)

    def folder_create(self, name): #creating a folder with a given name
        if not os.path.exists(name):
            os.makedirs(name)

    def face_slice(self, side): #slicing the left or right side of the image and saving to a new one
        for x,y,w,h in self.faces:
            if side == '-l': 
                roi_color = self.initial_image[y: y + h, x: x + w//2]
            elif side == '-r':
                roi_color = self.initial_image[y: y + h, x + w//2: x + w] 
            else:
                print('Choose the side')
                pass
            cv2.imwrite("temp/half/{}x{}x{}x{}.jpg".format(x,y,w,h), roi_color)

    def image_overlay(self): #placing an overlay image to a certain coordinates on initial image  
        for x,y,w,h in self.faces:
            path = str(x) +'x'+ str(y) +'x'+ str(w) +'x'+ str(h) + '.jpg'
            s_img = cv2.imread('temp/shronk/' + path, -1)
            s_img = cv2.cvtColor(s_img, cv2.COLOR_RGB2RGBA).copy()
            y1, y2 = y, y + s_img.shape[0]
            x1, x2 = x, x + s_img.shape[1]

            alpha_s = s_img[:, :, 3] / 255.0
            alpha_l = 1.0 - alpha_s

            for c in range(0, 3):
                self.initial_image[y1:y2, x1:x2, c] = (alpha_s * s_img[:, :, c] +
                                        alpha_l * self.initial_image[y1:y2, x1:x2, c])
        cv2.imwrite('final/{}x{}.jpg'.format(w,h), self.initial_image)

if __name__ == '__main__':
    face_mirror = FaceMirror()
else:
    pass