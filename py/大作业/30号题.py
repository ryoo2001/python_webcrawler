import csv
from itertools import islice


def trans(amount):
    if "美元" in amount:
        value = amount.split("美元")[0]
        if "数十万" == value[:3]:
            value = float(str(value).replace("数十万", "500000"))
        elif "数百万" == value[:3]:
            value = float(str(value).replace("数百万", "50000000"))
        elif "数千万" == value[:3]:
            value = float(str(value).replace("数千万", "50000000"))
        elif "数亿" == value[:2]:
            value = float(str(value).replace("数亿", "500000000"))
        elif "万其他" == value[-3:]:
            value = float(str(value).replace("万其他", "0000"))
        elif "亿其他" == value[-3:]:
            value = float(str(value).replace("亿其他", "00000000"))
        elif "亿" in value:
            value = float(str(value).replace("亿", "00000000"))
        elif "万" in amount:
            value = float(str(value).replace("万", "0000"))
        value *= 6
        return value
    elif "卢布" in amount:
        value = amount.split("卢布")[0]
        if "数十万" == value[:3]:
            value = float(str(value).replace("数十万", "500000"))
        elif "数百万" == value[:3]:
            value = float(str(value).replace("数百万", "50000000"))
        elif "数千万" == value[:3]:
            value = float(str(value).replace("数千万", "50000000"))
        elif "数亿" == value[:2]:
            value = float(str(value).replace("数亿", "500000000"))
        elif "万其他" == value[-3:]:
            value = float(str(value).replace("万其他", "0000"))
        elif "亿其他" == value[-3:]:
            value = float(str(value).replace("亿其他", "00000000"))
        elif "亿" in value:
            value = float(str(value).replace("亿", "00000000"))
        elif "万" in amount:
            value = float(str(value).replace("万", "0000"))
        value *= 0.1
        return value
    elif "英镑" in amount:
        value = amount.split("英镑")[0]
        if "数十万" == value[:3]:
            value = float(str(value).replace("数十万", "500000"))
        elif "数百万" == value[:3]:
            value = float(str(value).replace("数百万", "50000000"))
        elif "数千万" == value[:3]:
            value = float(str(value).replace("数千万", "50000000"))
        elif "数亿" == value[:2]:
            value = float(str(value).replace("数亿", "500000000"))
        elif "万其他" == value[-3:]:
            value = float(str(value).replace("万其他", "0000"))
        elif "亿其他" == value[-3:]:
            value = float(str(value).replace("亿其他", "00000000"))
        elif "亿" in value:
            value = float(str(value).replace("亿", "00000000"))
        elif "万" in amount:
            value = float(str(value).replace("万", "0000"))
        value *= 8.5
        return value
    elif "欧元" in amount:
        value = amount.split("欧元")[0]
        if "数十万" == value[:3]:
            value = float(str(value).replace("数十万", "500000"))
        elif "数百万" == value[:3]:
            value = float(str(value).replace("数百万", "50000000"))
        elif "数千万" == value[:3]:
            value = float(str(value).replace("数千万", "50000000"))
        elif "数亿" == value[:2]:
            value = float(str(value).replace("数亿", "500000000"))
        elif "万其他" == value[-3:]:
            value = float(str(value).replace("万其他", "0000"))
        elif "亿其他" == value[-3:]:
            value = float(str(value).replace("亿其他", "00000000"))
        elif "亿" in value:
            value = float(str(value).replace("亿", "00000000"))
        elif "万" in amount:
            value = float(str(value).replace("万", "0000"))
        value *= 7.3
        return value
    elif "日元" in amount:
        value = amount.split("日元")[0]
        if "数十万" == value[:3]:
            value = float(str(value).replace("数十万", "500000"))
        elif "数百万" == value[:3]:
            value = float(str(value).replace("数百万", "50000000"))
        elif "数千万" == value[:3]:
            value = float(str(value).replace("数千万", "50000000"))
        elif "数亿" == value[:2]:
            value = float(str(value).replace("数亿", "500000000"))
        elif "万其他" == value[-3:]:
            value = float(str(value).replace("万其他", "0000"))
        elif "亿其他" == value[-3:]:
            value = float(str(value).replace("亿其他", "00000000"))
        elif "亿" in value:
            value = float(str(value).replace("亿", "00000000"))
        elif "万" in amount:
            value = float(str(value).replace("万", "0000"))
        value *= 0.05
        return value
    elif "卢比" in amount:
        value = amount.split("卢比")[0]
        if "数十万" == value[:3]:
            value = float(str(value).replace("数十万", "500000"))
        elif "数百万" == value[:3]:
            value = float(str(value).replace("数百万", "50000000"))
        elif "数千万" == value[:3]:
            value = float(str(value).replace("数千万", "50000000"))
        elif "数亿" == value[:2]:
            value = float(str(value).replace("数亿", "500000000"))
        elif "万其他" == value[-3:]:
            value = float(str(value).replace("万其他", "0000"))
        elif "亿其他" == value[-3:]:
            value = float(str(value).replace("亿其他", "00000000"))
        elif "亿" in value:
            value = float(str(value).replace("亿", "00000000"))
        elif "万" in amount:
            value = float(str(value).replace("万", "0000"))
        value *= 0.08
        return value
    elif "港元" in amount:
        value = amount.split("港元")[0]
        if "数十万" == value[:3]:
            value = float(str(value).replace("数十万", "500000"))
        elif "数百万" == value[:3]:
            value = float(str(value).replace("数百万", "50000000"))
        elif "数千万" == value[:3]:
            value = float(str(value).replace("数千万", "50000000"))
        elif "数亿" == value[:2]:
            value = float(str(value).replace("数亿", "500000000"))
        elif "万其他" == value[-3:]:
            value = float(str(value).replace("万其他", "0000"))
        elif "亿其他" == value[-3:]:
            value = float(str(value).replace("亿其他", "00000000"))
        elif "亿" in value:
            value = float(str(value).replace("亿", "00000000"))
        elif "万" in amount:
            value = float(str(value).replace("万", "0000"))
        value *= 0.89
        return value
    elif "未透露" in amount:
        return 0
    else:
        value = amount.split("人民币")[0]
        if "数十万" == value[:3]:
            value = float(str(value).replace("数十万", "500000"))
        elif "数百万" == value[:3]:
            value = float(str(value).replace("数百万", "50000000"))
        elif "数千万" == value[:3]:
            value = float(str(value).replace("数千万", "50000000"))
        elif "数亿" == value[:2]:
            value = float(str(value).replace("数亿", "500000000"))
        elif "万其他" == value[-3:]:
            value = float(str(value).replace("万其他", "0000"))
        elif "亿其他" == value[-3:]:
            value = float(str(value).replace("亿其他", "00000000"))
        elif "亿" in value:
            value = float(str(value).replace("亿", "00000000"))
        elif "万" in amount:
            value = float(str(value).replace("万", "0000"))
        return value


with open('D:\\PycharmProjects\VVVF\py\大作业\online-education-invest-utf8.csv', 'r', encoding="UTF-8") as f:
    reader = csv.reader(f)
    data = [row for row in islice(reader, 1, None)]
year = input()
count = {}
for row in data:
    time = row[0]
    company = row[1]
    round = row[3]
    money = row[4]
    money1 = trans(money)
    if time[:4] != year:
        continue
    if company not in count:
        count[company] = {"round": 0, "money": 0}
    count[company]["round"] += 1
    count[company]["money"] += int(money1)
for company, stat in sorted(count.items(), key=lambda x: (-x[1]['round'], -x[1]['money'], x[0])):
    print(f'公司名称：{company}，轮次总次数：{stat["round"]}，总金额：{stat["money"]}')
