file=open('./test.txt');

# for line in file:
#     print(line);

# file.seek(0);  #to move cursor to first place
# linelist= file.readlines();
# print(linelist);

# file.seek(50);
# lines=file.read(100);
# print(lines);
# file.close()

with open('./test.txt') as file:
    for line in file:
        print(line);
print('other work')