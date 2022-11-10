import sys
import cv2
import numpy as np

def compass(img, T):

    # Gray-scaling image
    x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Kernel
    K1 = np.array([[-1, 1, 1],
                    [-1, -2, 1],
                    [-1, 1, 1]])

    K2 = np.array([[-1, -1, 1],
                    [-1, -2, 1],
                    [1, 1, 1]])

    K3 = np.array([[-1, -1, -1],
                    [1, -2, 1],
                    [1, 1, 1]])

    K4 = np.array([[1, -1, -1],
                    [1, -2, -1],
                    [1, 1, 1]])

    K5 = np.array([[1, 1, -1],
                    [1, -2, -1],
                    [1, 1, -1]])

    K6 = np.array([[1, 1, 1],
                    [1, -2, -1],
                    [1, -1, -1]])

    K7 = np.array([[1, 1, 1],
                    [1, -2, 1],
                    [-1, -1, -1]])

    K8 = np.array([[1, 1, 1],
                    [-1, -2, 1],
                    [-1, -1, 1]])

    # Konvolusi
    Tr = cv2.filter2D(src=x, ddepth=-1, kernel=K1)
    Tg = cv2.filter2D(src=x, ddepth=-1, kernel=K2)
    S = cv2.filter2D(src=x, ddepth=-1, kernel=K3)
    BD = cv2.filter2D(src=x, ddepth=-1, kernel=K4)
    B = cv2.filter2D(src=x, ddepth=-1, kernel=K5)
    BL = cv2.filter2D(src=x, ddepth=-1, kernel=K6)
    U = cv2.filter2D(src=x, ddepth=-1, kernel=K7)
    TL = cv2.filter2D(src=x, ddepth=-1, kernel=K8)

    # Mencari Kekuatan Tepi Citra
    KT1 = cv2.max(Tr, Tg, S)
    KT2 = cv2.max(KT1, BD, B)
    KT3 = cv2.max(KT2, BL, U)
    KT = cv2.max(KT3, TL)

    # Proses Tresholding
    ret, y = cv2.threshold(KT, T, 255, cv2.THRESH_TOZERO)

    # Display
    Hori = np.concatenate((x, y), axis=1)
    
    cv2.namedWindow("Compass", cv2.WINDOW_NORMAL)
  
    # Using resizeWindow()
    cv2.resizeWindow("Compass", 600, 700)
    
    # Displaying the image
    cv2.imshow("Compass", Hori)

#Input & Driver
x = cv2.imread(sys.path[0]+'\\foto2.jpeg')
compass(x, 128)

cv2.waitKey(0)

cv2.destroyAllWindows()