# function di python
    #! function biasa
    #! function dengan input
    #! function dengan return\

# #? function biasa
# def print_hello():
#     print("Hello World")

# print_hello()

# def nama():
#     print("mukhtar")
#     print(242)
# nama()

# # break, countinue, pass
# def ga_ngapain():
#     pass

# # function dengan input
# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     print(f"luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")

# luas_persegi_panjang(7, 4)


# def perkenalan(nama :str, npm: int, asal: str): # nama, npm, asal
#     # print perkenalan
#     print("NPM", npm)
#     print("NAMA", nama)
#     print("ASAL", asal)
    
# perkenalan(nama= "mukhtar", npm= 242, asal= "palembang")



# def luas_persegi_panjang(panjang=6, lebar=3):
#     luas = panjang * lebar
#     print(f"luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")

# panjang = int(input("Inputkan panjang : "))
# lebar= int(input("Inputkan lebar : "))
# luas_persegi_panjang(panjang=panjang, lebar=lebar)


# # function dengan return
# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     return luas

# luas = luas_persegi_panjang(4,2)
# luas_baru = luas * 10
# print(luas)

# def hello():
#     return "hello"

# nilai = hello()
# print(hello()) #! == print("hello")

def luas_segitiga(alas, tinggi ):
    # luas = (alas * tinggi) /2 
    return (alas * tinggi) /2

luas_segitiga_baru = luas_segitiga(2,2) * 2
print(luas_segitiga_baru)
