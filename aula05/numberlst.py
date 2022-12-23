def positionOfFirstLargest(lst):
    'returns the index of the largest value in the list'
    max = lst[0]
    index = 0
    for i in range(len(lst)):
       if max < lst[i]:
          max = lst[i]
          index = i
    return index

def main():

    lst1 = [0,1,2,3,4,5]
    lst2 = [-1,-2,-3,-4]
    lst3 = [0,1,5,3,4,5]
    lst4 = [0,1,2,3,4,3]

    print(positionOfFirstLargest(lst1))
    print(positionOfFirstLargest(lst2))
    print(positionOfFirstLargest(lst3))
    print(positionOfFirstLargest(lst4))

if __name__ == '__main__':
    main()