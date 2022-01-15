import random

choice= ("rock","paper","scissor")
comp= random.randint(0,2)
comp= choice[comp]
mine= input("Choose Rock,paper or scissor: ")

def rps(comp,mine):
    if(comp==mine):
        return None
    if(comp=="rock" and mine== "paper" ):
        return True
    if(comp=="scissor" and mine== "rock" ):
        return True
    if(comp=="paper" and mine== "scissor" ):
        return True
    else:
        return False

win= rps(comp,mine)
print(f"You chose {mine} and computer chose {comp}")
if win is None:
    print("It is a draw")
if win is True:
    print("You Won")
else:
    print("You Lost")    