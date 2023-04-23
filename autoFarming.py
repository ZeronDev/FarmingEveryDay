import datetime
import schedule
import time
import os
# from keep_alive import keep_alive

counter = 0

def job():
  global counter
  date = datetime.datetime.now()

  with open("./README.md", "a") as readme:
      readme.write(f"Commit bot lol {counter}\n\n")

  os.system("git add README.md")
  os.system(f"git commit -m \"{date.year}/{date.month}/{date.day}\"")
  os.system("git push origin main")
    
  counter += 1

schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
