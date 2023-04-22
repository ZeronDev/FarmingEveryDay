import datetime
import schedule
import time
import os

counter = 0

def farm():
    date = datetime.datetime.now()

    with open("./README.md", "a") as readme:
        readme.write(f"{date.year}년 {date.month}월 {date.day}일 ({counter}일째)")

    os.system("git add README.md")
    os.system(f"git commit -m \"{date.year}/{date.month}/{date.day}\"")
    os.system(f"git push origin master")
    
    counter += 1

schedule.every().day.at("0:0").do(farm)

while True:
    schedule.run_pending()
    time.sleep(1)


