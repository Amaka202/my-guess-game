secret_number = 10
guess_limit = 3
guess_count = 0

while guess_count < guess_limit:
    guess_count += 1
    guess = int(input("Guess my secret number: "))
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, You Failed!")
