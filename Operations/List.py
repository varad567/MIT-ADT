lst = [1, 2, 3, 4, 5]
print(lst)

print(lst[2])

lst.append(6)
print("List after adding 6:", lst)

lst.remove(3)
print("List after removing 3:", lst)

lst.insert(2, 10)
print("List after inserting 10 at index 2:", lst)

lst.pop()
print("List after popping last element:", lst)

lst.sort()
print("List after sorting in ascending order:", lst)

lst.sort(reverse=True)
print("List after sorting in descending order:", lst)

lst.reverse()
print("List after reversing elements:", lst)