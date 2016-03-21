#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

def main():
	url = 'http://hostel.daiict.ac.in/index.php?option=com_eventtableedit&view=default&Itemid=2'
	webpage_data = requests.get(url)
	soup = BeautifulSoup(webpage_data.content, "lxml")

	names,rooms,dates = [],[],[]
	
	for i in range(30):
		date = 'evtd' + str(i) + '0'
		name = 'evtd' + str(i) + '1'
		room = 'evtd' + str(i) + '2'

		for link in soup.find_all("td", {"class":name}):
			names.append(link.text.strip())

		for link in soup.find_all("td", {"class":date}):
			dates.append(link.text.strip())

		for link in soup.find_all("td", {"class":room}):
			rooms.append(link.text.strip())

	print
	print '{:^13}'.format('Date:'), '{:^12}'.format('Room No.'), '{:^40}'.format('Name:')
	print '{:^13}'.format('-----'), '{:^12}'.format('--------'), '{:^40}'.format('-----')

	for i in range(30):
		print '{:^13}'.format(dates[i]),'{:^12}'.format(rooms[i]),'{:^40}'.format(names[i])


if __name__ == '__main__':
	main()