### 基于 cv2 + numpy + mediapipe 的图像智能识别项目

### 环境说明（建议使用 anaconda 环境）
在安装完 pycharm 和 anaconda 之后，在命令行中装配环境
```bash
# 创建名为 python37 的环境
conda create -n python37 python=3.7
# 终端激活当前环境
 conda activate python37
# 安装 cv2 环境
pip install opencv-python==4.5.5.64 -i https://mirrors.aliyun.com/pypi/simple
# 安装 opencv 扩展
pip install opencv-contrib-python==4.5.5.564 -i https://mirrors.aliyun.com/pypi/simple
```
到 pycharm 中引入当前的 anaconda 环境，并编写如下代码测试是否安装成功
```python
import cv2
print(cv2.__version__)
```
### 下载工具库
```bash
pip install numpy
pip install mediapipe
```

### 运行
找到 Mian.py，点击运行即可
