import tkinter
import tkinter.font as tkFont
import sys
import time
import DbHelper


# 展示聊天记录界面
class ListChat:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('python聊天记录')

        self.frame = (tkinter.Frame(), tkinter.Frame(), tkinter.Frame(), tkinter.Frame())

        self.chatTextScrollBar = tkinter.Scrollbar(self.frame[0])
        self.chatTextScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

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

    def get_chat_list(self):
        DbHelper.DbHelper.init_connect()
        chat_list = DbHelper.DbHelper.get_all()
        for chat in chat_list:
            user_name = chat[1]
            target_name = chat[2]
            message = chat[3]
            send_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(chat[4]))
            #print(user_name, target_name,message, send_time)
            self.chatText.insert(tkinter.END, '{}  {} 发送给 {} 内容：{} \r'.format(send_time, user_name, target_name, message))

    # 关闭消息窗口并退出
    def close(self):
        sys.exit()


def main():
    list_chat = ListChat()
    list_chat.get_chat_list()
    list_chat.root.mainloop()


if __name__ == '__main__':
    main()
