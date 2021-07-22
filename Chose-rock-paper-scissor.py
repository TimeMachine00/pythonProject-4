print("created by hussainatphysics@gmail.com(hussainsha syed)")
print("welcome to the game")




rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
choice = int(input("what would you like to choose? 0 for rock, 1, paper, 2 for scissors\n"))
a =[rock, paper, scissors]

b= random.randint(0,len(a)-1)
print(b)
c=a[b]

# print(c)

if b==choice:
  print(c)
  print("you win the game")
else:
  print(c)
  print("you lost the game, computer wins")
print()

but1= print(input("press enter for bye..........."))
# l = random.choice(a)
# print(l)
#
# if a.index(l)==choice:
#   print('you won')
# else:
#   print('you lost')