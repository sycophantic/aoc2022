#!/usr/bin/env python3

cycle=1
x=1
values={}
cyclecheck=[20,60,100,140,180,220]
total=0

with open('input') as file:
  lines=file.readlines()
  for line in lines:
    line=line.strip()
    func=line.split()
    if func[0] == 'noop':
      cycle+=1
      values[cycle]=x
    else:
      cycle+=2
      x+=int(func[1])
      values[cycle]=x
      values[cycle-1]=x

for x in cyclecheck:
  if x in values:
    total+=x*values[x]
    print(x, values[x],x*values[x])
  elif x - 1 in values:
    total+=x*values[x - 1]
    print(x, values[x - 1],x*values[x-1])

print('signal', total)

mid=0
row=-1
rows=[['.'] * 40] * 6
output=''
posl=[]
for cycle in range(0,240):
  rowcalc = (cycle) % 40
  #print(cycle,row,rowcalc)
  if rowcalc == 0:
    row+=1
  if cycle in values:
    pos=values[cycle]
    posl=[*range(pos -1,pos +2)]

    if rowcalc in posl:
      output=output + '#'
    else:
      output=output + '.'
  elif cycle - 1 in values:
    pos=values[cycle - 1]
    posl=[*range(pos -1,pos +2)]

    if rowcalc in posl:
      output=output + '%'
    else:
      output=output + '.'
  else:
      output=output + '.'

   
print(output[0:40])
print(output[40:80])
print(output[80:120])
print(output[120:160])
print(output[160:200])
print(output[200:240])
print(len(output))