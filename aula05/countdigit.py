def countDigits(word):
    'returns the number of digits contained in the string'
    count = 0
    for char in word:
        if char.isdigit():
            count += 1

    return count

def main():

    #testing function

    count = 0
    while count < 3:
        word = input("Please enter a string with digits: ")
        print(f'the entered phrase has {countDigits(word)} digits!')
        count += 1

if __name__ == "__main__":
    main()