"""
ExcelのSUM関数使いましたよね？
プログラミングでは、自分で関数を作ることもできます！

"""

# num には配列が入ります。
def sum(num):
    result = 0
    for val in num:
        result += val
    return result

suji = [2,5,6,4]

print(sum(suji))