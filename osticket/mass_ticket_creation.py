#!/usr/bin/python

import requests
import json
import base64

headers = {'X-API-Key': '60E19651398CC9593A2D42DCED9C3881'}

message = """
<h2>Entry UI Service</h2>
<p>Create the Hello World framework for the Entry UI Service.  The goal is to build something and take it the entire way through the continuous integration/deployment process of Development &rarr; QA &rarr; Production.</p>
<ol>
<li>Clone the code repository </li>
<li>Install your framework or create your initial files (i.e. myapp.py, db.json, etc.)</li>
<li>Commit your code to the git repository (git commit -a)</li>
<li>Push your changes to the git server (git pull &amp;&amp; git push)</li>
<li>Setup the Jenkins Project (http://jenkins.pyatt.lan:8000/)</li>
<li>Get Jenkins to run a successful build (doesn't have to have any build steps yet)</li>
</ol>
<i>Note: Jenkins is a Java application running on a raspberry pi. It will run slow until it can cache it'
s resources.  If you are having trouble getting it to load the page come back to this step in 20 minutes or so.</i>
<h3>Git Repository</h3>
<p>&nbsp;&nbsp;&nbsp; # git clone git://git.pyatt.lan/entry_ui_service</p>
<h3>Unit Tests</h3>
<p>This doesn't apply for this ticket.</p>
<h3>Document the following in this ticket:</h3>
<ul>
  <li><b>Technology Choice</b>: Python or NodeJS or .Net Core</li>
  <li><b>Command to run</b>: The command Infrastructure will run in production to make the system work (i.e. `python entryui.py`)</li>
  <li><b>Communication</b>: The people in the slack channel that are responsible for this service.</li>
</ul>
"""

ticket = {}
ticket['email'] = 'hackmt@mailinator.com'
ticket['name'] = 'HackMT Project'
ticket['subject'] = 'User UI Service -- Profile Page'
ticket['phone'] = '555-555-5555'
ticket['message'] = 'data:text/html;charset=utf-8,' + message
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
