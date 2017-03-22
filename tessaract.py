from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep
from PIL import Image, ImageEnhance, ImageFilter
#from pytesser import *
import pytesseract
import cv2
global ext
'''
while True:
    img = cv2.VideoCapture(0).read()[1]
    sleep(3)
    print(cv2.VideoCapture(0).read()[0])
    cv2.imwrite('test.jpg',img)
    img = Image.open('test.jpg')
    words = pytesseract.image_to_string(image).strip()
    print(words)
    '''

camera = PiCamera()
piRgbaArray = PiRGBArray(camera)
camera.rotation = 180

camera.start_preview(alpha = 200)
sleep(2)
camera.capture('test.jpg')
#image = piRgbaArray.array
#cv2.imwrite('test.jpg',image)
ext = ".jpg"
img = Image.open('test.jpg')
w, h = img.size
img.crop((0, 30, w, h/2)).save('test.jpg')
img = Image.open('test.jpg')
#im = img.filter(ImageFilter.MedianFilter())
#enhancer = ImageEnhance.Contrast(im)
#im = enhancer.enhance(2)
#im = im.convert('1')
#im.save('temp2.jpg')
#img = Image.open('temp2.jpg')
text = pytesseract.image_to_string(img).strip()
camera.stop_preview()
print(text)


