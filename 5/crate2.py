#!/usr/bin/env python3

crates=[
['T','D','W','Z','V','P'],
['L','S','W','V','F','J','D'],
['Z','M','L','S','V','T','B','H'],
['R','S','J'],
['C','Z','B','G','F','M','L','W'],
['Q','W','V','H','Z','R','G','B'],
['V','J','P','C','B','D','N'],
['P','T','B','Q'],
['H','G','Z','R','C']
]

with open('input1') as file:
  move=file.readlines()
  for m in move:
    action=m.split()
    fr=int(action[3]) - 1  
    to=int(action[5]) - 1
    number=int(action[1])
    move=crates[fr][int(-1 * number):]
    crates[to]=crates[to]+move
    for x in range(1,number+1):
      crates[fr].pop()
  code=''
  for c in crates:
    code+=str(c[-1])
  print(code)
