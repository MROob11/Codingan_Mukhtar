umur = int(input("Input umur: "))
if umur < 13:
    print("aku masih anak anak belum cukup umur untuk voting")
elif umur > 13 and umur < 16:
    print("aku seudah remaja, tetapi belum cukup umur untuk voting")
elif umur > 17 and umur < 64:
    print("aku seudah dewasa dan bisa melakukan voting")
elif umur > 65:
    print("aku tua dan masih bisa melakukan voting")
