# operator dictionary

data_dict = {
    "ucok":"ucok siucok",
    "oob":"oob sioob",
    "arthur":"arthur siarthur"
}

# panjang dictionary
lendict = len(data_dict)
print(f"panjang dictionary : {lendict}")

# mengecek key exist atau tidak 
key = "ucok"
checkkey = key in data_dict
print(f"apakah {key} ada di data_dict: {checkkey}")

# mengakses value (read) dengan get
print(data_dict["ucok"])
print(data_dict.get("oob"))
print(data_dict.get("SHY","key tidak di temukan")) # key tidak di temukan

# mengupdate data
data_dict["ucok"] = "ucok si ganteng"
print(data_dict)
data_dict["oob"] = "oob si ganteng"
print(data_dict)

data_dict.update({"ucok":"ucok siucok"})
print(data_dict)
data_dict.update({"james":"james si kece"}) # kalau nggak ada di tambah aja 
print(data_dict)

# mendelate data pada dictionary
del data_dict["james"]
print(data_dict)