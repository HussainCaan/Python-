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
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Name: {row[1]}, Time: {row[2]}, URL: {row[3]}")

def add_video(name, time, url):
    cursor.execute("INSERT INTO videos (Name, time, URL) VALUES (?, ?, ?)", (name, time, url))
    conn.commit()
    

def update_video(video_id, time, url):
    cursor.execute("UPDATE videos SET time = ?, URL = ? WHERE id = ?", (time, url, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()


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
            time = input("Enter video time: ")
            url = input("Enter video URL: ")
            update_video(video_id, time, url)
            
        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
    conn.close()

if __name__ == "__main__":
    main()