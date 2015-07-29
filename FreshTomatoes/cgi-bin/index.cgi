#!/usr/bin/env python
import cgi
import os
import cgitb
cgitb.enable()

#Get form POST data for adding new movies
form = cgi.FieldStorage()

title = form.getvalue('title', 'empty')
description = form.getvalue('description', 'empty')
rating = form.getvalue('rating', 'empty')
producer = form.getvalue('producer', 'empty')
trailer = form.getvalue('trailer', 'empty')
poster = form.getvalue('poster', 'empty')

#Escape user input to prevent script injection
title = cgi.escape(title)
description = cgi.escape(description)
rating = cgi.escape(rating)
producer = cgi.escape(producer)
trailer = cgi.escape(trailer)
poster = cgi.escape(poster)

#Append data to file for storage
with open ('movies.txt','a') as out:
    out.write(title+';')
    out.write(description+';')
    out.write(rating+';')
    out.write(producer+';')
    out.write(poster+';')
    out.write(trailer+'\n')

#Process input for rendering
os.system("./entertainment_center.py")

#Redirect back to main page
URL = 'http://localhost:8000/fresh_tomatoes.html'

print('Content-Type: text/html')
print('Location: %s' % URL)
print('')
print('<html>')
print('  <head>')
print('    <meta http-equiv="refresh" content="0;url=%s" />' % URL)
print('    <title>You are being redirected</title>')
print('  </head>') 
print('  <body>')
print('    Redirecting... <a href="%s">Click here if you are not redirected</a>' % URL)
print('  </body>')
print('</html>')
   
