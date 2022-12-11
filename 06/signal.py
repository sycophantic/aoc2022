#!/usr/bin/env python3

with open('input') as file:
    lines=file.readlines()
    for line in lines:
      buffer=[*line.strip()]
      l=len(buffer)
      for x in range(0,l):
        setlen=len(set(buffer[x:x+4]))
        if setlen == 4:
          print(x+4)
          break
