"""
・デバッグとは
プログラムのバグを発見し、修正すること。
虫取りが語源

・ツール活用の重要性
VSCODEにはデバッグツールが導入されている

機能
ブレークポイント：
指定行までプログラムが実行された場合、プログラムの処理を一時停止し、その間で格納されている変数の値を確認することができる


ウォッチ式：
特定の変数を監視させて値の動きを追う


・デバッグツールを活用するメリット
不具合の発見効率が上がる（デバッグスキルを磨けばプログラミングも上がります）
作業効率が圧倒的に上がります。


"""


""" question!!!!!
デバッグを活用してどこが間違っているかを発見して、修正してみよう

<正しい出力例>
田中さんの
誕生日は1999/11/11。
出身地はtokyo。
山田さんの
誕生日は2009/11/11。
出身地はtokyo。
富山さんの
誕生日は2019/11/11。
出身地はsapporo。

"""
import requests as req
import json

def check():
    r = req.get("https://script.google.com/macros/s/AKfycbx59mSU5gTZ_FExAwaZrgjEorUcuki0AqGnh_XYn5uyZi_RSYzJ/exec")
    r = json.loads(r.text)

    for one in r:
        for profile in one:
            if profile == "name":
                print("{}さんの".format(one[profile]))
            if profile == "birth":
                print("誕生日は{}。".format(one[profile]))
            if profile == "born":
                print("出身地は{}。".format(one[profile]))


check()