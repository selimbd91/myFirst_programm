
import numpy as np

class PracticeNumpy:

    def __init__(self):
        pass

    def function1(self):
        print("hello numpy")
        x = np.array([[1,2,3,4,5],[5,6,7,8,9],[10,11,12,13,14]])
        print(x)
        cd = x[2,[0,3,4]]
        dd = x[0,[0,2,4]]
        ee = x[1,
             0:3]
        xxx = np.vstack([dd,ee,cd])
        print(xxx)



def main():
    obj = PracticeNumpy()
    obj.function1()

if __name__ == '__main__':
    main()