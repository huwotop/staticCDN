import requests
import datetime
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

url1 = 'https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/cncidr.txt'
url2 = 'https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/direct.txt'

def get_content(url):
    response = requests.get(url)
    return response.text

cncidr = get_content(url1)
direct = get_content(url2)

with open('direct.list', 'w', encoding='utf-8') as f:
    f.write(f'# 内容：直接访问域名与IP\n')
    f.write(f'# 来源：https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/cncidr.txt\n')
    f.write(f'# 来源：https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/direct.txt\n')
    f.write(f'# 更新：{now_time}\n')
    for c in cncidr.split('\n'):
        if '-' in c:
            c = c[5:]
            c = c[:-1]
            f.write(f'IP-CIDR,{c},no-resolve\n')
            
    for d in direct.split('\n'):
        if '+' in d:
            d = d[7:]
            d = d[:-1]
            f.write(f'DOMAIN-SUFFIX,{d}\n')
        elif '-' in d:
            d = d[5:]
            d = d[:-1]
            f.write(f'DOMAIN,{d}\n')
