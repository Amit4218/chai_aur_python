import pymongo
from bson import ObjectId


client = pymongo.MongoClient("mongodb+srv://<name>:<password>@cluster0.itgpz.mongodb.net/", tlsAllowInvalidCertificates=True)

db = client["Youtube_manager"]

video_collection = db["videos"]

# print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']},\n Name: {video['name']}, \nTime: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name":name, "time":time})

def update_video(video_id, name, time):
    video_collection.update_one({'_id': ObjectId(video_id)}, {"$set":{"name":name, "time":time}})

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:
        print("\n Youtube manager app")
        print("1. list all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("Enter 5 to exit !")

        choice = input("Enter a choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video id to delete: ")
            name = input("Enter the video name: ")
            time = input("Enter video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video id to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid input !")
        


if __name__ == "__main__":
    main()