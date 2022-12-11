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
  content=file.readlines()
  filelen=int(len(content) / 3)
  index=0
  for x in range(0,filelen):
    combined=content[index:int(index+3)]
    index+=3
    for c in range(65,123):
      if combined[0].count(chr(c)) >= 1 and combined[1].count(chr(c)) >= 1 and combined[2].count(chr(c)) >= 1:
        total+=letter2value(chr(c))
        print(x,index, index + 3, chr(c))
  print(total)
