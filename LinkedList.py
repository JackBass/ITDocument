#!/usr/bin/env python


class Node:
    def __init__(self,data):
        self.data = data
	self.next = None
    def setData(self,data):
    	self.data = data
    def getData(self):
    	return self.data
    	
