import os
import shutil
import json


json_file = './train_multi_label.json'
our_data = json.load(open(json_file, 'r'))

pifold_json_file = './data.json'
data = json.load(open(pifold_json_file, 'r'))
pifold_data = data['test']

# print(pifold_data)

for key, values in our_data.items():
    # 构建文件的相对路径
    for value in values:
        if value in pifold_data:
            print(key, value)
            print(pifold_data[value])
            print('------------------')

