"""
dict = {
    "name":"田中"
    "age":20
    "seibetsu": "男"
}

name_list = [
    ["田中", 20, "男"],
    ["鈴木", 21, "女"],
    ["鈴木", 21, "女"],
]

name_list[0].append("お酒")
name_list[0][3] = "カラオケ"
name_list[1].insert(1,"カラオケ")
name_list[0].pop()
name_list[1].pop(1)

print(name_list[0])
print(name_list[1])

for(let num in range ){

}

"""
name_list = [
    ["田中", 20, "男"],
    ["鈴木", 21, "女"],
    ["田中", 20, "男"],
    ["鈴木", 21, "女"],
    ["田中", 20, "男"],
    ["鈴木", 21, "女"],
    ["田中", 20, "男"],
    ["鈴木", 21, "女"],
    ["田中", 20, "男"],
    ["鈴木", 21, "女"],
    ["田中", 20, "男"],
    ["鈴木", 21, "女"],
    ["田中", 20, "男"],
    ["鈴木", 21, "女"],
    ["田中", 20, "男"],
    ["鈴木", 21, "女"],
]

for num in name_list:
    for profile in num:
        if profile == "鈴木" or profile == "田中":
            print(profile + "さんは")
        elif type(profile) == int:
            print(str(profile) + "さい")
        else:
            print("性別は" + profile)
