.. highlight:: rst

Database Schema
===============

.. _activity-table:

==============
**activity**
==============

This table tracks the activity of todo items and relates back to it (FK).

============== ====================
Column Name    Type
============== ====================
rowid          (provided by SQLite)
todo_id        integer
note           text
status_id      integer
employee_id    integer
active         integer
date_created   text
============== ====================

.. _crew-table:

============
**crew**
============

The crew table tracks the various 'crews' of people and equipment.

============== ====================
Column Name    Type
============== ====================
rowid          (provided by SQLite)
name           text
active         integer
date_created   text
============== ====================

.. _crew-member:

================
**crew_member**
================

This is a join table between the employee table and the crew table.

============== ====================
Column Name    Type
============== ====================
rowid          (provided by SQLite)
crew_id        integer
employee_id    integer
active         integer
date_created   text
============== ====================

.. _customer-table:

===============
**customer**
===============

This holds both prospects and customers

============== ====================
Column Name    Type
============== ====================
rowid          (provided by SQLite)
name           text
email          text
street         text
city           text
state          text
zip            text
phone          text
status_id      integer
active         integer
date_created   text
============== ====================

.. _employee-table:

===============
**employee**
===============

This table holds information about the hero employees of Lawnbots

============== ====================
Column Name    Type
============== ====================
rowid          (provided by SQLite)
name           text
email          text
phone          text
password       text
message        text
status_id      integer
active         integer
date_created   text
============== ====================

.. _equipment-table:

===============
**equipment**
===============

This is a list of equipment and which crew it's assigned to

============== ====================
Column Name    Type
============== ====================
rowid          (provided by SQLite)
name           text
quantity       integer
crew_id        integer
active         integer
============== ====================

.. _notification-table:

=================
**notification**
=================

This table holds notifications for display on the mobile app.

============== ====================
Column Name    Type
============== ====================
rowid          (provided by SQLite)
type           text
note           text
customer_id    integer
employee_id    integer
status_id      integer
active         integer
date_created   text
============== ====================

.. _schedule-table:

===============
**schedule**
===============

This table holds the operations employee schedule.

============== ====================
Column Name    Type
============== ====================
rowid          (provided by SQLite)
type           text
customer_id    integer
employee_id    integer
active         integer
schedule_date  text
date_created   text
============== ====================

.. _session-table:

===============
**session**
===============

This table holds the sessions.  If they have an entry in here and it's less than
1 hour old, then they are logged in.

============== ====================
Column Name    Type
============== ====================
rowid          (provided by SQLite)
user_id        integer
date_created   text
============== ====================

.. _status-table:

===============
**status**
===============

This table holds the statuses for several different applications.

============== ====================
Column Name    Type
============== ====================
rowid          (provided by SQLite)
name           text
description    text
status_group   text
active         integer
date_created   text
============== ====================

There are going to be a bunch of status values here:

* *Activity Statuses*

  * Filled out RFQ - Customer filled out the RFQ
  * Meeting Scheduled - We’ve scheduled the appointment with the customer
  * Called - Customer has been contacted
  * Left Message - Got the voicemail and left a message
  * Changed Mind - Customer has decided not to use the service
  * Complaint Processed - Customer complaint has been processed

* *Customer Statuses*

  * Prospect - Customer has requested a quote
  * Estimate - Operations Team has delivered an estimate
  * Contract - Customer has accepted the estimate and signed the contract

* *Employee Statuses*

  * Employeed - Employee is still working here
  * Fired - We mutually decided that it was time for you to leave
  * Leave - Employee has taken a leave of abscense

* *Notification Statuses*

  * Queued - Message read to be sent
  * Sent - Message has been sent
  * Read - Message has been read by customer

* *Todo Statuses*

  * New - This Todo hasn’t been looked at yet (read page not visited)
  * Assigned - This Todo is assigned to a CSR
  * Locked - This Todo is locked by a CSR
  * Completed - This Todo is completed
  * Closed - This Todo was closed without work being done

* *User Statuses*

  * Disabled - User account is disabled.  User can't login
  * Enabled - User account is enabled and can login
  * New - New account
  * Admin - This account has special privileges

.. _todo-table:

===============
**todo**
===============

This is the todo list for the CRMs.

============== ====================
Column Name    Type
============== ====================
rowid          (provided by SQLite)
type           text
customer_id    integer
status_id      integer
active         integer
date_created   text
============== ====================

The **type** field should have one of the following values:

* RFQ
* Complaint

.. _user-table:

========
**user**
========

============== ====================
Column Name    Type
============== ====================
rowid          (provided by SQLite)
email          text
password       text
employee_id    integer
customer_id    integer
status_id      integer
active         integer
date_created   text
============== ====================

.. note:: Each row in the **user** table should only have one of the following: **employee_id** or **customer_id**.  It should never have both.
