for num in range(1,10):
    if num % 2 == 0:
        for star in range(1,6):
            print("*" * star)
    else:
        for star in range(6,1,-1):
            print("*" * star)
