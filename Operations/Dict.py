d = {'name': 'Riya', 'age': 18, 'city': 'Pune'}
print(d)

print("Accessing name from dictionary:", d['name'])

d['country'] = 'India'
print("Dictionary after adding country:", d)

d.pop('age')
print("Dictionary after removing age:", d)

d['age'] = 19
print("Dictionary after updating age:", d)

keys = d.keys()
print("Keys of dictionary:", keys)

d.pop('city')
print("Dictionary after removing city:", d)