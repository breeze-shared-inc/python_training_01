"""
dict型は要素番号で操作していたものが
key(識別子)とvalue(値)形式で操作します。


プログラム上でデータベース操作が頻繁にあり、
データベースから情報を取得する際はkeyとvalue形式になっていたり、
他のアプリケーションと情報をやりとりする際もkeyとvalue形式になっていることが
非常に多いです。

要素番号だけだと、どんなデータなのか判別しづらいデータが
keyで識別子を持たせることで、
開発者がデータを読み取る手出すけを行うことが可能です。

<定義方法>
my_dict = {
    "key":value,
    "key2":value2
}

listが[]囲うのに対し、
dictは{}で囲う。

要素番号で管理せず、keyで管理する

<要素のアクセス>
print( my_dict["key"] )
=>valueが出力

print( my_dict["key2"] )
=>value2が出力

<要素の追加・削除>
my_dict["new_key"] = "new_value"

my_dict.pop("new_key")

<問題：下記を出力してみよう！>
{'key': 'value', 'key2': 'value2'}

"""

# dict型を定義してみよう！
my_dict = {
    "key":"value",
    "key2":"value2"
}

print(my_dict)