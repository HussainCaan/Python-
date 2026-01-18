# Generate a youtube manager app  in terminal onl for playlist management, favriorite videos adding and video removing from playlist. All this will happen in a txt file named "youtube_data.txt" 
import json
def video_exits(video_name):
    try:
        with open("youtube_data.txt", 'r') as file:
            for line in file:
                if video_name in line:
                    return False
        return True
    except:
        print("Error while reading file ❌")
        
        
def video_remover(video_name):
    try:
        with open("youtube_data.txt", "r") as file:
            lines = file.readlines()

        updated_lines = [line for line in lines if video_name not in line]

        if len(updated_lines) == len(lines):
            return False 

        with open("youtube_data.txt", "w") as file:
            file.writelines(updated_lines)

        return True

    except Exception as e:
        print("Error while removing video: ❌", e)
        return False
        
def video_updater(old_name, new_name, new_url):
    try:
        checker = video_remover(old_name)
        if checker == False:
            return False
        with open('youtube_data.txt', 'a') as file:
            data = {
                "Video Name": new_name,
                "Video_URL": new_url
            }
            json.dump(data, file, ensure_ascii=False)
            file.write("\n") 
        return True
    except:
        print("Error while reading file ❌")
        return False
    

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
                    name = input("👉 Enter video name: ")
                    video_checker = video_exits(name)
                    if video_checker == False:
                        print("Video is already in the list 🚫")
                        continue
                    Video_Url = input("👉 Enter video URL: ")
                    data = {
                        "Video Name": name,
                        "Video_URL": Video_Url
                    }
                    # Dump the object directly; json.dumps() + json.dump() double-encodes and adds escapes
                    json.dump(data, file, ensure_ascii=False)
                    file.write("\n")  # newline so each entry is on its own line
                print("Video added ✅")
            except:
                print("Error while updating the file 🚫")

        case '2':
            video_name = input("👉 Enter the video name you want to remove: ")
            checker = video_remover(video_name)
            if checker == False:
                print("👉 Video not Found 🚫 ")
                continue
            print("Video removed successfully ✅")
        case '3':
            try:
                with open("youtube_data.txt", 'r') as file:
                    print("Your Playlist:")
                    for line in file:
                        video_data = json.loads(line)
                        print(f" - {video_data['Video Name']}: {video_data['Video_URL']}")
            except:
                print("Error while reading the file 🚫")
        case '4':
            video_name = input("👉 Enter the video name you want to update: ")
            checker = video_exits(video_name)
            if checker ==  False:
                new_name = input("👉 Enter new video name: ")
                new_url = input("👉 Enter new video URL: ")
                video_updater_checker = video_updater(video_name, new_name, new_url)
                if video_updater_checker == True:
                    print("Video updated successfully ✅")
            else:
                print("👉 Video not Found 🚫 ")
                continue 
        case '5':
            print("Exiting Youtube Manager App. Goodbye!")
            break
        case _:
            print("❌ Invalid input! Please enter a choice between 1-5")
