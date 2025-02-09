import random
n=random=random.randint(1,100)
a=-1
guesses=1
while(a!=n):
    guesses+=1
    a=int(input("Guess the number:"))
    if(a>n):
        print("lower number pls")
    else:
        print("higher number pls")

print(f"you have guessed the number in the {guesses}attempt")