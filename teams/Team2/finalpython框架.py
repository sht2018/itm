while (signsmp!=1):
    print("来人玩！")
    signsmp=输入(来自树莓派)#来自树莓派的信号，1为有人，0为没人
#有人就开始

flag1=False#甲方是否布局完成
flag2=False#乙方是否布局完成

while (flag1==False && flag2==False)
    print("放军舰，按键")
    signard1=输入(来自甲方arduino)#来自甲方arduino的信号，1为按下按钮，0为没按
    if (signard1==1):
        pic1=图#甲方摄像头拍摄甲方棋盘布局
        map1=根据pic1生成的二维数组（将图切块，识别各块颜色）
        #mc中建甲方模型
        flag1=True



    print("放军舰，按键")
    signard2=输入(来自乙方arduino)#来自乙方arduino的信号，1为按下按钮，0为没按
    if (signard2==1):
        pic2=图#乙方摄像头拍摄乙方棋盘布局
        map2=根据pic1生成的二维数组
        #mc中建乙方模型
        flag2=True

#初始布局完成



#游戏正式开始
score1=0#甲方分数
score2=0#乙方分数
while (i<=回合数限制):
    #甲方回合
    while (signard1!=1):
        print("扔海绵，按键")
        signard1=输入(来自甲方arduino)
    pic1=图
    #做相应处理，更新map
    positionx=
    positiony=#海绵在棋盘上的位置，如（0，0）；若不在棋盘上（-1，-1）
    bombtype=#0为没扔中，1，2，3为。。类型

    #mc中反应情况

    #arduino提示甲方玩家命中情况及分数



    #乙方回合
    while (signard2!=1):
        print("扔海绵，按键")
        signard1=输入(来自乙方arduino)
    pic2=图
    #做相应处理，更新map
    positionx=
    positiony=#海绵在棋盘上的位置，如（0，0）；若不在棋盘上（-1，-1）
    bombtype=#0为没扔中，1，2，3为。。类型

    #mc中反应情况

    #arduino提示乙方玩家命中情况及分数


    i=i+1#记录回合数


#游戏结束
#告知胜负
