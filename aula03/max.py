def max2(x,y):
    if x > y: 
        return x
    else: 
        return y

def max3(x,y,z):
    if max2(x,y) > z:
        return max2(x,y)
    else:
        return z

def main():
    #testing function
    count = 0
    while count < 2:
        print(max2(x = int(input('digit number: ')),y = int(input('digit number: '))))
        print(max3(x = int(input('digit number: ')),y = int(input('digit number: ')),z = int(input('digit number: '))))
        count += 1

if __name__ == '__main__':
    main()