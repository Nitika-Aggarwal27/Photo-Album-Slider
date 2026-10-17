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

image_size = [700,700]
images = []

for path in images_path:
    img = Image.open(path)
    img = img.resize(image_size)
    images.append(img)   #adding each images in the list


# convert PIL images into tkinter compatible images
final_images = []
for img in images:
    photo = ImageTk.PhotoImage(img)
    final_images.append(photo)


# label widget to keep Photo
image_label = tk.Label(root)
image_label.pack(pady=30)


# Slideshow function
def start_slideshow():
    for photo in final_images:
        image_label.config(image = photo)
        image_label.image = photo
        root.update()
        time.sleep(2)


# Button
play_button = tk.Button(
    root,
    text = "Play the Slideshow",
    font = ("Arial", 17),
    command= start_slideshow
)

play_button.pack(pady=40)

root.mainloop()