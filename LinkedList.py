#!/usr/bin/env python

__metaclass__ = type

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def setData(self,data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self,next):
        self.next = next
    
    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None

class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None

    def addNode(self,node):
       if self.length == 0:
	  self.addFirst(node)
       else:
	  self.addLast(node)

    def addFirst(self,node):
	newNode = node
        newNode.next = self.head #newNode.next ---> None
        self.head = newNode      #self.head --> point to first node (newNode)
        self.length += 1         #the Length of LinkedList + 1

    def addLast(self,node):
        currentNode = self.head  # point to currentNode
        
	while currentNode != None:
	      currentNode = currentNode.next

        newNode = node
	newNode.next = None #newNode will be placed at the end of List.
        currentNode.next = newNode
        self.length = self.length + 1

    def printList(self):
        nodeList=[] # Python List will store the LinkedList's data
        currentNode = self.head
        while currentNode != None:
		nodeList.append(currentNode.data)
                currentNode = currentNode.next

	print nodeList[]


    def addAtPos(self,node,pos):  #Method to add Node at specific position
        count = 0       #Local Count variable
        currentNode  = self.head  #Current Node point to head
        previousNode = self.head  #Previous Node point to head

	if pos > self.length or pos < 0:
	    print "The Position does not exist,Please Enter a Valid Position"

        else:
	    while currentNode.next != None or count < pos:
		count = count + 1
		if count == pos:
                    previousNode.next = node
		    node.next = currentNode
		    self.length +=1
		    return 
		else:
		    previousNode = currentNode
		    currentNode = currentNode.next





if __name__ =="__main__":
	
   n1 = Node(15)
   n2 = Node(16)
   n3 = Node(190)
   
   aLinkedList = LinkedList()
   aLinkedList.addNode(n1)
   aLinkedList.addNode(n2)	
   aLinkedList.addNode(n3)

   aLinkedList.printList()













 
