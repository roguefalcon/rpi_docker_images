#!/bin/bash

CLIENT=$1
if [ -z "$CLIENT" ]; then
    echo "USAGE: ./create_dev_container.sh <container_name> <ip_address>"
    exit 1
fi
IPADDR=$2
if [ -z "$IPADDR" ]; then
    echo "USAGE: ./create_dev_container.sh <container_name> <ip_address>"
    exit 1
fi

# Create the OVPN File
./generate_ovpn.sh $1

# Create the Dockerfile
mkdir $1
FILE=$1/Dockerfile
cat > $FILE << EOL
FROM python_dev:latest

COPY $1.ovpn /ovpnfile.ovpn

EXPOSE 22 5000-5010

CMD /tmp/start.sh
EOL
mv ~/$1.ovpn $1/.

# Build the Docker Container
docker build -t $1 $1

# Update OpenVPN
# Save IP Address in /etc/openvpn/ipp.txt
#echo "$1,$2" >> /etc/openvpn/ipp.txt
CCDFILE=/etc/openvpn/client/$1
cat > $CCDFILE << EOL
ifconfig-push $2 255.255.0.0
EOL
sleep 3

# Start the container
docker run --name $1 --privileged -d --hostname $1 $1
