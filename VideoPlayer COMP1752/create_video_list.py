import ttkbootstrap as ttk
import tkinter as tk
import tkinter.scrolledtext as tkst
from ttkbootstrap import style
import video_library as lib
import simple_webbrowser as swb
from PlayPlayList import PlayPlaylist


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", content)

class CreateVideoList:
    #GUI
    def __init__(self, window):
        self.playlist = []
        
        window.geometry("1500x900")
        window.title("Create Video List")

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=10)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        add_video_btn = tk.Button(window, text="Add to Playlist", command=self.add_to_playlist)
        add_video_btn.grid(row=0, column=2, padx=10, pady=10)

        run_playlist_btn = tk.Button(window, text="Play Playlist", command=self.play_playlist)
        run_playlist_btn.grid(row=0, column=3, padx=10, pady=10)

        clear_playlist_btn = tk.Button(window, text="Reset Playlist", command=self.clear_playlist)
        clear_playlist_btn.grid(row=0, column=4, padx=10, pady=10)

        random_video_btn = tk.Button(window, text="Random Video", command=self.add_random_video)
        random_video_btn.grid(row=0, column=5, padx=10, pady=10)
        
        video_open_btn = tk.Button(window, text="Watch on Youtube", command=self.watch_YouTube)
        video_open_btn.grid(row=0, column=6, padx=10, pady=10)
        
        self.playlist_txt = tkst.ScrolledText(window, width=70, height=20, wrap="none")
        self.playlist_txt.grid(row=1, column=0, columnspan=7, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=7, sticky="W", padx=10, pady=10)
        
        self.inputyt_txt = tk.Entry(window, width=10)
        self.inputyt_txt.grid(row=2, column=3, padx=10, pady=10)

        video_search_btn = tk.Button(window, text="Watch on Youtube", command=self.search_YT)
        video_search_btn.grid(row=2, column=6, padx=10, pady=10) 
    #function
    def search_YT(self):
        video_id = self.inputyt_txt.get()
        swb.YouTube(query=video_id)
        
    def watch_YouTube(self):
        video_id = self.input_txt.get()
        url = lib.get_url(video_id)
        swb.YouTube(query=url)
      
    def add_to_playlist(self):
        video_id = self.input_txt.get()
        name = lib.get_name(video_id)
        if name:
            self.playlist.append(name)
            self.update_playlist_display()
            self.status_lbl.configure(text=f"Added video {video_id} to playlist!")
        else:
            try: 
                video_id = int(video_id)
                self.status_lbl.configure(text=f"Video {video_id} not found!")
            except ValueError:
                self.status_lbl.configure(text=f"Please enter a valid ID!")

    def add_random_video(self):
        video_id = lib.get_random_video_id()
        if video_id:
            name = lib.get_name(video_id)
            self.input_txt.delete(0, tk.END)  
            self.input_txt.insert(0, video_id) 
            self.playlist.append(name)
            self.update_playlist_display()
            self.status_lbl.configure(text=f"Added video ID {video_id} to playlist!")
        else:
            self.status_lbl.configure(text="No video found!")

    def update_playlist_display(self):
        set_text(self.playlist_txt, "\n".join(self.playlist))

    def play_playlist(self):
        if self.playlist:
            PlayPlaylist(self.playlist_txt, self.playlist[0])
        else:
            self.status_lbl.configure(text="Playlist is empty. Add videos to the playlist first.")

    def clear_playlist(self):
        self.playlist = []
        set_text(self.playlist_txt, "")
        self.status_lbl.configure(text="Playlist cleared.")