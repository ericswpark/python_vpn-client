#!/usr/bin/env python3

import cmd_opt
import vpn_client

if __name__ == "__main__":
	parser = cmd_opt.get_parser()	# Start the command-line argument parsing
	args = parser.parse_args()	# Read the command-line arguments


	# VPN start
	if args.start is True:
		print("Starting the VPN")
		vpn_client.startVPN(args.START_REGION)
	elif args.quit is True:
		print("Stopping the VPN")
		vpn_client.stopVPN()
	elif args.restart is True:
		print("Restarting the VPN")
		vpn_client.restartVPN()
	elif args.logs is True:
		vpn_client.logsVPN()
	elif args.change is True:
		vpn_client.stopVPN()
		vpn_client.startVPN(args.CHANGE_REGION)
	else:
		print("Fatal error?")

