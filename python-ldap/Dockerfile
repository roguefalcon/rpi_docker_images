FROM kprpi

RUN apt-get update && apt-get upgrade -y

# Setup Python
RUN apt-get -y install python python-pip python-dev python-ldap
RUN apt-get -y install python-ldap
RUN pip install Flask
RUN pip install tinydb

# Move the files in
RUN mkdir /var/user_reg
COPY templates /var/user_reg/templates
COPY user_registration.py /var/user_reg/user_registration.py
COPY last_uid.txt /var/user_reg/last_uid.txt

# Setup the database
COPY load_db.py /tmp/load_db.py
RUN chmod u+x /tmp/load_db.py && /tmp/load_db.py
RUN cp /db.json /var/user_reg/db.json

EXPOSE 80

# Run the command on port 5000 mapped to port 80
CMD /var/user_reg/user_registration.py
