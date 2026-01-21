import sqlite3

conn = sqlite3.connect('youtube_manager.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    time TEXT NOT NULL,
    URL TEXT NOT NULL
    )               
''')

def view_videos():
    pass

def add_video(name, time, url):
    pass

def update_video(video_id):
    pass
def main():
    while True:
        print("\nYouTube Manager APP with SQLite3")
        print("1. View Videos")
        print("2. Add Video")
        print("3. Update Videos")
        print("4. Delete Video")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            view_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            url = input("Enter video URL: ")
            add_video(name, time, url)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            update_video(video_id)



if __name__ == "__main__":
    main()