x = 10
y = 5

# nasted if (cocok untuk pengecekan lebih dari satu ekspresi)
if x == 10:
    if y == 10:
        print("x adalah 10 dan y adalah 10")
    else:
        print("x adalah 10 dan y bukan 10")
else:
    print("x bukan 10")


# elif
if x == 10 and y == 10:
    print("x adalah 10 dan y adalah 10")
elif x == 10 and y != 10:
    print("x adalah 10 dan y bukan 10")
else:
    print("x bukan 10")