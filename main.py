# Project Photo album or image slider
# fisrt install the pillow library into terminal, cmd-> python -m pip install pillow

import tkinter as tk
import time
from PIL import Image, ImageTk

# main application window
root = tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("900*900")

# List of general path Images (if you want to watch the images just download the images on the same path, then you will see the image slider as well.)
images_path = [
    r"/Users/nitika/Desktop/Album/img0.jpeg",
    r"/Users/nitika/Desktop/Album/img1.jpeg",
    r"/Users/nitika/Desktop/Album/img2.jpeg",
    r"/Users/nitika/Desktop/Album/img3.jpeg",
    r"/Users/nitika/Desktop/Album/img4.jpeg",
    r"/Users/nitika/Desktop/Album/img5.jpeg",
    r"/Users/nitika/Desktop/Album/img6.jpeg"
]

images = []

for path in images_path:
    img = Image.open(path)