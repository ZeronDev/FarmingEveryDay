import time
import os

counter = 0

def job():
  global counter

  with open("./README.md", "a", encoding="utf-8") as readme:
      readme.write(" ")

  os.system("git add README.md")
  os.system(f"git commit -m \"{counter}\"")
  os.system("git push origin main")
    
  counter += 1

while True:
    job()
    time.sleep(1)
