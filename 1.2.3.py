# Input: number of rows
n = int(input())

# Loop for rows
for i in range(1, n + 1):
    # Print stars for each row
    for j in range(i):
        print("*", end=" ")
    print()
