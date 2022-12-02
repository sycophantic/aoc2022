#!/usr/bin/env python3

score={
        'AX':'4', # rock rock tie 3+1
        'AY':'8', # rock paper win 6+2
        'AZ':'3', # rock scissors lose 0+3
        'BX':'1', # paper rock lose 0+1
        'BY':'5', # paper paper tie 3+2
        'BZ':'9', # paper scissors win 6+3
        'CX':'7', # scissors rock win 6+1
        'CY':'2', # scissors paper lose 0+2
        'CZ':'6'  # scissors scissors tie 3+3
}


with open ('input') as file:
  total=0
  for line in file:
    game=line.split()
    total+=int(score[game[0]+game[1]])
print(total)
    


  
