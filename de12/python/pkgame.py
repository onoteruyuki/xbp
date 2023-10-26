print("PKゲームへようこそ！")
name=input("プレイヤー名を入れてください")
print(name,"さんはキッカーです。")
point=0


for i in range(1,6):
    print(i,"回目")
    print("１．右　２．真ん中　３．左")
    select=int(input("コースを数字で選んでね"))
    
    import random
    a = random.randint(1,3)
    print("キーパーはが選んだのは",a)
    if select==a:
        print("止められた...") 
    else:
        print("ナイスシュート！")
        point=point+1

if point>=4:
    print(name,"さんの結果は",point,"点獲得で勝利！")
elif point<=3:
    print(name,"さんの結果は",point,"点獲得で敗北...")
        



