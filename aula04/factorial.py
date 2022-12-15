def factorial(n):
    value = 1
    if n == 0 or n == 1:
        return value
    
    for i in range(1,n+1):
        value *= i

    return value

def main():
    #testing function
    count = 0
    while count < 5:
        n = int(input('digit value: '))
        print(factorial(n))
        count += 1

if __name__ == '__main__':
    main()