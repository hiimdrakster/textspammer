from pynput.keyboard import Key, Controller
import time

keyb = Controller()

greeting ='''
    Welcome to text spammer...
        by @hi_im_drakster

    Please, press a key to continue:
    (0)Exit
    (1)Word spam
    (2)Text spam
    '''

def count_down():
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)

def send():
    keyb.press(Key.enter)
    keyb.release(Key.enter)
    time.sleep(0.1)

def wordSpam():
    def output(word,count):
        for i in range(0,count):
            for j in word:   
                keyb.press(j)
                keyb.release(j)
            time.sleep(0.1)
            send()
    
    word = input("Type word: ")
    count = int(input("How many times to spam?: "))
    count_down()
    output(word,count)

def textSpam():
    def convertText(long):
        short = long.split()
        return short

    def output(words):
        for i in words:
            word = i
            for j in word:
                keyb.press(j)
                keyb.release(j)
            time.sleep(0.1)
            send()

    text = input("Introduce text: ")
    count_down()
    textList = convertText(text)
    output(textList)

print(greeting)
option = None
while option!=0:
    option = int(input('Select an option: '))
    if int(option)==1:
        print("-------")
        wordSpam()
    elif int(option)==2:
        print("-------")
        textSpam()

print("Done!")
time.sleep(0.5)
