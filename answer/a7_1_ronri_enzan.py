"""
Excel関数で学んだ論理演算のPython版です！

論理演算子一覧
AとBが等しい
==
is

AとBが異なる
!=
is not

AがBよりも大きい
>

AがB以上
>=

AがBよりも小さい
<

AがB以下
<=

Aが真かつBが真なら真
A and B

Aが真又はBが真なら真
A or B

Aが真なら偽になる
not A

AがBに含まれる
A in B

AがBに含まれる(配列)
A in ["A","B","C"]


AがBに含まれるない
A not in B



問題：次のように出力せよ
AとBが等しい(数字)
True
False
True
False
AとBが等しい(文字列)
True
False
True
False
AとBが異なる
False
True
False
True
AがBよりも大きい
True
False
AがB以上
True
True
AがBよりも小さい
False
False
AがB以下
False
True
Aが真かつBが真なら真
True
False
False
Aが真又はBが真なら真
True
True
False
Aが真なら偽になる
False
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

print("AとBが等しい(数字)")
print(1 == 1)
print(1 == 2)
print(1 is 1)
print(1 is 2)

print("AとBが等しい(文字列)")
print("山田" == "山田")
print("山田" == "田中")
print("山田" is "山田")
print("山田" is "田中")

print("AとBが異なる")
print(1 != 1)
print(1 != 2)
print(1 is not 1)
print(1 is not 2)

print("AがBよりも大きい")
print(2 > 1)
print(1 > 1)

print("AがB以上")
print(2 >= 1)
print(1 >= 1)

print("AがBよりも小さい")
print(2 < 1)
print(1 < 1)

print("AがB以下")
print(2 <= 1)
print(1 <= 1)

print("Aが真かつBが真なら真")
print(1 == 1 and 1 == 1)
print(1 == 2 and 1 == 1)
print(1 == 2 and 1 == 2)


print("Aが真又はBが真なら真")
print(1 == 1 or 1 == 1)
print(1 == 2 or 1 == 1)
print(1 == 2 or 1 == 2)

print("Aが真なら偽になる")
print(not 1 == 1)

print("AがBに含まれる")
print("田" in "田中")
print("山" in "田中")

print("AがBに含まれる(配列)")
print("田中" in ["田中", "山田", "佐藤"])
print("福田" in ["田中", "山田", "佐藤"])

print("AがBに含まれるない")
print("田" not in "田中")
print("山" not in "田中")

