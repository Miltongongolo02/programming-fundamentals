from random import randrange

def hilo(x):
    count = 0
    while True:
        y = int(input('digit number: '))
        count += 1
        if x == y:
            print(f'got it right with {count} tries')
            break
        else:
            if y < x:
                print('the number is low')
            else:
                print('the number is high')
        

def main():
    #testing function
    count = 0
    while count < 3:
        x = randrange(1, 100)
        print(x)
        hilo(x)
        count += 1

if __name__ == '__main__':
    main()

            
    

