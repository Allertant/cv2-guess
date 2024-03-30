import math

import numpy as np


def getAngle(point_1, point_2, point_3):
    """
    根据三点坐标计算夹角
    :param point_1: 点1坐标
    :param point_2: 点2坐标
    :param point_3: 点3坐标
    :return: 返回任意角的夹角值，这里只是返回点2的夹角
    """
    a = math.sqrt(
        (point_2[0] - point_3[0]) * (point_2[0] - point_3[0]) + (point_2[1] - point_3[1]) * (point_2[1] - point_3[1]))
    b = math.sqrt(
        (point_1[0] - point_3[0]) * (point_1[0] - point_3[0]) + (point_1[1] - point_3[1]) * (point_1[1] - point_3[1]))
    c = math.sqrt(
        (point_1[0] - point_2[0]) * (point_1[0] - point_2[0]) + (point_1[1] - point_2[1]) * (point_1[1] - point_2[1]))
    A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
    B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
    C = math.degrees(math.acos((c * c - a * a - b * b) / (-2 * a * b)))

    return B

def get_angle_v2(a, b, c):
    '''
    计算角度
    :param a:
    :param b:
    :param c:
    :return:
    '''

    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    if angle > 180.0:
        angle = 360 - angle
    return angle


def angle_test():
    a = np.array([0, 30, 45, 60, 90])
    print('不同角度的正弦值：')
    # 通过乘 pi/180 转化为弧度
    print(np.sin(a * np.pi / 180))
    print('数组中角度的余弦值：')
    print(np.cos(a * np.pi / 180))
    print('数组中角度的正切值：')
    print(np.tan(a * np.pi / 180))


def get_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])






