# list, Tuple & Set, Dictionary

# List = Sebuah struktur data yang di gunkanan untuk menyimpan value

#? List / Array [Index ->, Length]
list_genap = [2, 4, 6, 8, 10]

panjang_list_genap = len(list_genap)
index_3 = list_genap[3] #! mengambil nilai index ke-
index_terakhir = list_genap[-1] #! (-) digunakan untuk mengambil index terakhir

print(f"Tipe Data : {type(list_genap)}")
print(f"Panjang List : {panjang_list_genap}")
print(f"Index ke-3 : {index_3}")
print(f"Index terakhir : {index_terakhir}")

# cara 1 {nilai}
for nilai in list_genap :
    print(f"ini nilai : {nilai}")

# cara 2 {index}
for i in range(0, len(list_genap)):
    # print(i) #! i = 0,1,2,3,4
    print(f"ini nilai : {list_genap[i]}")

# cara 3 {index & nilai}
for index, value in  enumerate(list_genap):
    print(f"ini list genap index ke-{index}: {value}")