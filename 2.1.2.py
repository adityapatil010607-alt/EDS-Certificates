# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}

# Display original dictionary

print("Original Dictionary:", student)
key_insert = int(input())
value_insert = input()
student[key_insert] = value_insert
print("After Insertion:", student)
key_update = int(input())
value_update = input()
if key_update in student:
    student.update({key_update: value_update})
print("After Update:", student)
key_delete = int(input())
if key_delete in student:
    student.pop(key_delete)
print("After Deletion:", student)

print("Traversing Dictionary:")
for key, value in student.items():
    print(key, ":", value)
