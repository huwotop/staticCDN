import base64
import requests
from lxml import etree

v = 
"vless://196b6c47-41c9-4f96-8fee-1238e983597e@158.101.132.255:8881?encryption=none&security=reality&sni=addons.mozilla.org&fp=chrome&pbk=GPnzQut0UNo4wpSR2IV_2XsVUwnsbqzwCzwPcPc4-nM&type=tcp&headerType=none#虎窝节点%20xtls-reality\n
hysteria2://196b6c47-41c9-4f96-8fee-1238e983597e@158.101.132.255:8882/?alpn=h3&insecure=1#虎窝节点%20hysteria2\n
tuic://196b6c47-41c9-4f96-8fee-1238e983597e:196b6c47-41c9-4f96-8fee-1238e983597e@158.101.132.255:8883?alpn=h3&congestion_control=bbr#虎窝节点%20tuic\n
ss://YWVzLTEyOC1nY206MTk2YjZjNDctNDFjOS00Zjk2LThmZWUtMTIzOGU5ODM1OTdlQDE1OC4xMDEuMTMyLjI1NTo4ODg1#虎窝节点%20shadowsocks\n
trojan://196b6c47-41c9-4f96-8fee-1238e983597e@158.101.132.255:8886?security=tls&type=tcp&headerType=none#虎窝节点%20trojan\n
vmess://eyAidiI6ICIyIiwgInBzIjogIuiZjueqneiKgueCuSB2bWVzcy13cyIsICJhZGQiOiAiY2RuLWIxMDAueG4tLWI2Z2FjLmV1Lm9yZyIsICJwb3J0IjogIjgwIiwgImlkIjogIjE5NmI2YzQ3LTQxYzktNGY5Ni04ZmVlLTEyMzhlOTgzNTk3ZSIsICJhaWQiOiAiMCIsICJzY3kiOiAibm9uZSIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZGVtby5odXdvLnRvcCIsICJwYXRoIjogIi8xOTZiNmM0Ny00MWM5LTRmOTYtOGZlZS0xMjM4ZTk4MzU5N2Utdm1lc3MiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIiB9\n
vless://196b6c47-41c9-4f96-8fee-1238e983597e@cdn-b100.xn--b6gac.eu.org:443?encryption=none&security=tls&sni=demo.huwo.top&type=ws&host=demo.huwo.top&path=%2F196b6c47-41c9-4f96-8fee-1238e983597e-vless%3Fed%3D2048#虎窝节点%20vless-ws-tls\n
vless://196b6c47-41c9-4f96-8fee-1238e983597e@158.101.132.255:8890?encryption=none&security=reality&sni=addons.mozilla.org&fp=chrome&pbk=GPnzQut0UNo4wpSR2IV_2XsVUwnsbqzwCzwPcPc4-nM&type=grpc&serviceName=grpc&mode=gun#虎窝节点%20grpc-reality\n"

def ipQuery(ip):    
    url = "https://browserleaks.com/ip/" + ip
    req = requests.get(url).text
    html = etree.HTML(req)
    addr = html.xpath('//img[@class="flag-icon"]/@title')  #地址
    # print(addr)
    return addr[0].strip()

str = v+"\n"    
with open('jiedian.list', 'w') as f:
    with open('cf_ip.txt', 'r', encoding='utf-8') as f1:
        lines = f1.readlines()
        for l in lines:
            ip = l.strip()
            addr = ipQuery(ip)
            str = str + "vless://3bd13558-f707-4f88-be35-ffd7cc9864fe@"+ip+":443?encryption=none&security=tls&sni=cfpgvless.huwo.top&fp=randomized&type=ws&host=cfpgvless.huwo.top&path=%2F%3Fed%3D2048#"+addr+"\n"
              
        f.write(base64.b64encode(str.encode('utf-8')).decode('utf-8'))
