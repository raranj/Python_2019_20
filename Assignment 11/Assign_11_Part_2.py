p = 1

for i in range(1,8):
    for j in range(p):
        print("*",end = "")
    print("")
    p = 2 * p

p = 32
for h in range(1,7):
    for k in range(p):
        print("*", end = "")
    print("")
    p = p // 2
