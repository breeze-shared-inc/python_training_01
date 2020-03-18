"""
文字列同士を　＋ 記号を使用することで結合することができる。
Pythonについては結合する際はいずれも文字列型である必要があり、
例えば、int型とsring型を結合する場合は、
int型をstring型にキャスト（変換）する必要がある。

"""

# 文字列同士の結合
company_name = "株式会社武離威頭"
name = "鈴木"
print(company_name + name)

# 型が違う同士の結合
tanaka = "堀田"
age = 17

print(tanaka + "さんは" + str(age) + "さい")



print("===別のやり方===")
sato = "佐藤"
satosan = sato + "さんは" + str(age) + "さい"
print("===別のやり方2===")
print(satosan)
print("===別のやり方3===")
sato += "さんは" + str(age) + "さい"
print(sato)