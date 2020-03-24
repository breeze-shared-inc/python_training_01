"""
結合した文字列を変数に代入するには

mo = "文"
ji = "字"

moji = mo + ji

で行うこともできる。

下記の方法でも可能

1.変数に上書きして結合代入
tanaka = "田中"
taro = "太郎"

tanaka = tanaka + taro

print(tanka)
=>田中太郎

2.「結合代入演算子」を使用することも可能

tanaka = "田中"
taro = "太郎"

tanaka += taro
print(tanaka)
=>田中太郎

※1と2は同じ結果が出力されます！



問題：下記を出力させよう
===別のやり方1===
佐藤秀雄
===別のやり方2===
鈴木三郎

"""
print("===別のやり方1===")
sato = "佐藤"
hideo = "秀雄"
sato = sato + hideo #この続きを完成させてください
print(sato)

print("===別のやり方2===")

suzuki = "鈴木"
saburo = "三郎"
suzuki += saburo #結合代入演算子を使用してください。
print(suzuki)