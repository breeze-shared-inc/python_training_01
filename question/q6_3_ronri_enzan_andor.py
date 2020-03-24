"""

論理演算子一覧
Aが真かつBが真なら真
A and B

Aが真又はBが真なら真
A or B

Aが真なら偽になる
not A


問題：次のように出力せよ

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


"""

print("Aが真かつBが真なら真")
print(1 == 1  1 == 1) # True
print(1 == 2  1 == 1) # False
print(1 == 2  1 == 2) # False


print("Aが真又はBが真なら真")
print(1 == 1  1 == 1) # True
print(1 == 2  1 == 1) # True
print(1 == 2  1 == 2) # False

print("Aが真なら偽になる")
print( 1 == 1) # false
