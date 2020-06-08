# 引数にlistを渡す。
# list内は全て数字で構成されており、全てを加算した結果を返す。
# 引数：[1,5,20,4]ならば、戻り値は1 + 5 + 20 + 4 = 30
def sum(ran):
    result = 0
    for one in ran:
        result += one

    return result


data = sum([1,5,20,4])

print(data)