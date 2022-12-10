#!/usr/bin/env python3
import copy

with open('input') as file:
  lines=file.readlines()
  trees=[]
  trees1=[]
  trees2=[]
  trees3=[]
  trees4=[]
  visible=[]
  for line in lines:
    line=line.strip()
    trees.append([*line])
    trees1.append([*line])
    trees2.append([*line])
    trees3.append([*line])
    trees4.append([*line])
    visible.append([*line])
  for row in trees:
    print(row)
  print('---')

def checktree(list,reverse):
  l=len(list)
  if reverse == True:
    list.reverse()
  output=[None] * l
  for x in range(1,l-1):
    for y in range(x+1,l):
      if list[x] <= list[y]: # check if tree is blocked, if blocked break out of loop, no need to continue
        break
      else:
        output[x]='V'
  output.reverse()
  return output

def check(list,reverse):
  l=len(list)
  if reverse:
    list.reverse()
  output=copy.deepcopy(list)
  for x in range(1,l-1):
    if list[x] > max(list[x+1:]):
       output[x]='V'
  if reverse:
    output.reverse()
  return output
  
# Left
total=0
vis=[]
for i, r in enumerate(trees):
  if i == 0 or i == len(trees) - 1:
    vis.append(r)
  else:
     vis.append(check(r,True))
for r in vis:
  print(r)
  total+=(r.count('V'))
print(total)
left=copy.deepcopy(vis)

# Right
total=0
vis=[]
for i, r in enumerate(trees1):
  if i == 0 or i == len(trees1) - 1:
    vis.append(r)
  else:
    vis.append(check(r,False))
for r in vis:
  print(r)
  total+=(r.count('V'))
print(total)
right=copy.deepcopy(vis)

# Top
list=[]
transpose=[]
for j in range(len(trees3[0])): # columns
  for i in range(len(trees3)): # rows
    list.append(trees3[i][j])
  transpose.append(list)
  list=[]
total=0
vis=[]
for i, r in enumerate(transpose):
  if i == 0 or i == len(transpose) - 1:
    vis.append(r)
  else:
    vis.append(check(r,True))
list=[]
transpose=[]
for j in range(len(vis[0])): # columns
  for i in range(len(vis)): # rows
    list.append(vis[i][j])
  transpose.append(list)
  list=[]
for r in transpose:
  print(r)
  total+=(r.count('V'))
print(total)
top=copy.deepcopy(transpose)

# Bottom
list=[]
transpose=[]
for j in range(len(trees3[0])): # columns
  for i in range(len(trees3)): # rows
    list.append(trees3[i][j])
  transpose.append(list)
  list=[]
total=0
vis=[]
for i, r in enumerate(transpose):
  if i == 0 or i == len(transpose) - 1:
    vis.append(r)
  else:
    vis.append(check(r,False))
list=[]
transpose=[]
for j in range(len(vis[0])): # columns
  for i in range(len(vis)): # rows
    list.append(vis[i][j])
  transpose.append(list)
  list=[]
for r in transpose:
  print(r)
  total+=(r.count('V'))
print(total)
bottom=copy.deepcopy(transpose)

total=(len(left)-2)*2+len(left[0]*2)
for x in range(len(left)):
  for y in range(len(left[0])):
    if left[x][y] == 'V' or right[x][y] == 'V' or bottom[x][y] == 'V' or top[x][y] == 'V':
      total+=1

print('Vis', total)

# part 2
scores=[]
for col in range(len(trees4[0])): 
  for row in range(len(trees4)):
    check=trees4[row][col]
    left = 0
    for t in range(col-1, -1, -1):
      left+=1
      if trees4[row][t] >= check:
        break
    right=0
    for t in range(col+1, len(trees4[0])):
      right+=1
      if trees4[row][t] >= check:
        break
    up=0
    for t in range(row-1, -1, -1):
      up+=1
      if trees4[t][col] >= check:
        break
    down=0
    for t in range(row+1, len(trees4)):
      down+=1
      if trees4[t][col] >= check:
        break
    scores.append(left*right*up*down)
print('max', max(scores))
    
    
