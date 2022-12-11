#!/usr/bin/env python3

with open('input') as file:
  total=0
  for line in file:
    pairs=line.strip().split(',')
    e1=pairs[0].split('-')
    e2=pairs[1].split('-')
    if int(e1[0]) >= int(e2[0]) and int(e1[1]) <= int(e2[1]):
      total+=1
      print(e1,e2)
    elif int(e2[0]) >= int(e1[0]) and int(e2[1]) <= int(e1[1]):
      print(e1,e2)
      total+=1
      
  print(total)
