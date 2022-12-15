def leibnizPi4(n):
    'Return the sum of N terms of a sequence ((-1)**i)/(2*i+1).'
    assert n >= 0
    sum = 0
    for i in range(n):
        numerator = (-1) ** i
        denominator = 2 * i + 1
        sum += (numerator / denominator) * 4

    return sum

def main():
    #testing function
    count = 0
    while count < 3:
        n = int(input('enter the number of terms you want to sum: '))
        print(f"The sum of the first {n} first terms of this series is equal to {leibnizPi4(n)}")
        count += 1

if __name__ == '__main__':
    main()
