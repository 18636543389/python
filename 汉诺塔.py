def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
a = input('请输入A柱盘子的个数：')
num = int(a)
print('把',num,'个盘子全部移到C柱子的顺序为：')
move(num, 'A', 'B', 'C')
