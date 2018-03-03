from random import randint

#計算核心
class Guess:
    def __init__(self):
        #答案
        self.number = randint(0, 9)

    #判斷大小
    def answer(self, guess):
        if self.number == guess:
            return 0
        else:
            if self.number > guess:
                return 1
            else:
                return 2

if __name__ == "__main__":
    g = Guess()
    for i in range(10):
        print(g.answer(i))

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：demo.py
# 功能：猜數字遊戲的計算核心
# 作者：張凱慶
