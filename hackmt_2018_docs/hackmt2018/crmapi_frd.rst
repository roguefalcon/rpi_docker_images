.. highlight:: rst

CRM API FRD
===============

CRM stands for Customer Relationship Management.  Our CRM Portal is designed to help us coordinate customer activity on the website in order to maintain a good relationship.

The CRM API will allow other programs to talk to the CRM Portal.  For example, when a customer fills out the request a quote form on the website, the website will be able to talk to the CRM Portal via the CRM API.  Let’s start with the database schema.

===============
Schema
===============

Please refer to :ref:`todo-table`, :ref:`customer-table`, :ref:`activity-table`, :ref:`status-table`.


===================
User Stories
===================

#. load_sql.py
#. read_sql.py
#. Endpoints

    #. Todo     /api/1.0/todo

        #. Browse
        #. Read
        #. Edit
        #. Add
        #. Delete

    #. Activity   /api/1.0/activity

        #. Browse
        #. Read
        #. Edit
        #. Add
        #. Delete

    #. Status   /api/1.0/status

        #. Browse
        #. Read

    #. Customer  /api/1.0/customer

        #. Browse
        #. Read
        #. Edit
        #. Add
        #. Delete




