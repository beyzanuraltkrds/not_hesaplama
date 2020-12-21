def asal_mi(x):
    i = 2
    if (i == 1):
        return False
    elif (i == 2):
        return True
    else:
        while(i < x):
            if (x % i):
                return False
            i += 1
    return True

