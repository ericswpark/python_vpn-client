#!/usr/bin/env python3

import cmd_opt
import vpn_client

if __name__ == "__main__":
	parser = cmd_opt.get_parser()	# Start the command-line argument parsing
	args = parser.parse_args()	# Read the command-line arguments


	# VPN start
	if args.START_REGION is not None:
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
	elif args.CHANGE_REGION is not None:
		vpn_client.stopVPN()
		vpn_client.startVPN(args.CHANGE_REGION)
	else:
		print("Fatal error?")

