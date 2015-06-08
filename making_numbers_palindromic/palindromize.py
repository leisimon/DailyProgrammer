#!/usr/bin/python

import sys

def palindromize(num):
	steps = 0
	curr_num = num
	while not is_palindromic(curr_num):
		curr_num = curr_num + int(str(curr_num)[::-1])
		steps += 1
	print str(num) + " gets palindromic after " + str(steps) + " steps: " + str(curr_num)

def is_palindromic(num):
	rev_num = int(str(num)[::-1])
	if num == rev_num:
		return True
	return False

def main():
	file = open(sys.argv[1], "r")
	input = file.read().split("\n")
	for i in input:
		palindromize(int(i))
	file.close()

if __name__ == "__main__":
    main()