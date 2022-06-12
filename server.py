import sys
import tkinter
import tkinter.font as tkFont
import socket
import threading
import time
import DbHelper
import FileHelper

# noinspection PyAttributeOutsideInit,PySimplifyBooleanCheck
class Server:
    host = '127.0.0.1'
    port = 8082
    serverSock = None
    flag = False
    table = "chat_log"

    # 初始化类的相关属性的构造函数
    def __init__(self):
        DbHelper.DbHelper.init_connect()
        self.root = tkinter.Tk()
        self.root.title('python聊天-服务器端')
        # 窗口面板，用四个frame面板布局
        self.frame = [tkinter.Frame(), tkinter.Frame(), tkinter.Frame(), tkinter.Frame()]
        # 显示消息Text右边的滚条
        self.chatTextScrollBar = tkinter.Scrollbar(self.frame[0])
        self.chatTextScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # 显示消息Text，并绑定上面的滚动条
        ft = tkFont.Font(family='Fixdsys', size=11)
        self.chatText = tkinter.Listbox(self.frame[0], width=70, height=18, font=ft)
        self.chatText['yscrollcommand'] = self.chatTextScrollBar.set
        self.chatText.pack(expand=1, fill=tkinter.BOTH)
        self.chatTextScrollBar['command'] = self.chatText.yview()
        self.frame[0].pack(expand=1, fill=tkinter.BOTH)
        # 标签，分开消息显示Text和消息输入Text
        label = tkinter.Label(self.frame[1], height=2)
        label.pack(fill=tkinter.BOTH)
        self.frame[1].pack(expand=1, fill=tkinter.BOTH)
        # 输入消息Text的滚动条
        self.inputTextScrollBar = tkinter.Scrollbar(self.frame[2])
        self.inputTextScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        # 输入消息Text，并与滚动条绑定
        ft = tkFont.Font(family='Fixdsys',size=11)
        self.inputText = tkinter.Text(self.frame[2], width=70, height=8, font=ft)
        self.inputText['yscrollcommand'] = self.inputTextScrollBar.set
        self.inputText.pack(expand=1, fill=tkinter.BOTH)
        self.inputTextScrollBar['command'] = self.chatText.yview()
        self.frame[2].pack(expand=1, fill=tkinter.BOTH)

        # 发送按钮
        self.sendButton = tkinter.Button(self.frame[3], text='发送', width=10, command=self.sendMessage)
        self.sendButton.pack(expand=1, side=tkinter.BOTTOM and tkinter.RIGHT, padx=25, pady=5)
        # 关闭按钮
        self.closeButton = tkinter.Button(self.frame[3], text='关闭', width=10, command=self.close)
        self.closeButton.pack(expand = 1,side = tkinter.RIGHT, padx=25, pady=5)
        self.frame[3].pack(expand=1, fill=tkinter.BOTH)

    # 接收消息
    def receiveMessage(self):
        # 建立socket连接
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSock.bind((self.host, self.port))
        self.serverSock.listen(15)
        self.buffer = 1024
        self.chatText.insert(tkinter.END, '服务器已经就绪........')
        # 循环接收客户端的连接请求
        while True:
            self.connection, self.address = self.serverSock.accept()
            self.flag = True
            while True:
                self.clientMsg = self.connection.recv(self.buffer).decode('utf-8')
                if not self.clientMsg:
                    continue
                elif self.clientMsg == 'Y':
                    self.chatText.insert(tkinter.END, '服务器已经与客户端建立连接.......')
                    self.connection.send(b'Y')
                elif self.clientMsg == 'N':
                    self.chatText.insert(tkinter.END, '服务器和客户端建立连接失败........')
                    self.connection.send(b'N')
                else:
                    theTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
                    self.chatText.insert(tkinter.END, '客户端'+theTime+'说: \n')
                    self.chatText.insert(tkinter.END, '  '+self.clientMsg)
    # 发送消息
    def sendMessage(self):
        # 得到用户在Text中输入的消息
        message = self.inputText.get('1.0', tkinter.END)
        # 格式化当前时间
        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        self.chatText.insert(tkinter.END, '服务器'+theTime+'说：\n')
        self.chatText.insert(tkinter.END, ' '+message +'\n')
        if self.flag:
            # 将消息发送到客户端
            self.connection.send(message.encode())
            # 清楚输入信息
            self.inputText.delete(0.0, message.__len__() - 1.0)
            # 持久化聊天信息
            DbHelper.DbHelper.insert(self.table, "服务端", "客户端", message)
            FileHelper.FileHelper.write("{} {} 给 {} 发送消息： {}".format(theTime, "服务端", "客服端", message))

        else:
            # Socket 连接没有建立用户，提示用户
            self.chatText.insert(tkinter.END, '你还未与客户端建立连接，客户端无法收到你的消息\n')
            # 清空用户在Text中输入的消息
            self.inputText.delete(0.0, message.__len__()-1.0)

    # 关闭消息窗口并退出
    def close(self):
        DbHelper.DbHelper.close()
        sys.exit()

    # 启动线程接收客户消息
    def startnewthread(self):
        thread = threading.Thread(target=self.receiveMessage, args=())
        thread.setDaemon(True)
        thread.start()


def main():
    server = Server()
    server.startnewthread()
    server.root.mainloop()


if __name__ == '__main__':

    main()

