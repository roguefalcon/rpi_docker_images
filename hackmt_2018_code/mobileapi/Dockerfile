FROM alpine

# basic flask environment
RUN apk add --no-cache --update python3 \
	&& pip3 install flask

# Set the production port
ENV APP_PORT=80
ENV APP_DEBUG=0
#ENV APP_DEBUG=1

# Create the folders and add the application
RUN mkdir /mobileapi
COPY load_sql.py /mobileapi/load_sql.py
RUN /mobileapi/load_sql.py
RUN mv sql.db /mobileapi/sql.db
COPY mobileapi /mobileapi/mobileapi
COPY run.py /mobileapi/run.py

# Run the flask app
WORKDIR /mobileapi
CMD ./run.py
