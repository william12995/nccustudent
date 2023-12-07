

# 複製檔案路徑
import pandas as pd
data = pd.read_csv("./output (1).csv", encoding = "UTF-8")

type_mapping = {
    "填表單": "問卷",
    "問卷": "問卷",
    "剩下的食物": "剩食",
    "多的食物": "剩食",
    "剩下的食物": "剩食",
    "剩下的便當": "剩食",
    "剩下三明治": "剩食",
    "剩下的炸雞": "剩食",
    "剩下的披薩": "剩食",
    "多的便當": "剩食",
    "多的三明治": "剩食",
    "多的炸雞": "剩食",
    "多的餐盒": "剩食",
    "可以過來拿": "剩食",
    "可以來拿": "剩食",
    "剩下的披薩": "剩食",
    "便當": "剩食",
    "撿到": "遺失物",
    "取回": "遺失物",
    "快去領": "遺失物",
    "掉在": "遺失物",
    "失主": "遺失物",
    "遺失": "遺失物",
    "駐警隊": "遺失物",
    "招領處": "遺失物",
    "拾獲": "遺失物",
    "忘在": "遺失物",
    "指南派出所": "遺失物",
    "同學你的": "遺失物",
    "遺忘": "遺失物",
    "來領": "遺失物",
    "丟在": "遺失物",
    "掉在": "遺失物",
    "帶他回家": "遺失物",
    "協尋": "遺失物",
    "忘記帶走": "遺失物",
    "尋傘": "遺失物",
    "已送至": "遺失物",
    "已送到": "遺失物",
    "不小心拿": "遺失物",
}

type = []

for content1 in data['貼文內容']:
    content_type = "其他"

    for keyword, category in type_mapping.items():
        if keyword in content1:
            content_type = category
            break

    type.append(content_type)

data['type'] = type

data_1 = data["type"] == "問卷"
data_2 = data["type"] == "遺失物"
data_3 = data["type"] == "剩食"
data_4 = data["type"] == "其他"



def getURL(user_input = ""):

  if user_input == "1": #問卷

    return data[data_1 == True]["貼文連結"].head(5)

  elif user_input == "2": #遺失物

    return data[data_2 == True]["貼文連結"].head(5)

  elif user_input == "3": #剩食

    return data[data_3 == True]["貼文連結"].head(5)

  elif user_input == "4": #其他

    return data[data_4 == True]["貼文連結"].head(5)

  else:
    print("ERROR")
