
class Elephant:

    def __init__(self, name, age, topics):
        self.name = name
        self.age = age
        self.topics = topics

    def setName(self):
        pass

    def printName(self):
        print(f'my name is :{self.name}')
        print(f'i am a :{self.age} years old')
        print(f'i study in germany and my topics is {self.topics}')

        self.printArray()

    def printArray(self):
        emptyList = []
        for i in range(10):
            emptyList += [i]

        print(emptyList)

    def differentDisplay(self):
        name1, name2 = input("What is your name:").split()
        print(f'my name is {name1} and Your name is {name2}')

    def calculateAverage(self):

        count = 0
        sum = 0
        print(f"please Enter your value:")
        num = input()
        while num.isnumeric():
            num = int(num)
            sum += num
            count +=1
            print(f"please Enter your value:")
            num = input()

        print(f'the average is:{round(sum / count,2)}')


    def slicing(self):

        name = input('Please enter your desired word:').lower()
        print(f'you enter the word is: {name}')
        length = len(name)
        print("The Length is: "+ str(length))
        des = input('Which character you want to search').lower()[0]
        print(des)

    def lengthArgument(self, *boxes):
        #self.name = name
        #self.age = age
        #self.study = study
        #self.department = department
        print('my name is {} and i am a {} years old.i study in {} and my department is:{}'.format(boxes[2], boxes[0], boxes[3],boxes[1]))
        print(boxes)

class SomethingNew(Elephant):

    def __init__(self):
        super().__init__("selim", 22, "cmm")
    def sumNnumber(self):
        total = 0
        i = 1
        nums = int(input("How many number you wanna print:"))
        while i <= 10:
            print(i, end= '+')
            total += i
            i += 1
        print('\b =',total)
    def stringToList(self):
        num = input("Enter the Value:").split(',')
        #num = list(num)
        print(num)
        total = 0
        for i in num:
            total += int(i)
        print("Total number sum is:",total)


def main():

    #obj = Elephant('Selim', '28', 'Digital Signal Processing')
    obj1 = SomethingNew()
    obj1.sumNnumber()
    obj1.stringToList()
    #obj.printName()
    #obj.printArray()
    #obj.differentDisplay()
    #obj.calculateAverage()
    #obj.slicing()
    #obj.lengthArgument(29, "CMM", "selim", "Germany")

if __name__ == '__main__':
    main()
