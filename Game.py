import random
l1=[i for i in range(1,101)]
number1=random.choice(l1)

class find_number:
    def __init__(self,number1):
        self.number1 = number1  
    def search(self):
        ####
        while True:
            print('_-_'*20,'\n','='*60,'\n','--->      '*4,'\n','='*60,'\n','_-_'*20)
            
            l2=[i for i in range(1,7)]### Make Level Harder
            number2=random.choice(l2)####
            l3=[i for i in range(15,0,-2)]####
            number3=random.choice(l3)####

            input1=int(input('Enter number between 0 to 100 : '))

            # print('number=',self.number1,'    difference=',number2,number3)#### Only for devloper..testing purpose.

            add=abs(self.number1+number2)
            sub=abs(self.number1-number3)

            if add>100:
                add=100

            if number1==input1:
                print('\n'*4,'='*79)
                print('_-_'*26,'\n'*4)
                print('                                                                       O     |\  ')
                print('                                                                      /|\    |_\  ')
                print('                                                                     / | \   |   ')
                print('______________________________________________________________________/_\____|_')
                print(f'NUMBER {input1} IS THE RIGHT ANS... MISSION COMPLETED....__________________/___\_____')
                print('_______________________________________________________________________________ ')

                print('\n'*4,'_-_'*26)
                print('='*79)
                print('\n'*4)
                quit()

            elif(input1>=(self.number1+7)) or (input1<=(self.number1-7)):
                print(f'You are "so long" to Win this game')
                print(f'it is between  {sub} to {add}')

            elif (input1==(self.number1+5)) or (input1==(self.number1-5)) or (input1==(self.number1+6)) or (input1==(self.number1-6)):
                print(f'You are "little bit longer" to Win this game')
                print(f'it is between  {sub} to {add}')

            elif (input1==(self.number1+2)) or (input1==(self.number1-2)) or (input1==(self.number1+3)) or (input1==(self.number1-3)) or (input1==(self.number1+4)) or (input1==(self.number1-4)):
                print(f'You are "closer" to Win this game')
                print(f'it is between  {sub} to {add}')

            elif (input1==(self.number1+1)) or (input1==(self.number1-1)):
                print(f'You are "Closest" to Win')
                print(f'it is between  {sub} to {add}')
                
            print('='*60)

game=find_number(number1)
game.search()
