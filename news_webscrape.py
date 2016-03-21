#!/usr/bin/python

''' Scrapes data from the given RSS Feed '''

import os
from bs4 import BeautifulSoup
import requests
import time

def main():
	os.system("clear")
	print 'Today\'s News:\n=============\n'
	print 'Press enter to load new headline, type "quit" to exit.'
	raw_input()

	try:
		url = requests.get("http://feeds.reuters.com/reuters/INtopNews")
		soup = BeautifulSoup(url.text,"lxml")
		#print soup.prettify()

	
		for link in soup.find_all("item"):
			print
			print '**' + link.title.text + '**'
			print '--' + '-'*len(link.title.text) + '--'
			stn =  str(link.description.text).split("<br")
			print stn[0]
			print
			print 'Link to full article:',link.guid.text
			print
			inp = raw_input()
			if inp in ["q","Q","Quit","quit","QUIT"]:
				break
		print '\nFinished Fetching Articles.\n'

	except Exception as e:
		#print e
		print 'Cannot retrive data. Check Internet connection.\n'


if __name__ == '__main__':
	main()
