# Difference
print("============== DIFFERENCE ==============")
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friend = friends.difference(abroad) # {"Rolf"}
local_friend_ = abroad.difference(friends) # {} or set()

print(f"friends: {friends}")
print(f"abroad: {abroad}")
print(f"local_friend: {local_friend}")
print(f"local_friend_: {local_friend_}")
print("========================================\n")

# Union
print("============== UNION ==============")
abroad = {"Bob", "Anne"}
local = {"Rolf"}
friends = local.union(abroad)
print(f"abroad: {abroad}")
print(f"local: {local}")
print(f"friends: {friends}")
print("===================================\n")

# Union
print("============== INTERSECTION ==============")
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
common = art.intersection(science)
print(f"art: {art}")
print(f"science: {science}")
print(f"common: {common}")
print("==========================================\n")