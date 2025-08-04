def numeros(*args):
    for n in range(len(args) - 1):
        if args[n] == 0 and args[n + 1] == 0:
            print(True)
            return True
        else:
            print(False)
            return False
    
numeros(1,2,3,4,5,6,7,0,0,9,0)

