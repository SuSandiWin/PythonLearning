nums=[1,2,3,4,5,6,7]

#Mapping
def mapFunction(num):
    return num*2;
nums_2=list(map(mapFunction,nums)); #return obj so type casting to list
print(nums_2);

#Comprehension
nums_2=[num*2 for num in nums];
print(nums_2);

# lambda function way
nums_2=list(map(lambda num:num*2,nums))
print(nums_2);