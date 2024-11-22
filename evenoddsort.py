list1=[1,2,3,4,5]
list2=[6,7,8,9,12]
combined_list=list1+list2
print(combined_list)
even_list=[]
odd_list=[]
for i in combined_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("even_list",even_list)
print("odd_list",odd_list)
even_list.sort()
odd_list.sort()
merged_list=even_list+odd_list
print("merged_list",merged_list)
