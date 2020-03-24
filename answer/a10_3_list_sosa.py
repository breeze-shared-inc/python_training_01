"""
＜配列の追加、削除の関数＞

末尾に追加 配列.append()
指定に追加 配列.insert(要素番号, 値)

末尾を削除 配列.pop()
指定を削除 配列.pop(要素番号)


＜問題：配列を扱って以下を出力せよ＞
====要素追加===
['鈴木', '藤田', '佐藤', '山田', '藤田']
['部長', '課長', '係長', '大統領']
====要素削除(末尾)===
['鈴木', '藤田', '佐藤', '山田']
['課長', '係長', '大統領']


"""

name_list = ["鈴木", "佐藤", "山田"]
position = ["部長", "課長", "係長"]

print("====要素追加===")
name_list.append("藤田")
position.append("大統領")

# 要素番号 1に追加
name_list.insert(1,"藤田")

print(name_list)
print(position)

print("====要素削除(末尾)===")
name_list.pop()
position.pop(0)

print(name_list)
print(position)