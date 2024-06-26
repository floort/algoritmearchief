#!/usr/bin/env python

import os
import urllib.request

REPO_PATH = "/home/floort/devel/page_snapshots/"
DELAY = 30*60 # 30 minutes
URL = "https://algoritmes.overheid.nl/api/downloads/NLD?filetype=csv" 
try:
  page_content = urllib.request.urlopen(URL).read()
  with open("Algoritmebeschrijvingen.csv", "w") as f:
      f.write(page_content)
  print("OK")
except:
  print("FAILED")

# Try to commit
os.system("git add .")
os.system("git commit -a -m \"Automatic update\"")
os.system("git push")
