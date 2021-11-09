
import random as r
import random as r
a = ["1","2","3","4","5","6","7","8","9","0","q","w","e","r","t","y","u","i","o","p","a","s",\
     "d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I",\
     "O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
def code():
    mi=""
    global a #全局变量a
    for i in range(8):
        n = r.randint(0,61) # 从a列表中任取一个字符串
        mi = mi + a[n] # 字符串相加得字符串
    return mi
def main():
    for i in range(1,11):
        print("the {} code is {}".format(i,code()))
main()
