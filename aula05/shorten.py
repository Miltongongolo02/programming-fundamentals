def shorten(word):
    abbreviation = ""
    for i in  word:
        if i.isupper():
            abbreviation += i

    return abbreviation

def main():
    count = 0
    while count < 3:
        word = input("Enter a word: ")
        print(shorten(word))
        count += 1

if __name__ == "__main__":
    main()