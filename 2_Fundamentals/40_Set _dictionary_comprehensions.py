friends = ["Rolf", "ruth", "charlie", "Jen"]
guest = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = {n.lower() for n in friends}
guest_lower = {n.lower() for n in guest}

present_friends = friends_lower.intersection(guest_lower)
present_friends = {name.title() for name in present_friends}

print(present_friends)

# =================================================================
old_friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timer = {
    old_friends[i]: time_since_seen[i] 
    for i in range(len(old_friends))
}

print(long_timer)