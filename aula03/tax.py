def tax(r):
    if r <= 1000:
        result = 0.1 * r
    elif r <= 2000:
        result = (0.2 * r) - 100
    else:
        result = (0.3 * r) - 300
    
    return result

def main():
    #testing function
    count = 0
    while count < 3:
        number = int(input('digit number: '))
        taxa = tax(number)
        print(taxa)
        count += 1

if __name__ == '__main__':
    main()