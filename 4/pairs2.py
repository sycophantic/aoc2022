#!/usr/bin/env python3

with open('input') as file:
  total=0
  for line in file:
    pairs=line.strip().split(',')
    e1=pairs[0].split('-')
    e2=pairs[1].split('-')
    r1=range(int(e1[0]),int(e1[1])+1)
    r2=range(int(e2[0]),int(e2[1])+1)
    for x in r1:
      if x in r2:
        total+=1
        break
  print(total)
