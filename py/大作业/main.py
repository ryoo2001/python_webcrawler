import pandas as pd
import cn2an

# 人民币美元汇率常量
USD2RMB = 7.0
# 人民币卢比汇率常量
RUB2RMB = 0.084
# 人民币英镑汇率常量
UKP2RMB = 8.57
# 人民币欧元汇率常量
EUR2RMB = 8.0
# 人民币日元汇率常量
JPY2RMB = 0.063


# 筛选出指定年份的数据
def filter_data_by_year(data, year):
    data = data[pd.to_datetime(data['时间']).dt.year == year]
    return data


# 判断是否全为中文
def is_all_ChineseTxt(str):
    for ch in str:
        if not '\u4e00' <= ch <= '\u9fff':
            return False
    return True


# 筛选出“公司名称”为全中文的数据
def filter_data_by_ChineseTxt(data):
    data = data[data['公司名称'].apply(is_all_ChineseTxt)]
    return data


# 清洗数据:将金额中的中文转换为数字并同一单位，金额范围按中值计算，未披露金额的按0计算
def clean_data(data):
    for index, row in data.iterrows():
        # 将未透露的金额转换为0
        if row['金额'] == '未透露':
            row['金额'] = '0'

        # 金额范围按中值计算
        if row['金额'].startswith('数'):
            row['金额'] = row['金额'].replace('数', '5')

        # 将中文金额转换为数字
        if "亿" in row['金额']:
            temp_str_list = row['金额'].split('亿')
            temp_str_list[0] = cn2an.cn2an(temp_str_list[0] + "亿", "smart")
            row['金额'] = str(temp_str_list[0]) + temp_str_list[1]
        elif "万" in row['金额']:
            temp_str_list = row['金额'].split('万')
            temp_str_list[0] = cn2an.cn2an(temp_str_list[0] + "万", "smart")
            row['金额'] = str(temp_str_list[0]) + temp_str_list[1]

        # 汇率转换成人民币
        if row['金额'].endswith('美元'):
            row['金额'] = str(float(row['金额'].replace('美元', '')) * USD2RMB)
        elif row['金额'].endswith('卢比'):
            row['金额'] = str(float(row['金额'].replace('卢比', '')) * RUB2RMB)
        elif row['金额'].endswith('英镑'):
            row['金额'] = str(float(row['金额'].replace('英镑', '')) * UKP2RMB)
        elif row['金额'].endswith('欧元'):
            row['金额'] = str(float(row['金额'].replace('欧元', '')) * EUR2RMB)
        elif row['金额'].endswith('人民币'):
            row['金额'] = str(float(row['金额'].replace('人民币', '')))
        elif row['金额'].endswith('日元'):
            row['金额'] = str(float(row['金额'].replace('日元', '')) * JPY2RMB)
        else:
            row['金额'] = 0

        # 以万做单位
        row['金额'] = float(row['金额']) / 1000


data = pd.read_csv('D:\\PycharmProjects\VVVF\py\大作业\online-education-invest-utf8.csv', encoding='utf-8', header=0)
input_year = int(input('请输入年份：'))
data = filter_data_by_year(data, input_year)
data = filter_data_by_ChineseTxt(data)
clean_data(data)

# 按公司名称分组,按月份分组，统计每个公司每个月的投资金额和次数
data = data.groupby(['公司名称', pd.to_datetime(data['时间']).dt.month])
result = data['金额'].apply(lambda x: x.astype(float).sum())
result = result.reset_index()
result = result.groupby(['公司名称']).sum()
result = result.sort_values(by='金额', ascending=False)
result = result.reset_index()
result = result.rename(columns={'金额': '投资金额(万)'})
result['投资次数'] = data['金额'].count().reset_index()['金额']
result = result.sort_values(by='投资金额(万)', ascending=False)
result = result.reset_index(drop=True)
for index, row in result.iterrows():
    print('公司名称：' + row['公司名称'] + '，投资金额(万)：' + str(row['投资金额(万)']) + '，投资次数：' + str(
        row['投资次数']))
