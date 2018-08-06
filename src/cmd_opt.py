#!/usr/bin/env python

import argparse

# Command-line helpers
def get_parser():
	parser = argparse.ArgumentParser(description=('A simple VPN script for OpenVPN client'))
	
	commands = parser.add_mutually_exclusive_group()
	commands.add_argument('--start', '-s',
					action="store", dest="START_REGION",
					help='Start the VPN with the supplied region.')
					
	commands.add_argument('--quit', '-q',
					action="store_true",
					help='Stops the VPN.')
					
	commands.add_argument('--restart', '-r',
					action="store_true",
					help='Restarts the VPN.')
					
	commands.add_argument('--change', '-c',
					action="store", dest="CHANGE_REGION",
					help='Hot-swaps the VPN region. ' +
					"The region is NOT optional.")
					
	commands.add_argument('--logs', '-l',
					action="store_true",
					help='Shows VPN logs.')

	return parser
