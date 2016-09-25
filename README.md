dev team is Mike Vu, Raymond Kim, Tim Lui, and Kevin Chen

We will be working on the slack implementation and bots that will aggragate all the data from piazza, blackboard, and email.

Here are the assignments:  
Kevin - ruby machanize and slack api  
Raymond - blackboard and IMAP  
Mike - Piazza api  
Tim - Heroku/server

Server (Raspi) TODO:
1. Install Debian

2. Setup local SSH and SFTP server

3. Either setup OpenVPN with certificates
	OR
	Setup SSH with certificates and brute force protection
4. Setup iptables firewall, allow all outgoing, block all incoming EXCEPT for the abovementioned ports (with request limiting), and HTTP port 80 (limited to Slack servers only)

5. Setup seperate user account and group for running our apps (isolation from main admin/root account)

6. Enable logging for all incoming and outgoing requests to RAMDISK (if it doesn't exist make one, this is to prevent excess writes to SD card)

7. Setup cron job for auto-updating on SECURITY patches only, check once a day (system updates will be done manually)

8. Set timer for scripts if necessary (e.g will check email once per 15 minutes)

Router (Kevin's router?) TODO:

1. Put the Raspi on either a seperate subnet or VLAN for isolation from home network, set firewall to prevent comms between subnets or VLANs (I really hope your router supports this feature, its a business feature but very important)

2. Enable dynamic DNS and register with a service (I personally use duckdns, you guys might have other preferences)

3. Port forward abovementioned ports to the server
