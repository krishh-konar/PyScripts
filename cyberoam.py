'''
author:Krishanu
A cyberoam client emulator that automatically logs in after every 2 hours.

NOTE: create a file "login.py and initialize 2 string variables username and password with your
credentials before running the script.
'''

from login import username,password
import requests
import time
import signal
import re
import cookielib
import sys
import os
import urllib
from bs4 import BeautifulSoup
import mechanize
import ssl
import signal

#logout once an interrupt is recieved.
def signal_handler(signal, frame):
	logout()
	time.sleep(3)
	sys.exit(0)


#DA-IICT's Cyberoam portal
url = "https://10.100.56.55:8090/httpclient.html"

def browser():
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders = [('user-agent','Chrome')]

	# Cookie Jar
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)

	# Browser options
	br.set_handle_equiv(True)
	br.set_handle_gzip(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	return br

def post_request(username,password,value,mode):
	
	br = browser()
	#POST request values
	values ={
		"mode":mode,
		"username":username,
		"password":password,
		"btnSubmit":value
	}

	data = urllib.urlencode(values)
	page = br.open(url,data)
	response = page.read()
	br._factory.is_html = True
	soup = BeautifulSoup(response,"lxml")

	regex = re.compile(r"<message><!\[CDATA\[(.*)\]\]><\/message>")

	x = re.search(regex,response)
	print username + ": " + x.group(1)
	return br

def login():
	br = post_request(username,password,"Login","191")
	return br

def logout():
	br = post_request(username,password,"Logout","193")
	return br

def bypass_ssl():
	### Bypassing SSL certification ###
	try:
	    _create_unverified_https_context = ssl._create_unverified_context
	except AttributeError:
	    # Legacy Python that doesn't verify HTTPS certificates by default
	    pass
	else:
	    # Handle target environment that doesn't support HTTPS verification
	    ssl._create_default_https_context = _create_unverified_https_context
	return

def main():
	bypass_ssl()
	signal.signal(signal.SIGINT, signal_handler)

	while True:
		login()
		time.sleep(6000)
	
if __name__ == '__main__':
	main()
