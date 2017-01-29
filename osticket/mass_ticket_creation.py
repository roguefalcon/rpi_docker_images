#!/usr/bin/python

import requests
import json
import base64

headers = {'X-API-Key': '60E19651398CC9593A2D42DCED9C3881'}

ticket = {}
ticket['email'] = 'hackmt@mailinator.com'
ticket['name'] = 'HackMT Project'
ticket['subject'] = 'User UI Service -- Profile Page'
ticket['phone'] = '555-555-5555'
ticket['message'] = 'data:text/html;charset=utf-8,<h2>User Profile</h2>  <p>Create the user profile page. It uses the User Management API.</p>'
ticket['ip'] = '192.168.2.11'
ticket['topicId'] = '1'
#ticket['key'] = '60E19651398CC9593A2D42DCED9C3881'

# Adding attachments
# base64 encode the file and add it to the array
with open("profile.png", "rb") as image_file:
   encoded_string = base64.b64encode(image_file.read())
ticket['attachments'] = [{'profile.png': "data:image/png;base64," + encoded_string}]

# Send it to the OSTicket API
r = requests.post("http://osticket.pyatt.lan/api/tickets.json", json=ticket, headers=headers)
print "Created ticket:", ticket['subject']
