#!/usr/bin/env python3

def letter2value(letter):
  value=ord(letter)
  if value < 91: # uppercase
    output=value-38
  else: # lowercase
    output=value-96
  return int(output)

with open ('input') as file:
  total=0
  matches=[]
  for line in file:
    check=[]
    ruck=line.strip()
    clen=int(len(ruck) / -2)
    c1=ruck[clen:]
    c2=ruck[:clen]
    for i in c1:
      print(i, c2.count(i))
      if c2.count(i) > 0 and check.count(i) == 0:
        matches.append(i)
        check.append(i)
  for m in matches:
    total+=letter2value(m)
  print(total)
