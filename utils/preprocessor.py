import cv2
import numpy as np

# TODO: SIFT ALGORITHM - Linrong Jin

# TODO: SaliencyELD Call - Linrong Jin

# TODO: Data Augmentation - Lingkun Li
def rotateImage(image, angle):
    height = image.shape[0]
    width = image.shape[1]
    height_big = height
    width_big = width
    image_big = cv2.resize(image, (width_big, height_big))
    image_center = (width_big/2, height_big/2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image_big, rot_mat, (width_big, height_big), flags=cv2.INTER_LINEAR)
    return result


# flag = 0 / 1 / -1
# 旋转: 垂直/ 水平 / 水平与垂直
def flipImage(image, flag):
    return cv2.flip(image, flag)


def scale(image, multiple, interpolation = None):
    rows, cols, channels = image.shape
    return cv2.resize(image, (int(cols*multiple),int(rows*multiple)), interpolation=interpolation)


def zoom(image, dsize, interpolation = None):
    return cv2.resize(image, dsize, interpolation=interpolation)


def shift(image, x, y):
    M = np.array([[1, 0, x],[0, 1, y]], np.float32)
    rows, cols, channels = image.shape
    return cv2.warpAffine(image, M, (cols,rows))


# 对比度变换
def contrast(image, alpha, beta):
    image = image * alpha + beta
    return image

# size - 噪点数量
def noise(image, size):
    for i in range(0,size):
        xi = int(np.random.uniform(0,image.shape[1]))
        xj = int(np.random.uniform(0,image.shape[0]))
        image[xj,xi] = 255
    return image