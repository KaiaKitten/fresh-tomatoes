#!/usr/bin/env python
import webbrowser
import os

#Prosses movies for rendering
os.system("./entertainment_center.py")

#Open browser new tab with main page
webbrowser.open('http://localhost:8000/fresh_tomatoes.html', new=2)
