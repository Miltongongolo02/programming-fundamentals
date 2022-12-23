def inputFloat():
    lst = []
    while True:
        number = input('Enter a number: ')
        if number is '': break
        if number.isdigit():
            float(number)
            lst.append(number)
        else:
            print('That is not a number')

    return lst

def countLower(lst, value):
    count = 0
    for item in lst:
        if item < value:
            count += 1
    
    return count

def minMax(lst):
    min = lst[0]
    max = lst[0]
    for item in lst:
        if item < min:
            min = item
        if item > max:
            max = item
    
    return (min, max)

def main():
    lst = inputFloat()
    num = minMax(lst)
    average = (num[0]+num[1])/2
    counter = countLower(lst, average)
    print(f'Elements of list: {lst}')
    print(f"Min: {num[0]}")
    print(f"Max: {num[1]}")
    print(f"Values below average ({average}): {counter}")

if __name__ == '__main__':
    main()