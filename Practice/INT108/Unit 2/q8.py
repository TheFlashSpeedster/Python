"""
Q8. Number Guessing Game using random (High) 
Generate random number 1–10. User has 3 chances to guess.
"""
import random

secret = random.randint(1,10)
chances = 3

while chances>0:
  guess = int(input("Guess the number: "))

  if guess==secret:
    print("You Won!")
    break
  elif guess<secret:
    print("Too Low")
  else:
    print("Too High")
  
  chances -= 1

if chances==0 and guess!= secret:
  print("Game Over!")
  print("Number was", secret)