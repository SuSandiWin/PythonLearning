# with open('./about.txt','w') as file:
#     file.write('I am SSW');

# #other work
# with open('./about.txt','a') as file:  #a=among(not to be overwrite file)
#     file.write('\n Welcome from my channel');

list=['Hello World', '\nSuSandiWin'];
with open('./about.txt','w') as file:
    file.writelines(list);
