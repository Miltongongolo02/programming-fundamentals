def fibonacci(number):
    n0 , n1 = 0, 1
    count = 0

    if number <= 0:
        print("Enter positive numbers! ")
    elif(number == 1):
        print(f" The Fibonacci sequence of {number} is: ")
        print(n1)
    else:
        print(f" The Fibonacci sequence of {number} is: ")
        while count < number:
            print(n0)
            ntermos = n0 + n1
            n0 = n1 
            n1 = ntermos
            count += 1

def main():
    #testing function
    count = 0
    while count < 3:
        number = int(input("Enter positive numbers: "))
        fibonacci(number)
        count += 1

if __name__ == "__main__":
    main()