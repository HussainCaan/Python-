# Generate a youtube manager app  in terminal onl for playlist management, favriorite videos adding and video removing from playlist. All this will happen in a txt file named "youtube_data.txt" 
import json
while True:
    print("Youtube Manager App")
    print("1. Add Video to Playlist")
    print("2. Remove Video from Playlist")
    print("3. View Playlist")
    print("4. Update details of video in Playlist")
    print("5. Exit")
    choice = input("Enter you choice (1-5): ")
    
    match choice:
        case '1':
            try:
                with open('youtube_data.txt', 'a') as file:
                    name = input("Enter video name: ")
                    Video_Url = input("Enter video URL: ")
                    data = {
                        "Video Name": name,
                        "Video_URL": Video_Url
                    }
                    # Dump the object directly; json.dumps() + json.dump() double-encodes and adds escapes
                    json.dump(data, file, ensure_ascii=False)
                    file.write("\n")  # newline so each entry is on its own line
                print("Video added ✅")
            except:
                print("Error while updating the file")
                