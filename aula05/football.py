def allMatches(teams):
    matches = []
    for team in teams:
        for match in teams:
            if team != match:
                matches.append((team, match))
    return matches

def main():
    test1 = ["A", "B"] 
    test2 = ["A", "B", "C"]
    test3 = ["A", "B", "C", "D"]
    test4 = ["A", "B", "C", "D", "E"]
    test5 = ["FCP", "SCP", "SLB"]

    print(allMatches(test1))
    print(allMatches(test2))
    print(allMatches(test3))
    print(allMatches(test4))
    print(allMatches(test5))

if __name__ == '__main__':
   main()