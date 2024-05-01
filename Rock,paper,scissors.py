import random
L=['rock','paper','scissors']
while True:
  c=int(input('''Enter your choice 
  1) Start the game
  2) Exit \n'''))
  if c == 1:
    print("Start Game...")
    for i in range(3):
      c=input("Choose rock, paper, or scissors:")
      print("User Input: ",c)
      com=random.choice(L)
      print("Computer Input: ",com)
      if c == com:
            print("It's a tie!")
      elif (c == "rock" and com == "scissors") or    (c== "paper" and com == "rock") or (c == "scissors" and com == "paper"):
            print("You win!")
            
      else:
            print("Computer wins!")
  else:
    print("Exit...")
    break