import tkinter as tk
from ttkbootstrap import ttk  # Import ttk from ttkbootstrap
import video_library as lib

def set_text(text_area, content):  # Function to set text in the text area
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", content)

class UpdateVideo:
    def __init__(self, window):
        window.geometry("1800x900")
        window.title("Update Video")
        
        # Define buttons
        listall_button = ttk.Button(
            window, text="List All Videos", 
            bootstyle="primary", command=self.listall
        )
        listall_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.check_video = ttk.Button(
            window, text="Check Video", 
            bootstyle="primary", command=self.displayinfo
        )
        self.check_video.grid(row=0, column=3, padx=10, pady=10)
        
        self.save = ttk.Button(
            window, text="Save", 
            bootstyle="primary", command=self.NewRating
        )
        self.save.grid(row=0, column=6, padx=10, pady=10)

        #===========================Text Areas===========================#
        self.video_box = tk.Text(window, width=50, height=15)
        self.video_box.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        
        self.Videoinfo_box = tk.Text(window, width=50, height=15, wrap="none")
        self.Videoinfo_box.grid(row=1, column=3, columnspan=3, sticky="W", padx=10, pady=10)
        
        #======================Info Labels======================#
        self.Video_ID = ttk.Label(window, font=("Arial", 15), text="Enter Video ID")
        self.Video_ID.grid(row=0, column=1, padx=10, pady=10)
        
        self.label = ttk.Label(window, font=("Arial", 15), text="Enter New Rating")
        self.label.grid(row=0, column=4, padx=10, pady=10)
        
        self.status = ttk.Label(window, text="", font=("Arial", 15))
        self.status.grid(row=8, column=0, columnspan=4, sticky="W", padx=10, pady=10)
        
        #================User Inputs================#
        self.ID_input = ttk.Entry(window, width=30)
        self.ID_input.grid(row=0, column=2, padx=8, pady=10)
        
        self.rating_input = ttk.Entry(window, width=20)
        self.rating_input.grid(row=0, column=5, padx=8, pady=10)
        
        # Automatically list all videos when the window opens
        self.listall()
    
    #====================Button Functions====================#
    #===================Receive and Display Info===================#
    def DisplayInfo(self, key, name, director=None, rating=None, playcount=None):
        director, playcount, rating = self.GetInfo(key)
        info = f"{name}\n{director}\nRating: {rating}\nPlays: {playcount}"
        set_text(self.Videoinfo_box, info)
    
    def GetInfo(self, key):
        director = lib.get_director(key)
        playcount = lib.get_play_count(key)
        rating = lib.get_rating(key)
        return director, playcount, rating
    
    def GetNameAndKey(self):
        key = self.ID_input.get()
        name = lib.get_name(key)
        return key, name
    
    #===========================Show All Available Videos===========================#
    def listall(self):
        showlist = lib.list_all()
        set_text(self.video_box, showlist)
        self.status.configure(text="Status: Showing All Videos")
    
    #==========================Check Video Info==========================#
    def displayinfo(self):
        key, name = self.GetNameAndKey()
        if name is not None:
            director, playcount, rating = self.GetInfo(key)
            self.DisplayInfo(key, name, director, rating, playcount)
            self.status.configure(text="Status: Checking Video Info")
        else:
            self.status.configure(text="Not a valid ID!")
    
    #=================Get New Rating=================
    def NewRating(self):
        key, name = self.GetNameAndKey()
        rate = self.rating_input.get()
        try:
            rate = float(rate)
            if 0 < rate <= 10:
                lib.update_rating(key, rate)
                new_rating = lib.get_rating(key)
                self.DisplayInfo(key, name, rating=new_rating)
                self.status.configure(text="Status: Saved new rating")
            else:
                self.status.configure(text="Rate can only be from 1 to 10!")
        except ValueError:
            self.status.configure(text="Not a valid number!")
