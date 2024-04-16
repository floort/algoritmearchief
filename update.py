#!/usr/bin/env python

import os
import urllib2

REPO_PATH = "/home/floort/devel/page_snapshots/"
DELAY = 30*60 # 30 minutes
URL = "https://algoritmes.overheid.nl/api/downloads/NLD?filetype=csv" 
try:
  page_content = urllib2.urlopen(URL).read()
  open("Algoritmebeschrijvingen.csv", "w").write(page_content)
  print("OK")
except:
  print("FAILED")

# Try to commit
os.system("git add .")
os.system("git commit -a -m \"Automatic update\"")
os.system("git push")
