import random

import requests  # 调用API 127.0.0.1:8080
import random
messages = ["机器人已上线，正在等待你的命令..."]
#ID0：上线消息
import pymongo
import time
Verifykey = input('请输入你的VerifyKey，它可能在MCL的运行窗口内。')
qq = input('请输入Bot的QQ号')
UserQQ=input('请输入你用于设置MiraiBot的管理员账号')
def init():
    botLog = open("./logs/log_"+str(random.randint(000000,8388609))+".log",'a+')
    verify = requests.post('http://127.0.0.1:8080/verify', data='{"verifyKey": "'+Verifykey+'"}')
    sessionJson=verify.json()
    sessionData='{"sessionKey": '+sessionJson['session']+', "qq": '+qq+'}'
    sessionVerifyResponse=requests.post('http://127.0.0.1:8080/bind', data=sessionData)
    getNickname = requests.get('http://127.0.0.1:8080/sessionInfo?sessionKey='+sessionJson['session'])
    YourID = getNickname.json()
    print("")
    print("您好，",YourID["data"]["qq"]["nickname"],"欢迎使用MiraiBot，您的会话是：",sessionJson['session'])
    onlinemsg='{"sessionKey": "'+sessionJson['session']+'", "target": '+UserQQ+', "messageChain": [{"type": "Plain", "text": "'+messages[0]+'"}]}'
    print(onlinemsg)
    onlinemsg=onlinemsg.encode('utf-8')
    #requests.post('http://127.0.0.1:8080/sendFriendMessage', data=onlinemsg) # 因为开发者正在调试机器人，故被注释
    while True:
        response = requests.get('http://127.0.0.1:8080/fetchMessage?sessionKey='+sessionJson['session']+'&count=1')
        response = response.json()
        if response['data'] == []:
            pass
        else:
            msg = str(response['data'])
            msg = str(msg.encode('utf-8'))+"\n"
            botLog.write(msg)
            response = response['data']
            print(response[0])
init()
