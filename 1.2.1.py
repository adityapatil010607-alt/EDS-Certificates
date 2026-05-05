# Input number of courses
n = int(input())

# Input marks
marks = list(map(int, input().split()))

# Check fail condition
fail = False
for m in marks:
    if m < 40:
        fail = True
        break

if fail:
    print("Fail")
else:
    # Calculate aggregate percentage
    avg = sum(marks) / n
    print("Aggregate Percentage: {:.2f}".format(avg))

    # Determine grade
    if avg > 75:
        print("Grade: Distinction")
    elif avg >= 60:
        print("Grade: First Division")
    elif avg >= 50:
        print("Grade: Second Division")
    elif avg >= 40:
        print("Grade: Third Division")
