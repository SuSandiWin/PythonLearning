person={
    'name':'SuSandiWin',
    'age':23
}
# print(person);
person['hair color']='black';
# print(person);
# print('name' in person);
if 'name' in person:
    print("name exits");

#change dic keys and value to list
person_keys=list(person.keys());
print(person_keys);
person_values=list(person.values());
print(person_values);