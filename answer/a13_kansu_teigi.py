"""
ExcelのSUM関数使いましたよね？
プログラミングでは、自分で関数を作ることもできます！

"""

def sum(ran):
    result = 0
    for one in ran:
        result += one

    return result
data = sum([1,5,20,4])

print(data)