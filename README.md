# rpi_docker_images
[BETA] Dockerfiles for the Raspberry PI and ODRIOD ARM Makerboards

These images are being created specifically for HackMT at MTSU:
http://hackmt.eventbrite.com

The goal is to create a complete continuous integration environment for the hack-a-thon that runs on a raspberry pi / odriod-c2 cluster.

I'm planning to use the following
- [x] Docker
- [x] MySQL
- [x] OpenLDAP
- [x] Jenkins
- [ ] OSTicket
- [ ] SonarQube (if I can get it to run on an Odriod C2)
- [x] Dokuwiki
- [ ] Kubernetes

__Use at your own risk__

In the spirit of time, I'm breaking a few rules.  For example, this will run on a private encrypted wifi network behind a firewall.  It is only intended to run
for the HackMT event.  This means I'm ok with things like running nginx as root or not setting up SSL for osticket (because the Raspberry Pi's will already be
under enough load without SSL decryption).


