import csv
import os
import random
from library_item import LibraryItem  # Ensure this matches your actual import path

# Define the path to the CSV file
VIDEO_FILE_PATH = 'C:\\Users\\Admin\\Downloads\\oop-main\\VideoPlayer COMP1752\\video_list.csv'

# Initialize the video library dictionary
video_lib = {}

def videoinfo():
    """Load video information from CSV into video_lib dictionary."""
    if not os.path.exists(VIDEO_FILE_PATH):
        print("CSV file not found.")
        return
    
    with open(VIDEO_FILE_PATH, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Skip header row

        for details in csv_reader:
            if len(details) < 5:
                print(f"Skipping incomplete row: {details}")
                continue

            video_id, name, director, rating, play_count, url = details
            try:
                video_lib[video_id] = LibraryItem(
                    name=name,
                    director=director,
                    rating=float(rating),
                    play_count=int(play_count),
                    url=url
                )
            except ValueError as e:
                print(f"Error converting data: {e}. Row: {details}")

def get_name(video_id):
    """Get the name of the video by its ID."""
    item = video_lib.get(video_id)
    return item.name if item else None

def get_url(video_id):
    """Get the URL of the video by its ID."""
    item = video_lib.get(video_id)
    return item.url if item else None

def get_director(video_id):
    """Get the director of the video by its ID."""
    item = video_lib.get(video_id)
    return item.director if item else None

def get_rating(video_id):
    """Get the rating of the video by its ID."""
    item = video_lib.get(video_id)
    return item.rating if item else None

def get_play_count(video_id):
    """Get the play count of the video by its ID."""
    item = video_lib.get(video_id)
    return item.play_count if item else None

def list_all():
    """List all videos in the library."""
    return "\n".join(f"{key}: {val.name}" for key, val in video_lib.items())

def add_video(video_id, name, director, rating, play_count=0):
    """Add a new video to the library."""
    if video_id not in video_lib:
        video_lib[video_id] = LibraryItem(name, director, rating, play_count)
        return True
    return False

def increment_play_count(video_id):
    """Increment the play count of a video."""
    if video_id in video_lib:
        video_lib[video_id].increment_play_count()

def update_rating(video_id, new_rating):
    """Update the rating of a video."""
    if video_id in video_lib:
        video_lib[video_id].update_rating(new_rating)
        return True
    return False

def get_random_video_id():
    """Get a random video ID from the library."""
    if not video_lib:
        return None
    return random.choice(list(video_lib.keys()))

# Initialize video library
videoinfo()
class LibraryItem:
    def __init__(self, name, director, rating, play_count, url=None):
        self.name = name
        self.director = director
        self.rating = float(rating)  # Ensure rating is a float
        self.play_count = int(play_count)  # Ensure play count is an int
        self.url = url

