import cv2
import mediapipe as mp
import math
from posture import POSTURE


class Hand:

    def __init__(self):
        mp_hands = mp.solutions.hands
        self.hands = mp_hands.Hands()
        self.image = None
        self.leftHandmark = []
        self.rightHandmark = []

    # 获取手部原始
    def getHandsRowInfo(self):
        image = self.image
        hands = self.hands
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = hands.process(image_rgb)
        multi_hand_landmarks = result.multi_hand_landmarks
        if not multi_hand_landmarks:
            return
        # 左右手是否都已经进入视频范围
        if len(multi_hand_landmarks) == 1:
            return
        # 赋值关键点
        # print(multi_hand_landmarks)
        self.leftHandmark = multi_hand_landmarks[0].landmark
        self.rightHandmark = multi_hand_landmarks[1].landmark

    # 获取手指伸屈信息
    def getUpDownInfoOfFinger(self):
        fingerList = [3, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        fingerList_l_y = [0] * 10
        fingerList_r_y = [0] * 10

        leftFingerSignal =  [POSTURE.FINGER_ON] * 5
        rightFingerSignal = [POSTURE.FINGER_ON] * 5

        for index, fingerNum in enumerate(fingerList):
            fingerList_l_y[index] = self.indexCv2Point(fingerNum)[0][1]
            fingerList_r_y[index] = self.indexCv2Point(fingerNum)[1][1]
        for i in range(0, len(fingerList), 2):
            if fingerList_l_y[i] < fingerList_l_y[i + 1]:
                leftFingerSignal[math.floor(i / 2)] = POSTURE.FINGER_DOWN
            if fingerList_r_y[i] < fingerList_r_y[i + 1]:
                rightFingerSignal[math.floor(i / 2)] = POSTURE.FINGER_DOWN

        return leftFingerSignal, rightFingerSignal

    # 处理图片信息
    def processHands(self, image):
        self.leftHandmark = []
        self.rightHandmark = []
        self.image = image
        # 获取手部信息
        self.getHandsRowInfo()
        # 判断是否有数据
        if len(self.leftHandmark) == 0 or len(self.rightHandmark) == 0:
            return [0,0,0,0,0],[0,0,0,0,0]
        leftSignal, rightSignal = self.getUpDownInfoOfFinger()
        # print(leftSignal,rightSignal)
        return rightSignal, leftSignal

    # 获取图片某一像素的位置
    def indexCv2Point(self,fingerNum):
        img_h, img_w = self.image.shape[:2]
        lm = self.leftHandmark[fingerNum]
        rm = self.rightHandmark[fingerNum]
        lm_x = int(lm.x * img_w)
        lm_y = int(lm.y * img_h)
        rm_x = int(rm.x * img_w)
        rm_y = int(rm.y * img_h)
        return (lm_x, lm_y), (rm_x, rm_y)
