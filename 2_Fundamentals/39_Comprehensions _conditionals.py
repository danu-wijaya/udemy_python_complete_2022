ages = [22, 35, 27, 21, 20]
odds = [age for age in ages if age % 2 == 1]
print(odds)

# =======================================================
friends = ["Rolf", "ruth", "charlie", "Jen"]
guest = ["jose", "Bob", "Rolf", "Charlie", "michael"]

present_friends = {
    name.title()
    for name in guest
    if name.lower() in [f.lower() for f in friends]
}

print(present_friends)