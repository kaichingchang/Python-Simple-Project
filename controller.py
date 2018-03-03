from tkinter import Tk
from guess import Guess
from view import View

class Controller:
    def __init__(self):
        self.g = Guess()
        self.count = 0
        self.flag = 0

        self.app = View(master=Tk())
        self.app.guess["command"] = self.guess
        self.app.again["command"] = self.again
        self.app.mainloop()

    def guess(self):
        self.count += 1
        result = self.g.answer(int(self.app.input.get()))
        if result == 0:
            self.app.display["text"] = "答對！你猜了" + str(self.count) + "次..."
            self.app.guess["state"] = "disabled"
            self.flag = 1
        elif result == 1:
            self.app.display["text"] = "大一點！"
        elif result == 2:
            self.app.display["text"] = "小一點！"
        else:
            self.app.display["text"] = "不正確的輸入..."

        if self.flag == 0 and self.count == 3:
            self.app.guess["state"] = "disabled"
            self.app.display["text"] = "猜了三次也沒猜對，答案是" + str(self.g.number) + "。"

        self.app.input.delete(0, 200)

    def again(self):
        self.g = Guess()
        self.count = 0
        self.flag = 0
        self.app.display["text"] = ""
        self.app.guess["state"] = "normal"

if __name__ == '__main__':
   game = Controller()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：controller.py
# 功能：猜數字遊戲的 GUI 版本
# 作者：張凱慶
