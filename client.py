import threading
import tkinter
import tkinter.font as tkFont
import socket
import sys
import time
import DbHelper
import FileHelper


class Client:
    host = '127.0.0.1'
    port = 8082
    flag = False
    buffer = 1024
    serverMsg = ""
    clientSock = None
    table = "chat_log"
    def __init__(self):
        DbHelper.DbHelper.init_connect()
        self.root = tkinter.Tk()
        self.root.title('python聊天-客户端')
        # 窗口面板，用四个frame面板布局
        self.frame = (tkinter.Frame(), tkinter.Frame(), tkinter.Frame(), tkinter.Frame())
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
        ft = tkFont.Font(family='Fixdsys', size=11)
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

        self.closeButton.pack(expand=1, side=tkinter.RIGHT, padx=25, pady=5)
        self.frame[3].pack(expand=1, fill=tkinter.BOTH)


    # 接收信息
    def receiveMessage(self):

        try:
            # 建立Socket连接
            self.clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientSock.connect((self.host, self.port))
            self.flag = True
        except ConnectionError:
            self.flag = False
            self.chatText.insert(tkinter.END, '你还未与服务器建立连接，请检查服务器是否启动')
            return

        self.clientSock.send('Y'.encode())  # 向服务器端发送字符Y，表示客户端要连接服务器

        while True:
            try:
                if self.flag:
                    self.serverMsg = self.clientSock.recv(self.buffer).decode('utf-8')
                    if self.serverMsg == 'Y':
                        self.chatText.insert(tkinter.END, '客户端已经与服务器端建立连接.....')
                    elif self.serverMsg == 'N':
                        self.chatText.insert(tkinter.END, '客户端与服务器端建立连接失败....')
                    elif not self.serverMsg:
                        continue
                    else:
                        thetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        self.chatText.insert(tkinter.END, '服务器端' + thetime + '说：\n')
                        self.chatText.insert(tkinter.END, '  ' + self.serverMsg)
                else:
                    break
            except EOFError as msg:
                raise msg
                self.clientSock.close()
                break

    # 发送消息
    def sendMessage(self):
        message = self.inputText.get('1.0', tkinter.END)
        # 格式化当前时间
        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.chatText.insert(tkinter.END, '客户端' + theTime + '说：\n')
        self.chatText.insert(tkinter.END, '  ' + message + '\n')
        if self.flag:
            self.clientSock.send(message.encode())
            self.inputText.delete(0.0, message.__len__() - 1.0)
            #持久化消息
            DbHelper.DbHelper.insert(self.table, "服务端", "客户端", message)
            FileHelper.FileHelper.write("{} {} 给 {} 发送消息： {}".format(theTime, "客户端", "服务端", message))
        else:
            self.chatText.insert(tkinter.END, '你还未与服务器端建立连接,服务器端无法收到你的消息\n')
            self.inputText.delete(0.0, message.__len__() - 1.0)

    # 关闭消息窗口并退出
    def close(self):
        DbHelper.DbHelper.close()
        sys.exit()

    # 启动线程接收服务器端消息
    def startNewThread(self):
        thread = threading.Thread(target=self.receiveMessage, args=())
        thread.setDaemon(True)
        thread.start()


def main():
    client = Client()
    client.startNewThread()
    client.root.mainloop()


if __name__ == '__main__':
    main()
