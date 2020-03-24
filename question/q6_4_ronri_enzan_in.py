"""

論理演算子一覧
AがBに含まれる
A in B

AがBに含まれる(配列)
A in ["A","B","C"]


AがBに含まれるない
A not in B



問題：次のように出力せよ
AがBに含まれる
True
False
AがBに含まれる(配列)
True
False
AがBに含まれるない
False
True


"""


print("AがBに含まれる")
print("田"  "田中") # True
print("山"  "田中") # False

print("AがBに含まれる(配列)")
print("田中"  ["田中", "山田", "佐藤"]) # True
print("福田"  ["田中", "山田", "佐藤"]) # False

print("AがBに含まれるない")
print("田"  "田中") # False
print("山"  "田中") # True

