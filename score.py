import cv2

class Score:
    def __init__(self):
        pass

    # 展示分数
    def showScores(self,image,score):
        for index in range(0, len(score), 2):
            left_text = score[index]
            right_text = score[index + 1]
            cv2.putText(image, str(left_text), org=(200, 100), color=(0, 255, 255), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=2, thickness=3)
            cv2.putText(image, str(':'), org=(260, 90), color=(0, 255, 255), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=2, thickness=3)
            cv2.putText(image, str(right_text), org=(300, 100), color=(0, 255, 255), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=2, thickness=3)
