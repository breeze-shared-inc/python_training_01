"""
配列って中々イメージできないですよね？
プログラミングでは配列をよく使います。
変数が一つの箱だとしたら、配列は箪笥のイメージです！

"""

name_list = ["鈴木", "佐藤", "山田"]
position = ["部長", "課長", "係長"]


print("====出力===")
print(name_list[0] + "さんの役職は" + position[0])
print(name_list[1] + "さんの役職は" + position[1])
print(name_list[2] + "さんの役職は" + position[2])

# 再代入
print("====再代入出力===")
name_list[0] = "藤田"
print(name_list[0] + "さんの役職は" + position[0])


print("====要素追加===")
name_list.append("藤田")
position.append("大統領")

print(name_list)
print(position)

print("====要素削除(末尾)===")
name_list.pop()
position.pop()

print(name_list)
print(position)