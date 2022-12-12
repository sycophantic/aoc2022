#!/usr/bin/env python3

import operator
import math

operatorlookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

monkey=0
items=[]
operation=''
test=''
t=''
f=''
monkeys=[]

with open ('input') as file:
    lines=file.readlines()
    for i, line in enumerate(lines):
      line=line.strip()
      if "Monkey" in line:
        monkey=line.split(' ')[1].replace(':','')
        items=list(map(int, lines[i+1].split(": ")[1].split(", ")))
        operation=lines[i+2].strip().replace('Operation: ','')
        test=int(lines[i+3].strip().replace('Test: divisible by ',''))
        t=int(lines[i+4].strip().replace('If true: throw to monkey ',''))
        f=int(lines[i+5].strip().replace('If false: throw to monkey ',''))
        monkeys.append({
          'items':items,
          'operation':operation,
          'test':test,
          't':t,
          'f':f,
          'inpections':0
          })
        #print(monkey)
        #print(items)
        #print(operation)
        #print(test)
        #print(t)
        #print(f)

rounds=10000 * len(monkeys) # misunderstood, a round is AFTER all monkeys go
round=1
monkeycount=len(monkeys)
currentmonkey=0
lcm=math.lcm(2, 13, 3, 17, 19, 7, 11, 5)

while round <= rounds:
#  print('Round', round, 'Monkey', currentmonkey)
  op=[]
  worry=0
  for item in monkeys[currentmonkey]['items']:
    ops=monkeys[currentmonkey]['operation'].split()
    ops.reverse()
    worry=item
    op=operatorlookup.get(ops[1])
#    print('inpecting', worry)
    if ops[0] == 'old' and ops[2] == 'old':
      worry=int(op(int(worry),int(worry)) % lcm)
    else:
      worry=int(op(int(ops[0]),int(worry)) % lcm)
#    print('new value', worry)
    mod=worry % monkeys[currentmonkey]['test']
    if mod == 0:
      monkeys[monkeys[currentmonkey]['t']]['items'].append(worry)
#      print('div by',monkeys[currentmonkey]['test'])
#      print('div by',monkeys[currentmonkey]['test'], 'thrown to', monkeys[currentmonkey]['f'] )
    else:
      monkeys[monkeys[currentmonkey]['f']]['items'].append(worry)
#      print('not div by',monkeys[currentmonkey]['test'], 'thrown to', monkeys[currentmonkey]['f'] )
#    print('adding to inpections')
    monkeys[currentmonkey]['inpections']+=1
#  print('clearing list')
  monkeys[currentmonkey]['items'].clear()
  currentmonkey+=1 
  if currentmonkey >= monkeycount:
    currentmonkey=0
  round+=1
#  for i, m in enumerate(monkeys):
#    print('Monkey', i, m['items'])

ins=[]
for i, x in enumerate(monkeys):
  print('Monkey',i,x['inpections'])
  ins.append(x['inpections'])
ins.sort()
ins.reverse()
print('Answer', ins[0]*ins[1])
