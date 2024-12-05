# ---LIST---

# Kumpulan data numbers
data_angka = [1,5,2,3]
print(data_angka)

# Kumpulan data string
data_string = ["ucup", "ucok", "oob"]
print(data_string)

# Kumpulan data boolean 
data_boolean = [True, False, True, False]
print(data_boolean)

# kumpulan campuran
data_campuran = [1,"ala ala",2,"ayam",True,"ucok",False,"bambang"]
print(data_campuran)

# cara alternatif membuat list
data_range = range(0,10,2) #range(start,stop,stop)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
list_pake_for_if = [i**2 for i in range(0,10)if i !=5]
print(list_pake_for_if)

# membuat list dengan for loop, list comprehension
print(list_pake_for_if)

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10)if i%2 ==0]
print(list_pake_for_if)

# membuat list pake for pake if
list_pake_for_if = [i**2 for i in range(0,10)if i%2 !=0]
print(list_pake_for_if)