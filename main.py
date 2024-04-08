import fitz
import os
import cv2


file_path = 'pathologyOfTheKidney.pdf'
images_path = 'images/'
pdf_file = fitz.open(file_path)
page_nums = len(pdf_file)

for i in range(page_nums):
    for item in pdf_file.get_page_images(i):
        pix = fitz.Pixmap(pdf_file, item[0])  # pixmap from the image xref
        pix0 = fitz.Pixmap(fitz.csRGB, pix)  # force into RGB
        pix0.save("img%i.png" % item[0])

