#!/usr/bin/python
# coding=utf-8
# ?通配符，表示匹配0或1个字符
# *通配符，表示匹配0或多个字符

# ^为匹配输入字符串的开始位置
# $为匹配输入字符串的结束位置

import re

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*) .*', line, re.M | re.I)
if matchObj:
    print(matchObj.group())
    print(matchObj.group(1))
    print(matchObj.group(2))
    print('匹配完毕!!')
else:
    print('没有劈匹配!!')

phone = "123-456-789 # 这是一个电话"
num = re.sub(r'#.*$', "", phone)
print("电话号码："), num
num = re.sub(r'\D', "", phone)
print("电话号码："), num
