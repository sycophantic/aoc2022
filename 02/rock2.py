#!/usr/bin/env python3

score={
        'AX':'3', # rock lose scissor 0+3
        'AY':'4', # rock tie rock 3+1
        'AZ':'8', # rock win paper 6+2
        'BX':'1', # paper lose rock 0+1
        'BY':'5', # paper tie paper 3+2
        'BZ':'9', # paper win scissors 6+3
        'CX':'2', # scissors lose paper 0+2
        'CY':'6', # scissors tie scissors 3+3
        'CZ':'7'  # scissors win rock 6+1
}


with open ('input') as file:
  total=0
  for line in file:
    game=line.split()
    total+=int(score[game[0]+game[1]])
print(total)
    


  
