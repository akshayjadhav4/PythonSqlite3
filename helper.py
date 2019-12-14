import sqlite3 as lite
import  json
# Functions
class DatabaseManage(object):
    def __init__(self):
        global conn
        try:
            conn = lite.connect("youtubevideos.db")
            with conn:
                cur = conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS youtubevideo(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT , description TEXT, tag TEXT)")

        except Exception:
            print("Unable to create a DB")
    
    def insert_data(self,data):
        try:
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO youtubevideo(name,description,tag) VALUES (?,?,?)",data)
            return True
        except  Exception:
            return False

    def fetch_data(self):
        try:
            with conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM youtubevideo ")
                return cur.fetchall()
        except  Exception:
            return False

    def delete_data(self,id):
        try:
            with conn:
                cur = conn.cursor()
                sql = "DELETE FROM youtubevideo WHERE id = ?"
                cur.execute(sql,[id])
            return True
        except  Exception:
            return False


def main():
    print("*"*40)
    print("\n:: YOUTUBE VIDEO IDEAS ::\n")
    print("*"*40)
    print("\n")

    db = DatabaseManage()
    print("::USER MANUAL::\n")
    print("1. Insert new Video Idea ")
    print("2. View all Video Idea ")
    print("3. Delete a Video Idea ( Need video ID) ")
    print("4. Quit ")
    print("*"*40)
    print("\n")

    while True:
        choice = input("\nEnter a choice")
        if choice == '1':
            name = input("\nEnter a Video Title:- ")
            description = input("\nEnter a Video description:- ")
            tag = input("\nEnter a tags related to Video seprated by space:- ")
            tag_list = tag.split()
            tags = json.dumps(tag_list)
            if db.insert_data([name,description,tags]):
                print("Video Idea saved")
            else:
                print("Something went wrong!")

        elif choice =="2":
            print("\n Video Idea List")
            for  index , item in enumerate(db.fetch_data()):
                print("\nSR.NO: " + str(index + 1))
                print("\VideoID: " +str(item[0]))
                print("\Description: " +str(item[1]))
                videoTags = json.loads(item[3])
                str1 = ' '.join(videoTags)
                print("\Tags: " + str(str1))

        elif choice =="3":
            video_id = input('Enter a Video idea ID: ')
            if db.delete_data(video_id):
                print('Video idea deleted successfully.')
            else:
                print("Something went wrong!")
        
        elif choice =="4":
            exit()
        else:
            print("Wrong Choice")


if __name__ == "__main__":
    main()





        




    

