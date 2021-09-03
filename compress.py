from PIL import Image
import PIL
import base64
import json
import cv2
import os
import glob
from matplotlib import pylab
import scipy
def img_compress(path):
    foldername = 'compressed_images'
    save_path = os.path.join(os.path.abspath('static'), foldername)
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    # if os.path.isdir(path) == True:
    #     for r, d, f in os.walk(path):
    #         for file in f:
    #             if ('.jpg' in file) or ('.png' in file):
    #                 exact_path = r + "/" + file
    #                 picture = Image.open(exact_path)
    #                 rgb_im = picture.convert('RGB')
    #                 rgb_im.save(save_path+'/'+file.split('.')[0]+'_compressed'+'.jpg',optimize=True,quality=30)
    #                 print("complete")
    #     return save_path
    # else:
    if ('.jpg' in path) or ('.png' in path):
        org_size=os.path.getsize(path)
        picture = Image.open(path)
        rgb_im = picture.convert('RGB')
        img_name = path.split('\\')[-1]
        #print(img_name)
        fn = save_path + '/' + img_name.split('.')[0] + '.jpg'
        rgb_im.save(fn,optimize=True, quality=60)
        img = cv2.imread(fn)
        string = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode()
        comp_size = os.path.getsize(fn)
        print("Compressed " + str(comp_size/org_size*100)+'% ')
    return string
# ret = img_compress(r'C:\Users\doank\Desktop\compress\static\uploaded_images\cv.png')
# #img_compress(r'C:\Users\doank\Desktop\compress\static\uploaded_images\test.jpg')
# print(ret)