if __name__ == '__main__':

    # alphanum ->  aa or AA or aA or 62 or F5gcW
    # not alphanum -> contains signs (@,!,#,$%27aAO)
    # alpha -> aa or AA or aA
    # digit -> 0-9
    # lower -> everything except NOT (A-Z)
    # upper -> everything except (a-z)

    s = input()

    alpha = False
    digit = False
    for ch in s:
        if ch.isdigit():
            digit = True
        if ch.isalpha():
            alpha = True

    if digit or alpha:  # aa or AA or 62 or F5gcW or 4adBs%
        print(True)    # alphanum

        if alpha and digit==False:
            print(True)  # only alpha
            print(False) # no digit

            if s.islower():
                print(True) # only lower
                print(False) # no upper
            elif s.isupper():
                print(False)  # no lower
                print(True) # only upper
                  
            else:  # lower and upper
                print(True)   # lower
                print(True)  # upper

        elif alpha==False  and digit:
            print(False) # no alpha
            print(True) #  only digit
            print(False) # no lower
            print(False) # no upper

        else:  # alpha and digit
            print(True)  # alpha
            print(True) # digit

            if s.islower():
                print(True) # only lower
                print(False) # only upper
            elif s.isupper():
                print(False) # no lower
                print(True) # only upper  
                
            else:  # lower and upper
                print(True)  # lower
                print(True)  # upper
    else:
        print(False) # no alphanum
        print(False) # no alpha
        print(False) # no digit
        print(False) # no upper
        print(False) # no lower