import cv2
import numpy as np

from combat import Combat
from posture import POSTURE


class Show:
    def __init__(self):
        images = [r'img/stone.jpg', r'img/scissor.jpg', r'img/hand.jpg', r'img/unknown.jpg']
        imgs = []
        # 读取图片
        for i in range(len(images)):
            imgs.append(cv2.imread(images[i]))
        self.imgs = imgs
        pass

    # 转场效果，direction为1表示从黑到白，为0反之
    def showTranslation(self, image, direction, text):
        self.showInfo(image, text, org=(130, 250), fontScale=2, color=(255, 255, 255), thickness=4)
        count = 0
        while count == 0:
            load_f = 50
            time = 2
            for t in range(time * 1000 // load_f):  # 间隔
                # self.showInfo(image, text, org=(200, 200), fontScale=2, color=(255, 255, 255), thickness=4)
                sc = 1 - 1 / time * (time * direction + pow(-1, direction) * t * load_f / 1000)
                img_show = cv2.multiply(image, (1, 1, 1, 1), scale=sc)
                cv2.imshow("image", img_show)
                cv2.waitKey(load_f)
                if sc == direction + pow(-1, direction) * 0.125:  # 即将结束
                    count = count + 1
                    break

    # 订帧
    def staticPage(self, image, text):
        load_f = 50
        time = 2
        for t in range(time * 1000 // load_f):  # 间隔
            # self.showInfo(image, text, org=(200, 200), fontScale=2, color=(255, 255, 255), thickness=4)
            # sc = 1 - 1 / time * (time * direction + pow(-1, direction) * t * load_f / 1000)
            img_show = cv2.multiply(image, (0, 0, 0, 0))
            self.showInfo(img_show, text, org=(200, 200), fontScale=2, color=(255, 255, 255), thickness=4)
            cv2.imshow("image", img_show)
            cv2.waitKey(load_f)

    def showWonInfo(self, wonInfo, image):
        # print(wonInfo)
        if wonInfo == Combat.LEFT_WON:
            text = "left won"
        elif wonInfo == Combat.RIGHT_WON:
            text = "right won"
        elif wonInfo == Combat.NECT_TO_NECK:
            text = "    ok"
        else:
            text = "unknow err"
        self.showInfo(image, text, org=(130, 250), fontScale=2, color=(255, 255, 255), thickness=4)
        return text

    # 打印文本信息
    def showInfo(self, image, info, org=(100, 100), fontScale=3, color=(0, 255, 0), thickness=1):
        cv2.putText(image,
                    str(info),
                    org=org,
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=fontScale,
                    color=color,
                    thickness=thickness
                    )

    # 显示出招的图像
    def showFit(self, image, type, status):

        img = self.imgs[type]
        # 是否需要翻转
        if status == POSTURE.RIGHT_HAND:
            img = cv2.flip(img, 1)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # print(gray_logo)
        # 转换成二值图
        # 参数1：被转换的图像
        # 参数2: 阈值(180)
        # 参数3: 大于阈值 就是当前给定的值255
        # 参数4: 阈值类型 cv2.THRESH_BINARY
        retval, binary_img = cv2.threshold(gray_img, 100, 255, cv2.THRESH_OTSU)
        # print(retval)
        # 查找轮廓
        # 参数1：被查找的图像二值图
        # 参数2: 图像轮廓存放规则 RETR_TREE 简单的理解为由外到内 由大到小
        # 参数3：存储轮轮廓的拐角点 CHAIN_APPROX_SIMPLE
        contours, hierarchy = cv2.findContours(binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # 绘制轮廓
        # 情况1: 将轮廓绘制在彩色图像背景上
        # 情况2:将图像绘制在黑色背景上
        mask = np.zeros_like(binary_img)
        # 绘制轮廓
        # cv2.drawContours(mask, contours, 0, color=255, )
        # cv2.drawContours(mask, contours, 0, color=(255, 255, 255), thickness=5)
        # cv2.drawContours(mask, contours, 1, color=(255, 255, 255), thickness=5)
        cv2.drawContours(mask, contours, 1, color=(255, 255, 255), thickness=-1)

        # img需要可以等比例调整 h/w
        ratio = img.shape[0] / img.shape[1]
        fit_w = 100
        fit_h = int(fit_w * ratio)
        # Can't parse 'dsize'. Sequence item with index 1 has a wrong type
        fit_img = cv2.resize(img, dsize=(fit_w, fit_h))
        fit_mask = cv2.resize(mask, dsize=(fit_w, fit_h))

        # 在视频帧上添加图片
        # img_h, img_w, _ = img.shape # 获取图片的高度、宽度和通道数
        rows, cols = np.where(fit_mask == 255)
        if status == POSTURE.LEFT_HAND:
            image[rows + 20, cols + 10] = fit_img[rows, cols]
        else:
            image[rows + 20, cols + 400] = fit_img[rows, cols]

        return image