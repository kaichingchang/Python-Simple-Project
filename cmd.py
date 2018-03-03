from guess import Guess

#終端機版本
class CMD:
    @staticmethod
    def gameloop():
        #步驟一：印出提示訊息
        print("請猜出 0 到 9 之間的正整數...")
        print("總共有三次機會猜出正確數字...")
        print("準備好了嗎...")

        #步驟二：建立計算核心物件
        g = Guess()

        #步驟三：遊戲的主要迴圈
        count = 0 #記錄次數
        flag = 0  #記錄答對與否
        while count < 3:
            count += 1
            n = input("請輸入：")

            result = g.answer(int(n))
            if result == 0:
                #步驟四之一：答對
                print("答對！")
                print("你猜了" + str(count) + "次...")
                flag = 1
            elif result == 1:
                print("大一點！")
            elif result == 2:
                print("小一點！")
            else:
                print("不正確的輸入...")

            if flag == 1:
                break

        #步驟四之二：沒有答對
        if flag == 0:
            print("猜了三次也沒猜對，答案是" + str(g.number) + "。")

if __name__ == "__main__":
    CMD.gameloop()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：cmd.py
# 功能：猜數字遊戲的終端機版本
# 作者：張凱慶
