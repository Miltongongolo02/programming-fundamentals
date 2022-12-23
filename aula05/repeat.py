def repeatNumber(number):
    'returns a list containing all numbers up to n, repeated by their number of times'
    lst = []
    for i in range(number+1):
        for j in range(i):
            lst.append(i)
    return lst

def main():
    # testing function
    count = 0
    while count < 3:
        number = int(input("Enter a number: "))
        print(repeatNumber(number))
        count += 1

if __name__ == "__main__":
    main()