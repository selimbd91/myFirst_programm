import numpy as np
class Practice:

    def __init__(self):
        pass
    def practiceNumpy(self):

        #xx = np.linspace(1,20, 20,dtype= "int16")
        file = np.genfromtxt("hello.txt",delimiter= ",")
        print(file)

def main():
    obj = Practice()
    obj.practiceNumpy()


if __name__ == "__main__":
    main()
