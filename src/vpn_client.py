#!/usr/bin/env python

from subprocess import call
import config

# VPN manipulation
def consoleVPN(action, region):
	call(["sudo", "systemctl", action, "openvpn@{}".format(region)])

def startVPN(region):
	consoleVPN("start", region)
	config.writeCurrentVPN(region)

def stopVPN():
	consoleVPN("stop", config.readCurrentVPN())
	config.removeCurrentVPN()

def enableVPN(region):
	consoleVPN("enable", region)

def disableVPN(region):
	consoleVPN("disable", region)

def restartVPN():
	region = config.readCurrentVPN()
	stopVPN()
	startVPN(region)

def changeVPN(new_region):
	stopVPN()
	startVPN(new_region)

def logsVPN():
	try:
		call(["watch", "-n", "1", "journalctl -u openvpn@{} | tail -n 10".format(config.readCurrentVPN())])
	except:
		pass
	call(["stty", "sane"])
