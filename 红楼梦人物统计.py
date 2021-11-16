import jieba as j
excludes = {"什么","一个","我们","那里","如今","你们","起来","这里","说道",
           "众人","他们","出来","姑娘","知道","自己","一面","只见","两个",
           "怎么","没有","不是","不知","这个","不知","听见","这样","进来",
           "告诉","东西","就是","咱们","回来","夫人","大家","只是","所以",
           "出去","不敢","这些","只得","丫头","不过","的话","一时","不好",
           "鸳鸯","过来","不能","心里","如此","今日","银子","二人","几个",
           "答应","还有","罢了","一回","说话","只管","这么","那边","这话",
           "外头","打发","自然","那些","今儿","听说","小丫头","屋里","奶奶"} 
txt = open("红楼梦.txt", "rb+", ).read()
words  = j.lcut(txt) 
counts = {}
for word in words:
    if len(word) == 1:  
        continue 
    elif word == "王熙凤" or word == "凤姐" or word == "二奶奶" or word== "凤姐儿":
        rword = "王熙凤"
    elif word == "老太太" or word == "史太君" or word == "老祖宗":
        rword = "贾母"
    elif word == "宝钗" or word == "宝姐姐" or word == "宝姑娘":
        rword = "薛宝钗"
    elif word == "太太" or word == "王夫人" :
        rword = "王夫人"
    elif word == "花珍珠" or word =="袭人":
        rword = "花袭人"
    elif word == "湘云" or word == "云儿": 
        rword = "史湘云"
    elif word == "黛玉" or word == "林妹妹" or word == "潇湘妃子": 
        rword = "林黛玉"      
    elif word == "宝玉" or word == "宝二爷": 
        rword = "林宝玉" 
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1 
for word in excludes:
    del(counts[word])
items = list(counts.items()) 
items.sort(key=lambda x:x[1], reverse=True)
for i in range(20):
    word, count = items[i] 
    print ("{0:<10}{1:>5}".format(word, count))
