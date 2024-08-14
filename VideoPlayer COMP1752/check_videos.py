import tkinter as tk
import tkinter.scrolledtext as tkst


import video_library as lib
import font_manager as fonts

#GUI
def set_text(text_area, content): # Function for inserting content into Text_area
    text_area.delete("1.0", tk.END)# Remove existing content
    text_area.insert(1.0, content)# Input text 


class CheckVideos():# A class for checking video in the program's window, inclues list video clicked
    def __init__(self, window):
        window.geometry("1350x600")# Configure window size 
        window.title("Check Videos")# Customize window title 

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)# create a button for listing all videos, that button retrives the output from the fuction list_video_clicked  
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)# Customize grid appearance 

        enter_lbl = tk.Label(window, text="Enter Video Number")# Create a label to tell the user to enter video number
        enter_lbl.grid(row=0, column=1, padx=10, pady=10,)# Customize grid appearance 

        self.input_txt = tk.Entry(window, width=3)# The input field for user to enter video number
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)# Customize grid appearance 

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)# Create a button for the user to check video, that button retrives information from the function check_video_clicked
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)# Customize grid appearance 

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none") # Create a text area that can be scrolled
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)# Customize grid appearance 

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")# create a window displaying video text
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)# Customize grid appearance 
  
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))# Check video status 
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)# Customize grid appearance 

        self.list_videos_clicked()# Invoke list_videos_clicked method 
#function
    def check_video_clicked(self):# A method to process checking videos
        key = self.input_txt.get()# Get the video number entered from input
        name = lib.get_name(key) # Get the video name from lib
        if name is not None: # If video does exist, collect and display its details
            director = lib.get_director(key)# Display attributes from lib
            rating = lib.get_rating(key)    
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details) # Give information about video details and display it in a window
        else:# If video does not exist, display the error message
            set_text(self.video_txt, f"Video {key} not found")#update the status after button
        self.status_lbl.configure(text="Check Video button was clicked!")# Update the status    

    def list_videos_clicked(self):# A method to process video listing
        video_list = lib.list_all() # Get all video list from lib 
        set_text(self.list_txt, video_list)#print result
        self.status_lbl.configure(text="List Videos button was clicked!")# Update the status after button is clicked

