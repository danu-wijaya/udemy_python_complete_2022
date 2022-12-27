numbers = [0, 1, 2, 3, 4]
doubled_numbers = []

# Doubled number use for loop
# for number in numbers:
#     doubled_numbers.append(number * 2)
# print(doubled_numbers)

# Doubled number use list compherention
doubled_numbers = [number * 2 for number in numbers]
print("Doubled number using list compeherention =", doubled_numbers)

# ====================================================================
friend_ages = [22, 31, 35, 37]
age_strings = [f"my friend is {age} years old." for age in friend_ages]
print(age_strings)

# ====================================================================
names = ["Rolf", "Bob", "Jen"]
lower = [name.lower() for name in names]
print(lower)

# ====================================================================
friend = input("Enter your friend name : ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friend_lower = [friend.lower() for friend in friends]

if friend.lower() in friend_lower:
    print(f"{friend.title()} is one of your friend.")