# This program generates 20 terms of a sequence by a recurrence relation.
Un = 100
count = 0                    # Un = each term of the sequence. Initially = U0
while Un > 0:
    print(Un)
    count += 1
    Un = 1.01*Un - 1.01     # Set Un to the next term of the sequence
print(f"O programa mostrou {count} termos")
