FROM alpine

# basic flask environment
RUN apk add --no-cache --update python3 \
	&& pip3 install flask

# Set the production port
ENV APP_PORT=80
ENV APP_DEBUG=0
#ENV APP_DEBUG=1

# Create the folders and add the application
RUN mkdir /crmapi
COPY load_sql.py /crmapi/load_sql.py
RUN /crmapi/load_sql.py
RUN mv sql.db /crmapi/sql.db
COPY crmapi /crmapi/crmapi
COPY run.py /crmapi/run.py

# Run the flask app
WORKDIR /crmapi
CMD ./run.py
