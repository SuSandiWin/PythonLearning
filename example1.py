person={};
while True:
    name=input("Enter name:");
    age=input("Enter age");
    person[name]=age;
    ask=input("another?y/n");
    if ask=='y':
        continue;
    elif ask=='n':
        break;
    else:
        print("Pls type y or n");
        continue;
# for (name,age) in person.items():
#     print(f'{name} is {age} year old');
# print(person);

ages=list(person.values());
for age in set(ages):
    count=ages.count(age);
    print(f'{age} year olds :{count}')
    print(set(ages))
print(person);
