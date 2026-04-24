import random

#~ For large range of 1 - 1000.

def rng_lrg():
    num=random.randrange(1,1001)
    count=0
    while True:
        ans=int(input("GUESS THE NUMBER: "))
        count+=1
        if ans >=1001:
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