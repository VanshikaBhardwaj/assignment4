tuple1 = 1,2,3,4

#1 Finding length of a tuple
t_length=len(tuple1)
print("length of array is",t_length)

#2 Finding minimum and mmaximum
print("Minimum element in tuple1 is",min(tuple1))
print("Minimum element in tuple1 is",max(tuple1))

#3 Product of all elements
pro=1
tuple2=23,43,12,2,3
for i in range(len(tuple1)):
    pro=pro*tuple1[0]
print("product of terms in tuple 2 ",pro)

#4 Creating sets
set1 = {10,20,30,40,50}
set2 = {'a','b','c','d','e'}
print("Sets created! \nset 1",set1,"\nset 2",set2)

#5 Creating dictionaries
diction1 = {"Name":"Vanshika","Roll No":37,"College":"GEU","Course":"Python and Machine learning"}

#6 sortting a dictionary
for key in sorted(diction1.keys()):
    print ("%s: %s" % (key, diction1[key]))
