def removeadjacentDuplicates(word):
    'returns a string with no duplicated adjacent'
    count = 0
    result = word[0]
    for i in word[1:]:
        if i != word[count]:
            result += i
        count += 1
    
    return result

def main():
    count = 0
    while count < 3:
        word = input("Please enter a word: ")
        print(removeadjacentDuplicates(word))
        count += 1

if __name__ == "__main__":
    main()