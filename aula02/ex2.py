def max2(x,y):
    'retorna o maior numero entre os argumentos.'
    if x > y:
        return x
    return y

def max3(x,y,z):
    'retorna o maior numero entre os argument.'
    if max2(x,y) > z:
        return max2(x,y)
    return z

def main():
    'inicia a função'
    while True:
        x = input("introduza um numero inteiro: ")
        y = input("introduza um valor inteiro: ")
        if x == '' or y == '': break
        int(x)
        int(y)

        print(max2(x,y))
    

if __name__ == '__main__':
    main()