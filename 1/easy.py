#!/usr/bin/env python3
# Daily Programmer #1, easy edition
# http://redd.it/pih8x

import argparse
import datetime

def main():
	parser = argparse.ArgumentParser(
		description='Log your name, age, and reddit username.')
	parser.add_argument('name', type=str, nargs='?')
	parser.add_argument('age', type=int, nargs='?')
	parser.add_argument('username', type=str, nargs='?')
	args = parser.parse_args()
	if args.name is not None:
		name = args.name
	else:
		name = input('What is your name? ')
	if args.age is not None:
		age = args.age
	else:
		age = input('What is your age? ')
	if args.username is not None:
		username = args.username
	else:
		username = input('What is your reddit username? ')
	print('your name is %s, you are %s years old, and your username is %s' % (
		name, age, username))
	with open('easy.log', 'a') as log:
		log.write('%s: name="%s", age=%s, username=%s\n' % (
			datetime.datetime.now(), name, age, username))


if __name__ == '__main__':
	main()
