#!/usr/bin/env python3

with open ('input') as file:
  calories=0
  for line in file:
    if line.strip() == '':
      print(calories)
      calories=0
    else:
      calories+=int(line.strip())
    
