from range_small import rng_small
from range_med import rng_med
from range_large import rng_lrg

while True:
    print("SELECT A RANGE ")
    print("For Range 1 - 10 , PRESS: 1 \n For Range 1 - 100 , PRESS: 2 \n For Range 1 - 1000 , PRESS: 3 \n CANCEL: PRESS 4")
    rtyp=int(input("PRESS NOW..."))

    if rtyp == 1:
        rng_small()

    elif rtyp == 2:
        rng_med()

    elif rtyp == 3:
        rng_lrg()

    elif rtyp == 4:
        break

    else:
        print("INVALID!!")
