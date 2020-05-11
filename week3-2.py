s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
s1_num = [18, 17, 19.5, 8, 25]
s2_num = [20, 20, 19, 9, 28]
s3_num = [14.5, 16, 13, 7, 23]
a = sum(s1_num)
b = sum(s2_num)
c = sum(s3_num)

names = {'Ahmad':['Ahmad', a], 'Sami':['Sami', b], 'Faris':['Faris', c]}

print(names.get(input("Enter student's name: "), 'Student is not recorded 0'))
