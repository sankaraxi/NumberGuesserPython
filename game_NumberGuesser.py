import random #importing built-in 'random' module

'''r = random.randrange(-1,10) #generates random numbers from -1 to 9 (10-1)
print(r)
ra= random.randint(-5, 10) #generates random numbers from -5 to 10 (includes 10) also randint requires initial argument i.e. -5
print(ra) '''

range_you_prescribe = input("Enter a number: ")

if range_you_prescribe.isdigit(): #checking whether the input is digits
    range_you_prescribe = int(range_you_prescribe) #converting it into an integer

    if range_you_prescribe <= 0:
        print("Please enter a number greater than 0 next time.")
        quit()
else: 
    print("Please enter a number next time.")
    quit()

random_number = random.randint(0,range_you_prescribe)

no_of_guesses = 0

while True:
    no_of_guesses += 1
    user_guess = input("Make a guess and enter a number: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time.")
        continue
    
    if user_guess == random_number:
        print("Your guess for the random number is correct!")
        break
    elif user_guess > random_number:
            print("You were above the number. Please Try Again!")
    else:
            print("You were below the number. Please Try Again!")
          

print("You got it in",no_of_guesses,"guesses!")




