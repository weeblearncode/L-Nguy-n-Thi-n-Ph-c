import tkinter as tk
from PIL import Image, ImageTk
import os

class PlayPlaylist:
    #GUI
    def __init__(self, window, video_name):
        self.play_window = tk.Toplevel(window)
        self.play_window.title("Play Video Image")

        self.img_label = tk.Label(self.play_window)
        self.img_label.pack(pady=20)

        # Set the path to the images directory
        self.image_directory = os.path.dirname(__file__)
        self.video_name = video_name
        self.display_image()
#function
    def display_image(self):        
            try:
                img = Image.open(r"C:\Users\Admin\Downloads\oop-main\VideoPlayer COMP1752\playlist.png")
                img = img.resize((300, 300), Image.LANCZOS)  # Resize image
                img = ImageTk.PhotoImage(img)

                self.img_label.configure(image=img)
                self.img_label.image = img  # Keep a reference to avoid garbage collection
            except Exception as e:
                print(f"Error loading image: {e}")
    