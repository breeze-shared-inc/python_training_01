from im import a

def check():
    r = a


    for one in r:
        for profile in one:
            if profile == "name":
                print("{}さんの".format(one[profile]))
            if profile == "birth":
                print("誕生日は{}。".format(one[profile]))
            if profile == "livein":
                print("出身地は{}。".format(one[profile]))


check()