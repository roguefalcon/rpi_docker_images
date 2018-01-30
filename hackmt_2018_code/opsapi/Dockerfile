FROM alpine

# basic flask environment
RUN apk add --no-cache --update python3 \
	&& pip3 install flask

# Set the production port
ENV APP_PORT=80
ENV APP_DEBUG=0
#ENV APP_DEBUG=1

# Create the folders and add the application
RUN mkdir /opsapi
COPY load_sql.py /opsapi/load_sql.py
RUN /opsapi/load_sql.py
RUN mv sql.db /opsapi/sql.db
COPY opsapi /opsapi/opsapi
COPY run.py /opsapi/run.py

# Run the flask app
WORKDIR /opsapi
CMD ./run.py
