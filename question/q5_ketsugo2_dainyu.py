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
次の内容を結合代入を用いて出力させる
山田 370
鈴木 350
日向 325
田中 330

制限事項：
print関数の使用は1度のみ

"""

# プログラミング言語
result = "テスト結果\n\n"

yamada = "山田"
yamada_s = "370"
suzuki = "鈴木"
suzuki_s = "350"
hyuga = "日向"
hyuga_s = "325"
tanaka = "田中"
tanaka_s = "330"
space = " "
kaigyo = "\n"



print(result)
