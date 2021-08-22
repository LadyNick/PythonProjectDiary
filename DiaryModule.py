import datetime

def Print_Menu():
    "This prints the Menu"
    print("[N] - New Entry")
    print("[R] - Read Entry")
    print("[V] - View Entry List")
    print("[C] - Special Message")
    print("[Q] - Close Diary\n")
    return

def DiaryReload():
    "This is for loading the entries from the txt file"
    return

class DiaryEntry:
    'This is the class for creating diary entries, but it might be more like an object'
    
    def __init__(self, title):
      current_day_time = datetime.datetime.now()
      self.date = current_day_time.strftime("%m/%d/%Y")
      self.title = title;
      self.time = current_day_time.strftime("%I:%M %p")
      self.text = ""
      
    def SetDiaryText(text):
        self.text = text
    
    
    
    
    