import os

def compare2(a,b):
    answer = 0
    while answer < 1 or answer >3:
        os.system('cls')
        print("[1] ",a)
        print("[2] ",b)
        print("\n[3] Draw")
        print("\nYour choice : ")
        try:
            answer = int(input())
        except:
            pass
        os.system('cls')
    
    if answer == 1:
        return 0
    elif answer == 2:
        return 1
    else:
        return 0.5