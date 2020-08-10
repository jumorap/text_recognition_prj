import pytesseract
import cv2
from os import remove

# First we install tesseract.exe found in
# "https://tesseract-ocr.github.io/tessdoc/Downloads"
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\juan1\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

# Is selected an image from folder [Images] and this is converted
# between RGB and BGR color spaces (with or without alpha channel),
# and after thanks to pytesseract, we generate all image text
img = cv2.imread('Images/5.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
to_write = pytesseract.image_to_string(img)

print(to_write)

height_img, width_img, _ = img.shape
boxes = pytesseract.image_to_data(img)

# We build a text file called "output.txt" trying of remove an
# existence of this is was build before and writing in a new file
try:
    remove("output.txt")
except:
    print("Building...")

f = open('output.txt', 'a')
f.write(to_write)
f.close()

# Here just use [boxes] to catch the text generated, and after
# be built boxes for word in image using the position number 11
# in [box] generated in loop by [boxes.splitlines()] and using split
#
# After it, just teach the boxes in red color within their interpretation
for x, box in enumerate(boxes.splitlines()):
    if x != 0:
        box = box.split()
        if len(box) == 12:
            x, y, w, h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
            cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
            cv2.putText(img, box[11], (x, y-1), cv2.FONT_ITALIC, 0.8, (50, 50, 255), 1)

cv2.imshow('Result', img)
cv2.waitKey(0)
