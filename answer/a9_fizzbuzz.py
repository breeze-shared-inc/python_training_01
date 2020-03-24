"""
FizzBuzzゲームを実装してみよう
元々はパーティゲームで行われていたのですが、

・参加者が順番に1から番号を言っていく
・ただし、3の倍数は「fizz」、5の倍数は「buzz」
　３と５の倍数はfizzbuzz
・例
　1,2,fizz,3,4,buzz,fizz,7,8,fizz,buzz,
　11,fizz,13,14,fizzbuzz

問題、fizzbuzzをプログラミングで表現させよう

ヒント:
・3の倍数や5の倍数をどうやってプログラミングで
　表現しよう。。。？
・まずは日本語で書いてプログラムに起こすとやりやすい
　倍数が3かつ5でないなら、fizzを出力
　倍数が3でないかつ5なら、buzzを出力
　倍数が3であり、5であるならfizzbuzzを出力　　

・3の倍数で割り切れるということは
　「余りがゼロ」になるということ！！



"""



for num in range(1, 51):

    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")

    elif num % 3 == 0 and num % 5 != 0:
        print("fizz")

    elif num % 3 != 0 and num % 5 == 0:
        print("buzz")

    else:
        print(num)