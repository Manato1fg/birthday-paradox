import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def main():
    #print("誕生日のパラドックスの検証")
    #print("文字列変換時に制度が失われるのでパーセント表示は厳密な値ではない")
    x = []
    y = []
    a = _factorial(365)
    for i in range(365):
        j = i + 1
        x.append(j)
        b = 365 ** j
        c = _factorial(365 - j)
        d = 1.0 - a / (b * c)
        #print(str(j) + "人の時に一人も誕生日が被らない確率: "+str(d * 100)+"％")
        y.append(d * 100)
    
    plt.plot(x, y)
    plt.title('Birthday Paradox')
    plt.xlabel('Number of people')
    plt.ylabel('Probability of a pair')
    plt.show()

def factorial(x):
    for i in range(x.size):
        x[i] = _factorial(x[i])
    
    return x

def _factorial(x):
    if x == 1:
        return 1
    elif x != 1 and x >= 1:
        return x * _factorial(x - 1)
    else:
        return 1

if __name__ == '__main__':
    main()