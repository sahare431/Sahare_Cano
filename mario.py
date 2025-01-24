while True:
        h = int(input("How tall should the pyramid be?"))
        if 1 <= h <= 8: 
            break
for i in range (1, h+1):
    print (" "* (h - i) + "#" * i + " " + "#" * i)
