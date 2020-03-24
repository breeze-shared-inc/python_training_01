"""
＜配列のアクセス＞
配列の中の要素を参照する場合、
配列が格納された変数を指定して、
要素番号を指定することで情報を取り出すことができます。

namelist = ["A","B","C"]
print(namelist[0])
=>A


＜問題：配列を扱って以下を出力せよ＞
鈴木部長
佐藤課長
山田係長



"""

name_list = ["鈴木", "佐藤", "山田"]
position = ["部長", "課長", "係長"]


print(name_list[0] + position[0])
print(name_list[1] + position[1])
print(name_list[2] + position[2])
