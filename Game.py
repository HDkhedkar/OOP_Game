import random
l1=[i for i in range(1,101)]
number1=random.choice(l1)

class find_number:
    def __init__(self,number1):
        self.number1 = number1  
    def search(self):
        try:
            print('\n'*4)
            input2=int(input('''   Select Mode  
                                    Enter 1->Normal
                                    Enter 2->Harder
                                    Enter 3->Hardest :'''))
        except:
            print('\n'*3)
            print('Please read "Menu" carefully and then Enter..."-_-"')
            print('\n'*3)
            print('|\|---O---|/|')
            print('|\|--/|\--|/|')
            print('|\|--\| \-|/|')
            print('|\|__/_\__|/| X X X X X X This is Wrong Way..."-_-"')
            print('\n'*3)


            print('____1___________GAME START HERE  -->  -->')
            print('____2___________GAME START HERE  -->  -->')
            print('____3___________GAME START HERE  -->  -->')

            game.search()



        while True:
            if (input2 > 3) or (input2 < 0):####456789..-1-2-3-4-5...X X X X
                print('\n'*3)
                print('Please read "Menu" carefully and then Enter..."-_-"')
                print('\n'*3)
                print('|\|---O---|/|')
                print('|\|--/|\--|/|')
                print('|\|--\| \-|/|')
                print('|\|__/_\__|/| X X X X X X This is Wrong Way..."-_-"')
                print('\n'*3)

                print('____1___________GAME START HERE  -->  -->')
                print('____2___________GAME START HERE  -->  -->')
                print('____3___________GAME START HERE  -->  -->')
                game.search()

            print('_-_'*20,'\n','='*60,'\n','--->      '*4,'\n','='*60,'\n','_-_'*20)

            if input2==1:###### Make Level Harder
                end=10
                step=1
            elif input2==2:
                end=15
                step=2
            elif input2==3:
                end=20
                step=3

            l2=[i for i in range(1,end,step)]### Make Level Harder
            number2=random.choice(l2)####
            l3=[i for i in range(end,5,-step)]####
            number3=random.choice(l3)####

            input1=int(input('Enter number between 0 to 100 : '))

            # print('number=',self.number1,'    difference=',number2,number3)#### Only for devloper..testing purpose.

            add=abs(self.number1+number2)
            sub=abs(self.number1-number3)
            
            if (self.number1-number3)<0:
                sub=0

            if add>100:
                add=100

            if number1==input1:
                print('\n'*4,'='*79)
                print('_-_'*26,'\n'*4)
                print('                                                                       O     |\  ')
                print('                                                                      /|\    |_\  ')
                print('                                                                     / | \   |   ')
                print('______________________________________________________________________/_\____|_')
                print(f'You are "Winner" and You are Selected for "Next Level" ....__________/___\_____')
                print('_______________________________________________________________________________ ')

                print('\n'*4,'_-_'*26)
                print('='*79)
                print('\n'*4)
                                
                input2+=1
                if input2>3:
                    print('='*20,'Game Over','='*20)
                    quit()

            elif(input1>=(self.number1+7)) or (input1<=(self.number1-7)):### Make Level Harder
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
                
game=find_number(number1)
game.search()
