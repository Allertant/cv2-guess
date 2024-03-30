from posture import POSTURE

class Combat:
    """
        1 左边赢了
        2 右边赢了
        3 错误
        0 平局
    """
    # 静态变量
    NECT_TO_NECK = 0
    LEFT_WON = 1
    RIGHT_WON = 2
    ERR_WON = 3

    def __init__(self):
        pass

    # battle
    def combat(self,handsInfo,scoreInfo):
        leftHandPosture = self.getPosture(handsInfo[0])
        rightHandPosture = self.getPosture(handsInfo[1])
        # print(leftHandPosture,rightHandPosture)
        return self.calCombat(leftHandPosture,rightHandPosture,scoreInfo)
        pass

    # 判断是什么姿势
    def getPosture(self,data):
        if data[1]==POSTURE.FINGER_DOWN \
            and data[2]==POSTURE.FINGER_DOWN \
            and data[3]==POSTURE.FINGER_DOWN \
            and data[4]==POSTURE.FINGER_DOWN:
            return POSTURE.STONE_SIGNAL
        elif data[1]==POSTURE.FINGER_ON \
            and data[2]==POSTURE.FINGER_ON \
            and data[3]==POSTURE.FINGER_DOWN \
            and data[4]==POSTURE.FINGER_DOWN:
            return POSTURE.SCISSOR_SIGNAL
        elif data[1]==POSTURE.FINGER_ON \
            and data[2]==POSTURE.FINGER_ON \
            and data[3]==POSTURE.FINGER_ON \
            and data[4]==POSTURE.FINGER_ON:
            return POSTURE.MAP_SIGNAL
        else:
            return POSTURE.ERR_SIGNAL

    # 判断谁赢了
    """
        left right
        0   0
        1   1
        2   2
    """
    def calCombat(self, left, right,scoreInfo):
        if left==POSTURE.ERR_SIGNAL or right==POSTURE.ERR_SIGNAL:
            return self.ERR_WON
        # print(left,right)
        elif left == right:
            return self.NECT_TO_NECK
        elif left==POSTURE.SCISSOR_SIGNAL and right==POSTURE.MAP_SIGNAL or \
            left==POSTURE.STONE_SIGNAL and right==POSTURE.SCISSOR_SIGNAL or \
            left==POSTURE.MAP_SIGNAL and right==POSTURE.STONE_SIGNAL:
            scoreInfo[0] += 1
            return self.LEFT_WON
        elif right==POSTURE.SCISSOR_SIGNAL and left==POSTURE.MAP_SIGNAL or \
            right==POSTURE.STONE_SIGNAL and left==POSTURE.SCISSOR_SIGNAL or \
            right==POSTURE.MAP_SIGNAL and left==POSTURE.STONE_SIGNAL:
            scoreInfo[1] += 1
            return self.RIGHT_WON