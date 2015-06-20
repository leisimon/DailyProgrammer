#!/usr/bin/python

class TodoList():
	def __init__(self):
		self.mylist = []

	def add(self, item):
		self.mylist.append(item)

	def delete(self, item):
		if item in self.mylist:
			self.mylist.remove(item)

	def view(self):
		for i in self.mylist:
			print i