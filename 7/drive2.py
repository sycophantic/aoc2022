#!/usr/bin/env python3

with open('input') as file:
  lines=file.readlines()
  curdir=[]
  total=0
  dirs={}
  dirlist=[]
  final={}
  for line in lines:
    line=line.strip().split()
    if line[0] == '$':
      total=0
      command=line[1]
      if command == 'cd':
        if line[2] == '..':
          curdir.pop()
        else:
          curdir.append(line[2])
          dirlist.append(' '.join(curdir))
      elif command == 'ls':
          continue
    elif line[0] == 'dir':
      continue
    else:
        key=' '.join(curdir)
        if key in dirs:
          dirs[key] += int(line[0])
        else:
          dirs[key] = int(line[0])
  total=0
  for x in dirs:
    if dirs[x] <= 100000:
      total+=dirs[x]

  dirlist.sort()

  for x in dirlist:
    for y in dirs:
      if y.startswith(x):
        if x in final:
          final[x]+=dirs[y]
        else:
          final[x]=dirs[y]

  used=final['/']
  free=70000000 - final['/']
  needed=30000000 - free
  print('used', used, 'free', free, 'needed', needed)

  sizes=[]
  for x in final:
    sizes.append(final[x])
  sizes.sort()
  for x in sizes:
    if x >= needed:
      print(x)
      break
