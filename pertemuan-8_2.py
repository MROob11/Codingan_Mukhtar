# Nested List
list_data_siswa = ["mukhtar", 254, 4.0] # 1D
list_kumpulan_siswa = [
    ["Mukhtar", 254, 4.0],
    ["Arthur", 255, 4.0],
    ["Oob", 154, 4.0],
    ["Ucok", 155, 4.0],
] # 2D

# Output
list_luar = list_kumpulan_siswa[0] # ['Mukhtar', 254, 4.0]
list_dalam = list_luar[0] # "Mukhtar"
print(list_kumpulan_siswa[0][0])