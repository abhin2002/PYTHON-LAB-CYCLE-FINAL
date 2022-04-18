# -*- coding: utf-8 -*-
"""3_cycle2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I3a7kFOEBp5B8xYEOi4NeAycX_BrxMDY
"""

def read_file(filename):
  a = open(filename,"r")             #reading the file iris.json
  data = a.readlines()               #a list having each line of the file as an element
  a.close()
  return data
  
data = read_file("iris.json")
                             
#print(data)                   
import json

def read_dictionary1(file):
  a = open(file,"r")
  dictionary1 = json.load(a)             #Convert into dictionary1 odatajects.
  dictionary11 = dictionary1
  a.close()
  print(dictionary1)
  return(dictionary1)

dictionary1 = read_dictionary1("iris.json")

#[print(i['species']) for i in dictionary1]

#def print_setosa(dictionary1):
for i in dictionary1:               
  if i['species'] == 'setosa':        #printing the details of all flowers whose species is "setosa".
    print(i)

#print_setosa(dictionary1)

l_species = []

def species(dictionary1):
  for i in dictionary1:                  #forming a list of type of species
    if i['species'] not in l_species:
      l_species.append(i['species'])
  return(l_species)

l_species = species(dictionary1)
#print(l_species)

l_area_sepal1 = []
l_area_petal1 = []
l_area_sepal2 = []
l_area_petal2 = []
l_area_sepal3 = []
l_area_petal3 = []

def area(dictionary1,l_area_petal1,l_area_petal2,l_area_petal3,l_area_sepal1,l_area_sepal2,l_area_sepal3,l_species):

  for i in dictionary1:
    ptlarea = (i['sepalLength']*i['sepalWidth'])  #calculating petal area of each flower 
    splarea = (i['petalLength']*i['petalWidth'])  #calculating sepel area of each flower
    totalarea = ptlarea + splarea                 #calculating total area of each flower       
    i.update({'totalArea' : totalarea})           #adding total area to the dictionary1
    if i['species'] == l_species[0]:
      l_area_sepal1.append(i['sepalLength']*i['sepalWidth'])      
      l_area_petal1.append(i['petalLength']*i['petalWidth'])
    elif i['species'] == l_species[1]:                                 #calculating sepal and petal area of different species
      l_area_sepal2.append(i['sepalLength']*i['sepalWidth'])
      l_area_petal2.append(i['petalLength']*i['petalWidth'])
    elif i['species'] == l_species[2]:
      l_area_sepal3.append(i['sepalLength']*i['sepalWidth'])
      l_area_petal3.append(i['petalLength']*i['petalWidth'])

  # print(l_area_sepal1)
  # print(l_area_petal1)
  # print(l_area_sepal2)
  # print(l_area_sepal2)
  # print(l_area_sepal3)
  # print(l_area_sepal3)

  print(l_species[0])
  print("Greatest sepal area : ",max(l_area_sepal1))                
  print("Minimum petal area  : ",min(l_area_petal1))                
  print(" ")                                                   
  print(l_species[1])                                                #printing the max sepal and minimum petal area of different species
  print("Greatest sepal area : ",max(l_area_sepal2))
  print("Minimum petal area  : ",min(l_area_petal2))
  print(" ")
  print(l_species[2])
  print("Greatest sepal area : ",max(l_area_sepal3))
  print("Minimum petal area  : ",min(l_area_petal3))
  print("    ")
  #print(dictionary1)
  print("    ")
  return(dictionary1)

dictionary1 = area(dictionary1,l_area_petal1,l_area_petal2,l_area_petal3,l_area_sepal1,l_area_sepal2,l_area_sepal3,l_species)

def sorted_dictionary1(dictionary1):  
  sorteddictionary1 = (sorted(dictionary1, key = lambda i:i ['totalArea'] ))   #Sort the list of dictionaries according to the total area of sepal and petal
  print("                                    Details of sorted list")
  print("---------------------------------------------------------------------------------------------------")
  print('Sepal Length     Sepal Width     Petal Length        Petal Width        Species         Total Area      ')

  for i in sorteddictionary1:
    print('  ',i["sepalLength"]," \t","\t",i["sepalWidth"],'\t\t',i['petalLength'],'\t\t',i['petalWidth'],'\t\t',i['species'],'\t',i['totalArea'])

sorted_dictionary1(dictionary1)

 # print(sorteddictionary1)