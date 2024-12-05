# nilai = 1
# batas = 242

input1 = int(input("masukan nilai awal = "))
input2 = int(input("masukan nilai akhir = "))

while input1 <= input2:
    if input1 % 3 == 0:
        print("FIZZ")
    elif input1 % 5 == 0:
        print("BUZZ")
    elif input1 % 5 == 3:
        print("FizzBuzz")
    else:
        print(input1)
    input1 += 1
    

