from os.path import isfile

import cv2
import sys
import os
import glob
import numpy as np
from PIL import Image

class FaceMirror:
    def __init__(self):
        self.folder_create('./data/images/temp/')
        self.folder_create('./data/images/temp/half/')
        self.folder_create('./data/images/temp/shronk/')
        self.folder_create('./data/images/stock/')
        self.folder_create('./data/images/final/')

    def run(self, image_path, cascade_path, side_choise):
        print("FaceMirror.py running")
        self.image_path = "./data/images/stock/" + image_path
        self.side_choise = side_choise
        self.cascade_path = cascade_path
        self.initial_image = cv2.imread(self.image_path)
        self.faces = self.face_detect(self.image_path)
        print("{} faces found".format(len(self.faces)))

        self.face_slice(self.side_choise)
        for image in os.listdir('./data/images/temp/half/'):
            self.image_flip(image)
        filename = self.image_overlay()
        return filename

    def face_detect(self, image_path): #face detection in the given image using haarcascades
        face_cascade = cv2.CascadeClassifier(self.cascade_path)
        image_grayscale = cv2.cvtColor(self.initial_image, cv2.COLOR_BGR2GRAY)
        self.faces = face_cascade.detectMultiScale(
            image_grayscale,
            scaleFactor=1.05,
            minNeighbors=5,
            minSize=(20, 20)
        )

        print("{} faces found".format(len(self.faces)))
        return self.faces      

    def image_flip(self, image_path): #flipping the image by vertical axis
        try:
            image_obj = Image.open('./data/images/temp/half/' + image_path)
            flipped_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
            flipped_image.save('./data/images/temp/half/flip_{}'.format(image_path))

            image1 = Image.open('./data/images/temp/half/' + image_path)
            image2 = Image.open('./data/images/temp/half/flip_' + image_path)
            self.image_concat(image1, image2, image_path, self.side_choise)
        except:
            pass

    def image_concat(self, image1, image2, image, side): #concatenating two images of the same height horizontally
        if side == 'left':
            final = Image.new('RGB', (image1.width + image2.width, image1.height))
            final.paste(image1, (0,0))
            final.paste(image2, (image1.width, 0))
        elif side == 'right':
            final = Image.new('RGB', (image1.width + image2.width, image1.height))
            final.paste(image2, (0,0))
            final.paste(image1, (image2.width, 0))
        else:
            pass
        final.save('./data/images/temp/shronk/{}'.format(image))

    def folder_create(self, name): #creating a folder with a given name
        if not os.path.exists(name):
            os.makedirs(name)

    def clear(self):
        self.folder_clear('stock/')
        self.folder_clear('temp/half/')
        self.folder_clear('temp/shronk/')
        self.folder_clear('final/')

    def folder_clear(self, directory): #deleting the files in given directory
        files = glob.glob('./data/images/' + directory + '*')
        for f in files:
            os.remove(f)

    def face_slice(self, side): #slicing the left or right side of the image and saving to a new one
        for x,y,w,h in self.faces:
            if side == 'left': 
                roi_color = self.initial_image[y: y + h, x: x + w//2]
            elif side == 'right':
                roi_color = self.initial_image[y: y + h, x + w//2: x + w] 
            else:
                print('Choose the side')
                pass
            cv2.imwrite("./data/images/temp/half/{}x{}x{}x{}.jpg".format(x,y,w,h), roi_color)

    def image_overlay(self): #placing an overlay image to a certain coordinates on initial image  
        for x,y,w,h in self.faces:
            path = str(x) +'x'+ str(y) +'x'+ str(w) +'x'+ str(h) + '.jpg'
            s_img = cv2.imread('./data/images/temp/shronk/' + path, -1)
            s_img = cv2.cvtColor(s_img, cv2.COLOR_RGB2RGBA).copy()
            y1, y2 = y, y + s_img.shape[0]
            x1, x2 = x, x + s_img.shape[1]

            alpha_s = s_img[:, :, 3] / 255.0
            alpha_l = 1.0 - alpha_s

            for c in range(0, 3):
                self.initial_image[y1:y2, x1:x2, c] = (alpha_s * s_img[:, :, c] +
                                        alpha_l * self.initial_image[y1:y2, x1:x2, c])
        cv2.imwrite('./data/images/final/{}x{}.jpg'.format(w,h), self.initial_image)
        return f"{w}x{h}.jpg"


face_mirror = FaceMirror()
