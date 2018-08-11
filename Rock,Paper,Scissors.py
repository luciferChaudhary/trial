from random import randint
def choices():
    print('Enter Your Choice:')
    print('1 - Rock')
    print('2 - Paper')
    print('3 - Scissor')
def cpuChoice(cpu):
    if cpu == 1:
        chosen = 'Rock'
    elif cpu == 2:
        chosen = 'Paper'
    else:
        chosen = 'Scissor'
    return chosen
def gameFun(user):
    cpu = randint(1,3)
    if user == cpu:
        print('Try Again, Both selected',cpuChoice(cpu))
        choices()
        user = int(input())
        gameFun(user)
    elif (user == 1 and cpu == 2) or (user == 2 and cpu == 3) or (user == 3 and cpu ==1):
        print('CPU Choose',cpuChoice(cpu))
        return print('CPU wins!!!')
    else:
        print('CPU Choose',cpuChoice(cpu))
        return print('User wins!!!')
print('Rock,Paper and Scissor Game...')
choices()
user = int(input())
gameFun(user)