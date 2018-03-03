from tkinter import *

class View(Frame):
    # 設定初值
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    # 建立所有視窗元件
    def createWidgets(self):
        self.label01 = Label(self)
        self.label01["text"] = "請猜出 0 到 9 之間的正整數..."
        self.label01.grid(row=0, column=0, columnspan=2)

        self.label02 = Label(self)
        self.label02["text"] = "總共有三次機會猜出正確數字..."
        self.label02.grid(row=1, column=0, columnspan=2)

        self.label03 = Label(self)
        self.label03["text"] = "準備好了嗎..."
        self.label03.grid(row=2, column=0, columnspan=2)

        self.label04 = Label(self)
        self.label04["text"] = "請輸入："
        self.label04.grid(row=3, column=0)

        self.input = Entry(self)
        self.input["width"] = 10
        self.input.grid(row=3, column=1)

        self.guess = Button(self)
        self.guess["text"] = "猜測"
        self.guess.grid(row=4, column=0)

        self.again = Button(self)
        self.again["text"] = "重來"
        self.again.grid(row=4, column=1)

        self.display = Label(self)
        self.display["text"] = ""
        self.display.grid(row=5, column=0, columnspan=2)

if __name__ == '__main__':
   root = Tk()
   app = View(master=root)
   app.mainloop()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：view.py
# 功能：猜數字遊戲的 GUI 版本
# 作者：張凱慶
