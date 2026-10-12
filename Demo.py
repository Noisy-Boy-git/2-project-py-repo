import random

field = ["Rock", "Scissors", "Paper"]

esci_r = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

esci_p = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

esci_s = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Welcome to the Rock, paper, scissors game!")

rules =  input("Press enter to start or type help for the rules.\n").lower()

if rules.lower() == "help":
    print("""
*************** RULES ****************
1) You choose and the computer chooses
2) Rock smashes Scissors = Rock win
3) Scissors smashes Paper = Scissors win
4) Paper smashes Rock = Paper win
""")

    comp_choice = random.choice(field).capitalize()
    you = input("Enter your choice (Rock, Scissors, Paper):\n").capitalize()
    if you not in ["Rock", "Scissors", "Paper"]:
        print("inavalid choice.please run the progress again and choose rock, paper, or scissors.")
    if comp_choice == you:
        if comp_choice==field[0]:
            print(f"draw:  \nyou choose\n{esci_p}\n and the computer choose \n{esci_p}")
        elif comp_choice==field[1]:
            print(f"draw:  \nyou choose\n{esci_s}\n and the computer choose \n{esci_s}")
        elif comp_choice==field[2]:
            print(f"draw:  \nyou choose\n{esci_p}\n and the computer choose \n{esci_p}")

    elif you == field[0] and comp_choice == field[1]:
        print(f"Rock win: you choose {esci_r} and the computer choose {esci_s}")

    elif you == field[1] and comp_choice == field[2]:
        print(f"Scissors win: you choose {esci_s} and the computer choose {esci_p}")

    elif you == field[2] and comp_choice == field[0]:
        print(f"Paper win: you choose {esci_p} and the computer choose {esci_r}")

    elif comp_choice == field[0] and you == field[1]:
        print(f"You lose: you choose {esci_s} and the computer choose {esci_r}")

    elif comp_choice == field[1] and you == field[2]:
        print(f"You lose: you choose {esci_p} and the computer choose {esci_s}")

    elif comp_choice == field[2] and you == field[0]:
        print(f"You lose: you choose {esci_r} and the computer choose {esci_p}")

elif rules == "":
    comp_choice = random.choice(field).capitalize()
    you = input("Enter your choice (Rock, Scissors, Paper):\n").capitalize()
    if you not in ["Rock", "Scissors", "Paper"]:
        print("inavalid choice.please run the progress again and choose rock, paper, or scissors.")
    if comp_choice == you:
        if comp_choice==field[0]:
            print(f"draw:  \nyou choose\n{esci_r}\n and the computer choose \n{esci_r}")
        elif comp_choice==field[1]:
            print(f"draw:  \nyou choose\n{esci_s}\n and the computer choose \n{esci_s}")
        elif comp_choice==field[2]:
            print(f"draw:  \nyou choose\n{esci_p}\n and the computer choose \n{esci_p}")
    elif you == field[0] and comp_choice == field[1]:
        print(f"Rock win: you choose {esci_r} and the computer choose {esci_s}")

    elif you == field[1] and comp_choice == field[2]:
        print(f"Scissors win: you choose {esci_s} and the computer choose {esci_p}")

    elif you == field[2] and comp_choice == field[0]:
        print(f"Paper win: you choose {esci_p} and the computer choose {esci_r}")

    elif comp_choice == field[0] and you == field[1]:
        print(f"You lose: you choose {esci_s} and the computer choose {esci_r}")

    elif comp_choice == field[1] and you == field[2]:
        print(f"You lose: you choose {esci_p} and the computer choose {esci_s}")

    elif comp_choice == field[2] and you == field[0]:
        print(f"You lose: you choose {esci_r} and the computer choose {esci_p}")

else:
  print("!!Invalid choice!!")