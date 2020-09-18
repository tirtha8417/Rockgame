from random import randint

Player= input('rock(r),paper(p) or scissors(s)?')

print(Player, 'vs', end=' ')

chosen= randint(1,3)
#print(chosen)


if chosen==1:
        computer='r'
elif chosen==2:
        computer='p'
elif chosen==3:
        computer='s'

print(computer)

if Player==computer:
        print('DRAW')

elif Player=='r' and computer=='s':
                print('Player Wins!')
elif Player=='r' and computer=='p':
        print('Computer Wins!')

elif Player=='p' and computer=='r':
        print('Player Wins!')
elif Player=='p' and computer=='s':
        print('Computer Wins!')
elif Player=='s' and computer=='p':
        print('Player Wins!')
elif Player=='s' and computer=='r':
        print('Compuiter Wins!')
    

