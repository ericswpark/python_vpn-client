#!/usr/bin/env python

from configparser import SafeConfigParser

# Configuration
def writeConfig(key, value):
	config = SafeConfigParser()
	config.read('config.ini')
	if not config.has_section('main'):
		config.add_section('main')
	config.set('main', key, value)

	with open('config.ini', 'w') as config_file:
		config.write(config_file)

def removeConfig(key):
	config = SafeConfigParser()
	config.read('config.ini')
	config.remove_option('main', key)
	
	with open('config.ini', 'w') as config_file:
		config.write(config_file)

def readConfig(key):
	config = SafeConfigParser()
	config.read('config.ini')
	return config.get('main', key)


##
# ONLY CALL THESE TWO
##

def writeCurrentVPN(region):
	writeConfig('currentVPN', region)

def readCurrentVPN():
	return readConfig('currentVPN')

def removeCurrentVPN():
	removeConfig('currentVPN')
