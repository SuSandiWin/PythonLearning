#global
name="su sandi win";
def callName():
    #local
    global name;#overwrite as global
    name="ag ag";
    print(name);
callName();
print(name);