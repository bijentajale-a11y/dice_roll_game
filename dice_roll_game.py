import random

total_score = 0
roll_count = 0
target = 8

while True:
    choice=input("Roll the dice(y/n): ").lower()
    if choice == 'y':
        roll_count += 1 #roll counter

        die1=random.randint(1,6)
        die2=random.randint(1,6)

        total = die1 + die2

        total_score += total
        
        print(f"\nRoll {roll_count}:({die1},{die2})")
        print(f"Current roll total:{total}")
        
        if total == target:
            print("You win!")
        else:
            print("You lose!")
        print(f"Total Score so far: {total_score}\n")
    

    elif choice == 'n':
        print("\nThanks for playing!")
        print(f"Total rolls: {roll_count}")
        print(f"Final score: {total_score}")
        break

    else:
        print("Enter a valid data.")

