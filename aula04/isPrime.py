def isPrime(number):
    mult = 0

    if number == 1:
        return False

    for i in range(2, number):
        if (number % i == 0):
            mult += 1

    if mult  == 0:
        return True
    else:
        return False

def main():
    for i in range(1,100):
        if isPrime(i):
            print(f'{i} is prime')
        else:
            print(f'{i} is not prime')

if __name__ == '__main__':
    main()