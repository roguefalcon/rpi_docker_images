# rpi_docker_images
[BETA] Dockerfiles for the Raspberry PI and ODRIOD ARM Makerboards

These images are being created specifically for HackMT at MTSU:
http://hackmt.eventbrite.com

The goal is to create a complete continuous integration environment for the hack-a-thon that runs on a raspberry pi / odriod-c2 cluster. I'm trying to support up to 30 developers on 4 odroids :-)

I'm planning to use the following
- [x] Docker
- [x] MySQL
- [x] OpenLDAP
- [x] Jenkins
- [x] OSTicket
- [-] SonarQube (needs 3 gigs of ram :-( )
- [x] Dokuwiki
- [x] Python Dev VM
- [x] Node.js Dev VM
- [x] .Net Core Dev VM (this will only run the app.  You still have to develop locally.)

__Use at your own risk__

In the spirit of time, I'm breaking a few rules.  For example, this will run on a private encrypted wifi network behind a firewall.  It is only intended to run
for the HackMT event.  This means I'm ok with things like running nginx as root or not setting up SSL for osticket (because the Raspberry Pi's will already be
under enough load without SSL decryption).
