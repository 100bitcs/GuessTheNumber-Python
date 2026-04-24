import random

#~ For small range of 1 - 10.

def rng_small():
    num=random.randrange(1,11)
    count=0
    while True:
        ans=int(input("GUESS THE NUMBER: "))
        count+=1
        if ans >=11:
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