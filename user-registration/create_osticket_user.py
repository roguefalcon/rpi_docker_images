#!/usr/bin/python

import MySQLdb
db=MySQLdb.connect(user='kproot',passwd="qwer",db="osticket",host='127.0.0.1')
c=db.cursor()
c.execute("""INSERT INTO ost_staff(dept_id, role_id, username, firstname, lastname, passwd, isactive, isadmin, isvisible,
                                   max_page_size, permissions, created, updated, signature) 
                           VALUES (1,2,%s,%s,%s,MD5(%s),1,1,1,25,'{"faq.manage":1}', now(), now(), '') """,
                    ('username', 'user', 'name', 'password')
         )
#db.commit()
