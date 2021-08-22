n=int(input())
word=[]
translate_sen=" "
dic={}
for i in range(n):
    word.append(input().split(' '))
#print(word)
sen=input().split(' ')
for m in range(len(word)):
    #print(len(word))
    dic[word[m][0]]=word[m][1:4]
val=list(dic.values())
for word in sen:
    for key,value in dic.items():
        if word in value:
            index=sen.index(word)
            sen.pop(index)
            sen.insert(index,key)
print(translate_sen.join(sen))





