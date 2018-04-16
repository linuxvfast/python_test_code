import select,socket,queue,sys

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',9999))
server.listen(1000)

server.setblocking(0)  #设置为非阻塞
inputs = [server] #存放建立连接的socket
outputs = []   #需要发送给客户端的信息
msg_dic = {}   #服务器收到数据之后先不发送给客户端，先保存在字典中
while True:
    #readable 内核需要监测的连接
    #writeable
    #exceptional 中断的连接
    readable,writeable,exceptional =select.select(inputs,outputs,inputs)
    # print(readable,writeable,exceptional)
    # server.accept()
    for s in readable:
        if s is server:  #代表来了一个新连接
            conn,addr = server.accept()
            print('新连接',conn)
            inputs.append(conn) #当前新建立的连接还没有发送数据过来，现在就接收数据的话程序报错，所以要想实现客户端发送数据过来时\
            # server端能知道，就需要让server端再监测conn
            msg_dic[conn] = queue.Queue()  #初始化一个队列，存放收到的客户端数据
        else:
            try:
                data = s.recv(1024)
                print('recv', data)
            except ConnectionResetError as e:  #检测客户端是否断开，如果客户端断开，将删除监听inputs和返回连接outputs,\
                #以及存储需要返回给客户端的数据msg_dic
                print('客户端已经断开连接')
                if s in outputs:  # 如果客户端发送过数据，就会在outputs中保存连接，客户端断开之后需要删除
                    outputs.remove(s)
                inputs.remove(s)  # 将断开连接的客户端重监听列表中删除

                del msg_dic[s]  # 将断开的客户端保存在字典中的数据删除

            else:
                msg_dic[s].put(data)
                if s not in outputs:
                    outputs.append(s)


    for w in writeable:#要返回给客户端的连接列表
        data_to_client = msg_dic[w].get()
        w.send(data_to_client) #返回给客户端的源数据
        outputs.remove(w)  #删除已经返回给客户端的连接

    for e in exceptional:  #客户端断开
        if e in outputs: #如果客户端发送过数据，就会在outputs中保存连接，客户端断开之后需要删除
            outputs.remove(e)
        inputs.remove(e) #将断开连接的客户端重监听列表中删除
        e.close()

        del msg_dic[e] #将断开的客户端保存在字典中的数据删除


