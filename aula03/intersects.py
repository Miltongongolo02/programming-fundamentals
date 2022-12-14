def intersect(x1, y1, x2, y2):
    return not y1 <= x2 or y2 <= x1

def main():
    #testing function
    #argument
    '''
       Arguments        expected
    x1, y1, x2, y2      boolean
    1,  3,  4,  7        False
    1,  4,  4,  7        False
    2,  5,  4,  7        True
    4,  5,  4,  7        True
    '''
    count = 0
    while count < 4:
        x1 = int(input('x1: ')) 
        y1 = int(input('y1: '))
        x2 = int(input('x2: '))
        y2 = int(input('y2: '))
        print(intersect(x1, y1, x2, y2))
        count += 1

if __name__ == '__main__':
    main()