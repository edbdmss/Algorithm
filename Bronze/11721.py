word = input().rstrip()
ct = 0
for i in word:
    print(i,end="")
    ct +=1
    if ct%10==0 :
        print()