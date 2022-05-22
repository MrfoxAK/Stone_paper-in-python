#stone_paper_seasor
import random
print("Hello") 
print("Choose - stone/paper/seasor")
i = 0
while(i<5):
     l1 = ["stone","paper","seasor"]
     n = input("Enter your choice\n")
     if n not in l1:
         print("Invalid")
     else:
         r_n = random.choice(l1)
         print("computer :",r_n)
         if (n == "stone") and (r_n == "stone"):
             print("same")
         elif (n == "stone") and (r_n == "paper"):
             print("computer win")
         elif (n=="stone") and (r_n =="seasor"):
             print("You win")
         elif (n == "paper") and (r_n == "paper"):
             print("same")
         elif (n == "paper") and (r_n == "stone"):
             print("You win")
         elif (n == "paper") and (r_n == "seasor"):
             print("Computer win")
         elif (n == "seasor") and (r_n == "seasor"):
             print("same")
         elif(n== "seasor") and (r_n == "paper"):
             print("You win")
         elif(n == "seasor") and (r_n == "stone"):
             print("Computer win")
                              

     i= i+1
"""
import random
print("1.Stone", end="   ")
print("2.Paper", end="   ")
print("3.Seasor")
number_of_Chance=1
n = int(input("Enter How many time you want to Play : "))
print(f"You have {n} Chance to Beat the computer: ")
while (number_of_Chance<=n):
 while True:
    game = input("Enter Your choice [1/2/3]: ")
    if game in ('1', '2', '3'):
            if game == '1':
                list = ["Stone", "paper", "Seasor"]
                choice = random.choice(list)
                print(choice)
            elif game == '2':
                list = ["Stone", "paper", "Seasor"]
                choice = random.choice(list)
                print(choice)
            elif game == '3':
                list = ["Stone", "paper", "Seasor"]
                choice = random.choice(list)
                print(choice)
            break
    else:
            print("invalid input")
            print(number_of_Chance, "no.of  Chance he took to finish.")
            break
 print(n - number_of_Chance, "no. of Chance left")
 number_of_Chance = number_of_Chance + 1

if (number_of_Chance > n):
    print("Game Over")

import random

while True:
     l1 = ["stone","paper","seasor"]
     n = input("Enter your choice\n")
     if n not in l1:
         print("Invalid")
     else:
         r_n = random.choice(l1)
         print("computer :",r_n)
         if (n == r_n):
             print("same")
         elif ((n == 'stone' and r_n == 'seasor') or (n == 'paper' and r_n == 'stone') or (n == 'seasor' and r_n == 'paper')):
             print("You Win!")
         else:
             print("You Lose!")
 """