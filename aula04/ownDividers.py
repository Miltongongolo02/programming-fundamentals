def ownDividers(number):
    dividers = []
    for i in range(1,number):
        if number % i == 0:
            dividers.append(i)

    return dividers

def numberCategory(number):
    sum = 0
    for i in ownDividers(number):
        sum += i
    if sum < number:
        category = 'Deficient Number!'
    elif sum > number:
        category = 'Abundant Number!'
    else:
        category = 'perfect Number!'

    return category

def main():
    #testing function
    count = 0
    while count < 3:
        number = int(input('digit integer number (positive): '))
        divisor = ownDividers(number)
        category = numberCategory(number)
        print(f'The number {number} has the following proper divisors: {divisor}. \n {number} is a {category}')
        count += 1

if __name__ == '__main__':
    main()