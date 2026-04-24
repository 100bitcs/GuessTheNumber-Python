import random

#~ For medium range of 1 - 100.

def rng_med():
    num=random.randrange(1,101)
    count=0
    while True:
        ans=int(input("GUESS THE NUMBER: "))
        count+=1
        if ans >=101:
            print("KNOW YOUR PLACE!!")
        else:
            if ans > num:
                print("LOOK BACK!!")
            elif ans<num:
                print("UP THERE!!")
            elif ans ==num:
                print("YOU GOT IT!!")
                break
    print(f"YOU HAVE TAKEN {count} GUESSES.")