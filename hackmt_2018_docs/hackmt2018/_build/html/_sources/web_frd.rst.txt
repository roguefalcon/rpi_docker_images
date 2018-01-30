.. highlight:: rst

Web FRD
===============

The website is designed to be the customer facing portal to the Lawnbots brand.  The wireframes speak for themselves regarding the design elements.  The FRD will describe the function.

==================
Schema
==================

We will use the **user** table and **sessions** table.

See :ref:`user-table` and :ref:`session-table`.

==================
User Stories
==================
#. Create load_sql.py (refer to tutorial: `Hello World - Step 8 <http://dev.kennypyatt.com:3500/hello_world/8>`_)
#. Create read_sql.py
#. Create web.py (refer to tutorial: `Hello World - Step 5 <http://dev.kennypyatt.com:3500/hello_world/5>`_)

    #. Index function
    #. About function
    #. Pricing function
    #. FAQ function
    #. Schedule function
    #. Save RFQ form function

        #. Save to Database
        #. Make API Call to CRM API (see special instructions below).

#. Create index.html
#. Create about.html
#. Create pricing.html
#. Create faq.html
#. Create schedule.html


=====================
Special Instructions
=====================

For the **Save RFQ form function** you are going to need to add an API call to the CRM API::

   # -------------------------------------------------------------------------
   #  Add these lines to the top of your web.py file
   # -------------------------------------------------------------------------

   import requests
   import os

   # -------------------------------------------------------------------------
   #   Add code similar to this in your save function
   # -------------------------------------------------------------------------

   # Set development values
   APP_URL = 'localhost'
   APP_PORT = '5001'

   # Now let's see if production wants override them
   if 'APP_PORT' in os.environ:
       APP_PORT = int(os.environ['APP_PORT'])

   if 'APP_URL' in os.environ and os.environ['APP_DEBUG'] == '0':
       APP_APP = str(os.environ['APP_URL'])

   # A best practice to make sure they aren't already added
   # But we'd need to get the CRM API team to let us search their api
   # r = requests.get('http://' + APP_URL + ':' + APP_PORT + '/api/1.0/customer?name=' + customer_name, data=data)

   # Let's add data to the CRM customer table via the CRM API
   data = {'key': 'value'}
   r = requests.post('http://' + APP_URL + ':' + APP_PORT + '/api/1.0/customer', data=data)

   # Let's make the call to the CRM API and add data to the todo so the CSRs know to do this
   data = {'key': 'value'}
   r = requests.post('http://' + APP_URL + ':' + APP_PORT + '/api/1.0/todo', data=data)

This example code would send the data to the CRM API for a customer and a todo item in two separate API calls.
