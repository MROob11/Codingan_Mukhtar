# # manipulasi list
# list_nama = ["mukhtar", "Oob", "Arthur"]
# #? Memasukan/menambahkan nilai ke list
# print(f"List sebelum append {list_nama}")
# #! Append
# print(f"List sebelum append {list_nama}")
# list_nama.append("ucok")
# print(f"List sesudah append {list_nama}")
# print("="*70)

# #! Insert
# print(f"List sebelum insert {list_nama}")
# list_nama.insert(1, "James")
# print(f"List sesudah insert {list_nama}")
# print("="*70)

# #! Extend
# list_nama_2 = ["iril", "mimar", "bejul"]
# print(f"List sebelum extend {list_nama}")
# list_nama.extend(list_nama_2)
# print(f"List sesudah extend {list_nama}")
# print("="*100)

# #! Menghapus nilai dari list
# #! Pop
# print(f"List sebelum pop {list_nama}")
# list_nama.pop()
# print(f"List sesudah pop {list_nama}")
# print("="*100)

# #! Remove {berdasarkan value}
# print(f"List sebelum remove {list_nama}")
# list_nama.remove("ucok")
# print(f"List sesudah remove {list_nama}")
# print("="*100)

# list_angka = [1,5,2,6,8,2,3,3,1,3,3,3,3,3,3,3]
# print(f"penggunaan index : {list_angka.index(2)}")
# print(f"penggunaan count : {list_angka.count(3)}")
# print(f"sebelum menggunakan sort : {list_angka}")
# list_angka.sort()
# print(f"sesudah menggunakan sort : {list_angka}")

# print(f"sebelum menggunakan reverse : {list_angka}")
# list_angka.reverse()
# print(f"sesudah menggunakan reverse : {list_angka}")

#! Slicing
list_angka = [1,5,2,6,8,2,3,3,1,3,3,3,3,3,3,3]
# list_baru = lis angka yang sampai index ke 10
awal = 5
akhir = 9
list_baru =  list_angka[awal:akhir]
print(list_baru)