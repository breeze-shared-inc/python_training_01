"""
<要素の追加・削除>
追加
my_dict["new_key"] = "new_value"

削除
my_dict.pop("new_key")

<問題：下記を出力してみよう！>
value3
{'key': 'value', 'key3': 'value3'}

"""
my_dict = {
    "key":"value",
    "key2":"value2"
}

# dictに要素[key3:value3]を追加してみよう！

print(my_dict["key3"])

# 識別子key2を削除してみよう！


print(my_dict)
