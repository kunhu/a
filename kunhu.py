print("Hello, Python!");


#Kunhu debug 5
print("Kunhu debug 5");

# Kunh debug4
class Demo:
    def setAtt(self, a = 22, b = 33):
        self.a = a
        self.b = b
     
    def do_something(self):
        return self.a + self.b
 
print()
d = Demo()
d.setAtt()
print(d.do_something())
d.setAtt(11, 22)
print(d.do_something())
print()
 
# 《程式語言教學誌》的範例程式
# http://pydoing.blogspot.com/
# 檔名：classdemo.py
# 功能：示範 Python 程式
# 作者：張凱慶
# 時間：西元 2012 年 12 月



# Kunh debug
print()
i = 10 # 設定控制變數
while i > 0:
    # 迴圈工作區
    print(i)
    i -= 1 # 調整控制變數值
print()



#Kunhu debug 2
if 3 > 5: 
    print("Oh! 3 is bigger than 5!")
elif 4 > 5:
    print("Oh! 4 is bigger than 5!")
elif 5 > 5:
    print("Oh! 5 is bigger than 5!")
elif 6 > 5:
    print("Of course, 6 is bigger than 5!")
else:
    print("There is no case :(")

# Kunhu debgug function
def big(a, b):
    if a > b:
        return a
    else:
        return b
 
print()
print(big(33, 22))
print(big("John", "Mary"))
print()
 
# 《程式語言教學誌》的範例程式
# http://pydoing.blogspot.com/
# 檔名：bigdemo.py
# 功能：示範 Python 程式
# 作者：張凱慶
# 時間：西元 2012 年 12 月
