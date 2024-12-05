# Perulangan While

# awal = 1
# batas = 5

# while awal <= batas:
#     #! perulangan 1 awal - awal = 1
#     #! perulangan 2 awal - awal = 2
#     #! perulangan 3 awal - awal = 3
#     #! perulangan 4 awal - awal = 4
#     #! perulangan 5 awal - awal = 5
#     #! perulangan 6 awal - awal = 6
#     #! perulangan 7 awal - awal = 7
#     awal += 1
#     print("hello world")


nilai_awal = 0
batas = 10

while nilai_awal <= batas :
    if nilai_awal % 2 == 0:
        print("bilangan ganjil")
    else:
        print(nilai_awal)
    nilai_awal += 1


# perulangan dengan for

# for i in range(1,5+1,1):
#     print(f"Hello world {i}")

# for i in range(5,0,-1):
#     print(i, end=", ")


# # buat persegi ukuran 4x4 pakai for loop
# for i in range(4):
#     for j in range(4):
#         print("*", end="")
#     print("")


# buat segitiga alas 10
# dry -> dont repeat your self

# n = 10
# for i in range(n):
#     for j in range(i):
#         print("*", end="")
#     print("")

# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end="")
#     print("")
# print("\n")

# for i in range(1,5+1,1):
#     print("*"*i)