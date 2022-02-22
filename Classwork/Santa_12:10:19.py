
masses = [1067 , 567 , 444 , 234 , 6780]
length = len(masses)
fuel = 0

for i in range(length):
    mod = (masses[i] * 3) - 2
    fuel = fuel + mod

print("The total amount of fuel is:", fuel)
