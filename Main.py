import cv2
from combat import Combat
from  hand import Hand
from show import Show
from score import Score
from posture import POSTURE
import winsound

# 创建一个视频采集器
# 0表示当前电脑的摄像头序号 外接头像 1, 2
# 地址:播放视频
cap = cv2.VideoCapture(0)
# 创建对象
combat = Combat()
hand = Hand()
show = Show()
score = Score()
scoreInfo = [0,0]
frames = 0
wonInfo = 0
leftHandSignal = 0
rightHandSignal = 0
status = 0
victoryText = ""
# 读取图像
while cap.isOpened():
    # retval 读取图像是否成功
    # image 读取的图像
    retval, image = cap.read()
    if not retval:
        print('can not read image')
        break
    # 将图像进行水平翻转
    image = cv2.flip(image,1)


    if status == 0:
        winsound.PlaySound(r"music/start.wav", winsound.SND_FILENAME)
        show.showTranslation(image,1,"game start")
        status = 1

    if scoreInfo[0]==3 or scoreInfo[1]==3:
        if scoreInfo[0] == 3:
            victoryText = "left won"
        else:
            victoryText = "right won"
        status = 2
    if status == 2:
        # 终了
        show.showTranslation(image, 0,"game over!")
        winsound.PlaySound(r"music/win.wav", winsound.SND_FILENAME)
        show.staticPage(image,victoryText)
        # 清空评分
        scoreInfo = [0,0]
        # 清空胜负情况
        wonInfo = 0
        # 回到游戏开始
        status = 0


    if frames%50 == 0:
        # 获取手部姿势信息
        leftHandSignal, rightHandSignal = hand.processHands(image)
        # print(leftHandSignal,rightHandSignal)
        wonInfo = combat.combat([leftHandSignal, rightHandSignal], scoreInfo)

    show.showWonInfo(wonInfo, image)
    score.showScores(image, scoreInfo)

    # 展示左手的手势
    show.showFit(image,combat.getPosture(leftHandSignal),POSTURE.LEFT_HAND)
    # 展示右手的手势
    show.showFit(image,combat.getPosture(rightHandSignal),POSTURE.RIGHT_HAND)

    cv2.imshow("image", image)
    key = cv2.waitKey(25)
    frames += 1
    # 显示时间，利用帧数u
    if key == ord('q'):
        break
# 释放资源
cap.release()
# 销毁窗口
cv2.destroyAllWindows()
