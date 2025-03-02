import sqlite3

connection = sqlite3.connect("Youtube_manager.db")

cursor = connection.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS videos (
               id integer primary key,
               name text not null,
               time text not null)""")

def list_videos():
    cursor.execute("SELECT * FROM videos")

    for row in cursor.fetchall():
            print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time)  VALUES (?, ?)",(name, time))
    connection.commit()

def update_video(name, time, video_id):
    cursor.execute("UPDATE videos SET name = ? , time = ? WHERE id = ?", (name, time, video_id))
    connection.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    connection.commit()

def main():
    while True:
        print("\n Youtube manager sqlite3")
        print("1. List all favorite video")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video id to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(name, time, video_id)
        elif choice == '4':
            video_id = input("Enter video id to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice !")

    connection.close()





if __name__ == "__main__":
    main()