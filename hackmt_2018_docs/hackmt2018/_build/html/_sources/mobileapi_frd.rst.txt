.. highlight:: rst

Mobile API FRD
===============

The Mobile API powers the Mobile app.  The mobile app will also use
several other APIs.

===============
Schema
===============

Please refer to the :ref:`notification-table`, :ref:`session-table`, :ref:`user-table` tables.

===============
User Stories
===============

#. load_sql.py
#. read_sql.py
#. notification_browse
#. notification_read
#. notification_edit
#. notification_add
#. notification_delete
#. session_login
#. session_logout
#. session_check_status
#. user_browse
#. user_read
#. user_edit
#. user_add
#. user_delete

=====================
Special Instructions
=====================

It is probable that you will want to build an API endpoint in the mobile API
that calls another API.  This is very easy using the Python Requests module::

   # ----------------------------------------
   # Put this at the top of your python file
   # ----------------------------------------
   import requests

   # ----------------------------------------------------------------
   # Then put this in your function definition or a helper function
   # ----------------------------------------------------------------
   r = requests.get('https://[URL:PORT]/api/1.0/[ENDPOINT]')


The documentation for this is `available here <http://docs.python-requests.org/en/master/user/quickstart/>`_.
