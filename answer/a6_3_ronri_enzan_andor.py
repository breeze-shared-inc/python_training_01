print("Aが真かつBが真なら真")
print(1 == 1 and 1 == 1) # True
print(1 == 2 and 1 == 1) # False
print(1 == 2 and 1 == 2) # False


print("Aが真又はBが真なら真")
print(1 == 1 or 1 == 1) # True
print(1 == 2 or 1 == 1) # True
print(1 == 2 or 1 == 2) # False

print("Aが真なら偽になる")
print(not 1 == 1) # false
