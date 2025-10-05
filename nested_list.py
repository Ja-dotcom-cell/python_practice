#nested list means inside a list, there is another list which is under the first list.
#we can also access the nested list by writing list_1[index of 1st list][index of 2nd list]
#we can also access the nested list by slicing, which means we put the value of the nested list
#print(list_1[index of nested list][0th index : upto which index we need to show])
list_1 = [1,2,3,4,5,[6,7,8],9]
print(list_1[5][:])