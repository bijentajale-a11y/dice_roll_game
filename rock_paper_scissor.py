import random

choices=('r','p','s')
emojis={
    'r': '🪨',
    'p': '📃',
    's': '✂️'
}

while True:
    your_choice=input("Enter your choice Rock,Paper or Scissors(r/p/s): ").lower()
    if your_choice not in choices:
        print("Invalid choice!")
        continue

    computer_choice=random.choice(choices)
    print(f"You chose {emojis[your_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")
    
    if(your_choice == computer_choice):
        print("Draw!")
    elif((your_choice == 'r' and computer_choice == 's') or
    (your_choice == 's' and computer_choice =='p') or
    (your_choice == 'p' and computer_choice == 'r')):
        print("You win!")
    else:
        print("You lose!")

    keep_playing=input("Keep playing (y/n)?: ").lower()
    if keep_playing == 'n':
        print("Thanks for playing!")
        break
    
        

