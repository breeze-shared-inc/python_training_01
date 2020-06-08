
print("AがBに含まれる")
print("田" in "田中") # True
print("山" in "田中") # False

print("AがBに含まれる(配列)")
print("田中" in ["田中", "山田", "佐藤"]) # True
print("福田" in ["田中", "山田", "佐藤"]) # False

print("AがBに含まれるない")
print("田" not in "田中") # False
print("山" not in "田中") # True

