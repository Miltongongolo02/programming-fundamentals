def countDown(number):
    if number == 0:
        print (number)
        return 0
    if number == 1:
        print (number)
        return 1
    else:
        print (number)
        return countDown(number - 1)

def main():
    #testing function
    count = 0
    while count < 3:
        number = int(input('digit number: '))
        countDown(number)
        count += 1

if __name__ == '__main__':
    main()
