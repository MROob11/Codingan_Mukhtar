# copy dictionary

teman_teman = {
    "ucok":"ucok siucok",
    "oob":"oob sioob",
    "arthur":"arthur siarthur",
    "james":"james sijames",
    "jai":"jai sianjai"
}

friends = teman_teman.copy()

print(f"teman_teman : {teman_teman}\n")
print(f"friends : : {friends}\n")

teman_teman["ucok"] = "ucok sikeren"
print(f"teman_teman : {teman_teman}\n")
print(f"friends : : {friends}\n")

# pop dictionary (berdasarkan key)
dataJames = friends.pop("james")
print(f"data james : {dataJames}\n")
print(f"friends : : {friends}\n")

# pop item dictionary (yang terakhir aja)
dataTerakhir = friends.popitem()
print(f"data terakhir : {dataTerakhir}\n")
print(f"friends : : {friends}\n")