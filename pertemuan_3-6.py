# Operasi Logika
# - and
# - or
# - not
# - xor '^'

# operasi and (harus keduanya bener)
a = True
b = True
c = a and b
print(f"a ({a}) and b ({b}) = {c}")

# operasi or (minimal ada salah satu yang bener)
a = True
b = True
c = a or b
print(f"a ({a}) or b ({b}) = {c}")

a = True
b = False
c = a or b
print(f"a ({a}) or b ({b}) = {c}")

# operasi not (negasi)
a = True
c = not a
print(f"negasi a({a}) = {c}")

# operasi ^ xor  (gaboleh ada yang sama)
a = True
b = True
c = a ^ b
print(f"a ({a}) xor b ({b}) = {c}")

a = False
b = True
c = a ^ b
print(f"a ({a}) xor b ({b}) = {c}")

a = False
b = False
c = a ^ b
print(f"a ({a}) xor b ({b}) = {c}")