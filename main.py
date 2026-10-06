import random
n = random.randint(1, 100)
user_num =int(input("Enter Your first guess:"))
guesses = 0
while(n!=user_num):
    guesses+=1
    if(n>user_num):
        print(f"OPPS! You guessed small then the number, Guess big than {user_num}")
        user_num =int(input("Another Guess:"))
    else:
        print(f"OPPS! You guessed big then the number, Guess small than {user_num}")
        user_num =int(input("Another Guess:"))
else:
    print(f"CONGRATULATION!!!! You guessed it right in {guesses + 1} attempts")