name_list = ["鈴木", "佐藤", "山田"]
position = ["部長", "課長", "係長"]

# name_listに藤田、positionに大統領を追加してみよう！
print("====要素追加===")
name_list.append("藤田")
position.append("大統領")

# 要素番号 1に追加してみよう
name_list.insert(1,"藤田")

print(name_list)
print(position)

print("====要素削除(末尾)===")
# name_listの最後の要素番号を削除しよう！
name_list.pop()
# positionの先頭の要素番号を削除しよう！
position.pop(0)

print(name_list)
print(position)