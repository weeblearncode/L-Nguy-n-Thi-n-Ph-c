import pytest
from library_item import LibraryItem  # Replace 'your_module' with the actual module name

def test_initialization_tom_and_jerry():
    item = LibraryItem(name="Tom and Jerry", director="Fred Quimby", rating=4, play_count=0, url="Tom and Jerry")
    assert item.name == "Tom and Jerry"
    assert item.director == "Fred Quimby"
    assert item.rating == 4
    assert item.play_count == 0
    assert item.url == "Tom and Jerry"

def test_info_method_breakfast_at_tiffanys():
    item = LibraryItem(name="Breakfast at Tiffany's", director="Blake Edwards", rating=5)
    assert item.info() == "Breakfast at Tiffany's - Blake Edwards *****"

def test_stars_method_casablanca():
    item = LibraryItem(name="Casablanca", director="Michael Curtiz", rating=2)
    assert item.stars() == "**"
    item.rating = 0
    assert item.stars() == ""

def test_update_rating_gone_with_the_wind():
    item = LibraryItem(name="Gone with the Wind", director="Victor Fleming", rating=3)
    item.update_rating(5)
    assert item.rating == 5
    item.update_rating('4')
    assert item.rating == 4.0

def test_increment_play_count_the_sound_of_music():
    item = LibraryItem(name="The Sound of Music", director="Robert Wise", play_count=0)
    item.increment_play_count()
    assert item.play_count == 1
    item.increment_play_count()
    assert item.play_count == 2