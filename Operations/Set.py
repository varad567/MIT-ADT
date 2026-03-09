s = {1, 2, 3, 4, 5}
print(s)

print("Accessing set elements:")
for element in s:
    print(element)

s.add(6)
print("Set after adding 6:", s)

s.remove(3)
print("Set after removing 3:", s)

s.update([7, 8, 9])
print("Set after adding multiple elements 7,8,9:", s)

s2 = {10, 11, 12}
set_union = s.union(s2)
print("Union of set and set2:", set_union)

s3 = {5, 6, 7, 10}
set_intersection = s.intersection(s3)
print("Intersection of set and set3:", set_intersection)

set_difference = s.difference(s3)
print("Difference of set and set3:", set_difference)