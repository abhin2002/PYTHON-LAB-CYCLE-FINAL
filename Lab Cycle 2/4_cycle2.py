# -*- coding: utf-8 -*-
"""4_cycle2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WlZQEfZ-PHZ8-7lwzE6021tOsOHAPYfw
"""

#4. Write a program to create a class Box with data members length, 
#   breadth, height, area, and volume. Provider constructor that enables 
#   initialization with one parameter (for cube), two parameters (for
#   square prism) three parameters (rectangular prism). Also, provide 
#   functions to calculate area and volume.
#   Create a list of N boxes with random measurements and print the 
#   details of the box with maximum volume: area ratio.





class Box:                        #creating class box
  __length = None
  __breadth = None
  __height = None
  __area = None
  __volume = None

  def __init__(self, *p):        #multiple constructor to take diiferent number of arguments
    if len(p) == 1:
      self.__length = p[0]
      self.__breadth = p[0]
      self.__height = p[0]
    elif len(p) == 2:
      self.__length = p[0]
      self.__breadth = p[0]
      self.__height = p[1]
    elif len(p) == 3:
      self.__length = p[0]
      self.__breadth = p[1]
      self.__height = p[2]

  def volume(self):
    self.__volume = self.__length*self.__breadth*self.__height
                                                                     #function to calculate area and volume
  def area(self):
    self.__area = 2*(self.__length*self.__length + self.__breadth*self.__breadth + self.__height*self.__height)

  def display(self):
    print("Box Details")                                            #function to print details of box
    print("Length  = ",self.__length)
    print("Breadth = ",self.__breadth)
    print("Height  = ",self.__height)
    print("Area    = ",self.__area)
    print("Volume  = ",self.__volume)

  def ratio(self):                                                 #function to calculate volume area ratio
    r= (self.__volume)/(self.__area)
    return r

import random

n=int(input("Enter the number of objects that want to made : "))

def putdata():
  ls1 = []
  count=0
  for i in range(0,n,3):                                            #providing random inputs
    while(count!=n):
      ls1.insert(i,Box(random.randrange(1,50,1)))
      count = count+1
      ls1.insert(i+1,Box(random.randrange(1,50,1),random.randrange(1,50,1)))
      count = count+1
      ls1.insert(i+2,Box(random.randrange(1,50,1),random.randrange(1,50,1),random.randrange(1,50,1)))
      count = count+1
      break;
  return(ls1)

ls1=putdata()

putdata()

for i in range(0,n):        #sorting area and volume
  ls1[i].area()
  ls1[i].volume()


ls2 = []

def display_fn():
  for i in range(0,n):
    ls2.append(ls1[i].ratio())
    ls1[i].display()
    print("Ratio   : ",ls1[i].ratio())
    print(" ")

display_fn()

def display_max(): 
  for i in range(0,n):                           #details of the box with maximum volume: area ratio.
    if max(ls2) == ls1[i].ratio():
      print(" ")
      ls1[i].display()
      print("Greatest Ratio",ls1[i].ratio())

display_max()