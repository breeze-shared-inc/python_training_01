"""
<要素の追加・削除>
my_dict["new_key"] = "new_value"

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
my_dict["key3"] = "value3"
print(my_dict)

# 識別子key2を削除してみよう！
my_dict.pop("key2")

print(my_dict)
