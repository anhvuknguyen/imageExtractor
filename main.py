import fitz
import os
import cv2
from PIL import Image
from PIL.Image import Resampling
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

file_path = 'pathologyOfTheKidney.pdf'
images_path = 'images/'
pdf_file = fitz.open(file_path)
page_nums = len(pdf_file)
num = 1
dictionary = {} 

c = canvas.Canvas("PdfWithImages.pdf", pagesize=A4)
width, height = A4

border = 20 # pixels that there is border around each image so it doesn't fill the entire paper
width -= (border * 2)
height -= (border * 2)

for i in range(page_nums):
    for item in pdf_file.get_page_images(i):
        pix = fitz.Pixmap(pdf_file, item[0]) # pixmap from the image xref
        pix0 = fitz.Pixmap(fitz.csRGB, pix)  # force into RGB
        pix0.save("img%i.jpg" % num)
        dictionary["img%i" % num]="img%i.jpg" % num
        


        # put all images in a pdf
        img = Image.open("img%i.jpg" % num)  # open image
        img_width, img_height = img.size  # save image width and size

        # rescale the image so it fits the page even with the borders
        scale_width = width / img_width
        scale_height = width / img_height
        scale_factor = min(scale_width, scale_height)

        # calculate new dimensions
        new_width = img_width * scale_factor
        new_height = img_height * scale_factor

        # resize the image, antialias (resampling.lanczos) to make the picture not blurry/weird
        img = img.resize((int(new_width), int(new_height)), Resampling.LANCZOS)
        img.save("img%i.jpg" % num)

        # calculate image position so its centered w/ borders
        img_x = border + (width - new_width) / 2
        img_y = border + (height - new_height) / 2

        # put image on pdf
        c.drawImage("img%i.jpg" % num,  img_x, img_y)
        c.showPage()

        num+=1


c.save()

print(dictionary['img1'])
im = Image.open(dictionary['img1'],'r')
im.show()



