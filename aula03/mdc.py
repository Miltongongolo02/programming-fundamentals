def mdc(x,y):
    if x > y: 
        x = y
        y = x
    resto = x % y
    if resto != 0: 
        return mdc(y, resto)
    return y

def main():
    '''
    value for testing           expected
    20,24                           4
    8,12                            4
    12,15                           3
    '''
    count = 0
    while count < 3:
        x = int(input("Digite o valor: "))
        y = int(input("Digite o valor: "))
        print(mdc(x,y))
        count = count + 1

if __name__ == '__main__':
    main()