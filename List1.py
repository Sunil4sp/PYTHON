#Program to show the various use case for builtin functions in List.
list1 = [[2,4,6,8,10,12],[True,False,True,False]]
list2 = ['sunil','kumar','pal']
list3 = ['hello','world','welcome','to','python']
list4 =list1 + list2 + list3
#for item in range(len(list3)):
#    print("Index:", item, "Value:", list3[item])
#print("Merged List:", list4,"\n List 1: ", list1 * 3, 'sunil' in list1,"\n", list3[0:3])
print(list3[::-1],"\n", list2[::2])
list1.append('sunil')
list1.extend(list3)
print("List1:",list1)