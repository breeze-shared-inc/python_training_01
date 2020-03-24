"""
次のLESSONで行う条件分岐（IF文）処理を扱う上で重要です。

論理演算とは
００は真である（正しい）
や
００は偽である（正しくない）

をプログラミングで表現します。
プログラミングでは
真と偽をそれぞれTrueとFalseで
表現します。

例
print(A == A)
=>True

print(1 == 2)
=>False

次のLESSONの条件分岐は

もし００が真なら〜
と言う処理が行われます。
まずは論理演算で扱う記号を活用できるようにしましょう！


論理演算子一覧
AとBが等しい
==
is

AとBが異なる
!=
is not


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

"""

print("AとBが等しい(数字)")
print(1 == 1) # True 記号で
print(1 == 2) # False 記号で
print(1 is 1) # True 文字で
print(1 is 2) # False 文字で

print("AとBが等しい(文字列)")
print("山田" == "山田") # True 記号で
print("山田" == "田中") # False 記号で
print("山田" is "山田") # True 文字で
print("山田" is "田中") # False 文字で

print("AとBが異なる")
print(1 != 1) # False 記号で
print(1 != 2) # True 記号で
print(1 is not 1) #  False 文字で
print(1 is not 2) # True 文字で