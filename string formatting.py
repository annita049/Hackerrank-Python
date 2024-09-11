def print_formatted(number):
        
    width = len(bin(number)[2:])
    for i in range(1,number+1):
        decimal = i
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(str(i).rjust(width)+" "+ octal.rjust(width) + " " + hexa.rjust(width)+ " " + binary.rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


#   17    21    11 10001
#   17    21    11 10001
#16    20    10 10000