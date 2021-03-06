try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

body = Tk();

#type of operation
global oprType;
global numReaderStr;
global allClear;
global num;
global num1;

oprType = -1;

#String var for numReader
numReaderStr = StringVar();
numReaderStr.set("0");

#Dial
numReader = Entry(body,width=50,exportselection=0,justify="right",bd=0,textvariable = numReaderStr);

#onButtonPress
def onOprPress(numReader, numReaderStr, oprType):
    print ("Click!");
    global num;
    global oprT;
    num = float(numReader.get());
    oprT = oprType;
    numReaderStr.set("0");

    return numReaderStr;

def onEqualPress(numReader, numReaderStr, oprType, num):
    num1 = float(numReader.get());
    global answer;

    if (oprType == 0):
        answer = num + num1;
        oprType = -1;
    elif (oprType == 1):
        answer = num - num1;
        oprType = -1;
    elif (oprType == 2):
        answer = num * num1;
        oprType = -1;
    elif (oprType == 3):
        if (num1 == 0):
            answer = "Error: Cannot divide by 0.";
            oprType = -1;
        else:
            answer = num / num1;
            oprType = -1;
    else:
        answer = "Error!";

    if (type(answer) == 'float'):
        numReaderStr.set(str(answer));
    else:
        numReaderStr.set(answer);

#Buttons
add = Button(body, text="+", bd=0, command = lambda: onOprPress(numReader, numReaderStr, 0));
sub = Button(body, text="-", bd=0, command = lambda: onOprPress(numReader, numReaderStr, 1));
mult = Button(body, text="x", bd=0, command = lambda: onOprPress(numReader, numReaderStr, 2));
div = Button(body, text="/", bd=0, command = lambda: onOprPress(numReader, numReaderStr, 3));
equal = Button(body, text="=", bd=0, command = lambda: onEqualPress(numReader, numReaderStr, oprT, num));
clear = Button(body, text="AC", bd=0, command = lambda: onClearPress(numReader, numReaderStr, num, num1));

#Numbers
num0 = Button(body, text="0", bd=0, command = lambda: onNumPress(0, numReader, numReaderStr));
num1 = Button(body, text="1", bd=0, command = lambda: onNumPress(1, numReader, numReaderStr));
num2 = Button(body, text="2", bd=0, command = lambda: onNumPress(2, numReader, numReaderStr));
num3 = Button(body, text="3", bd=0, command = lambda: onNumPress(3, numReader, numReaderStr));
num4 = Button(body, text="4", bd=0, command = lambda: onNumPress(4, numReader, numReaderStr));
num5 = Button(body, text="5", bd=0, command = lambda: onNumPress(5, numReader, numReaderStr));
num6 = Button(body, text="6", bd=0, command = lambda: onNumPress(6, numReader, numReaderStr));
num7 = Button(body, text="7", bd=0, command = lambda: onNumPress(7, numReader, numReaderStr));
num8 = Button(body, text="8", bd=0, command = lambda: onNumPress(8, numReader, numReaderStr));
num9 = Button(body, text="9", bd=0, command = lambda: onNumPress(9, numReader, numReaderStr));

#onButtonPress
def onNumPress(inNum, numReader, numReaderStr):
    currentNum = float(numReaderStr.get());
    if currentNum == 0:
        numReaderStr.set(str(inNum));
    else:
        numConcat = numReaderStr.get();
        numReaderStr.set(numConcat+str(inNum));

def onOprPress(numReader, numReaderStr, oprType):
    print ("Click!");
    global num;
    global oprT;
    num = float(numReader.get());
    oprT = oprType;
    numReaderStr.set("0");

    return numReaderStr;

def onEqualPress(numReader, numReaderStr, oprType, num):
    global num1;
    num1 = float(numReader.get());
    global answer;

    if (oprType == 0):
        answer = num + num1;
    elif (oprType == 1):
        answer = num - num1;
    elif (oprType == 2):
        answer = num * num1;
    elif (oprType == 3):
        if (num1 == 0):
            answer = "Error: Cannot divide by 0.";
        else:
            answer = num / num1;
    else:
        answer = "Error!";

    if (type(answer) == 'float'):
        numReaderStr.set(str(answer));
    else:
        numReaderStr.set(answer);

def onClearPress(numReader, numReaderStr, num, num1):
        numReaderStr.set("0");
        onEqualPress(numReader, numReaderStr, 0, 0);


#Add to grid
numReader.grid(row=1, column=0, columnspan=4);
clear.grid(row=2, columnspan=3);
add.grid(row=2, column=3);
sub.grid(row=3, column=3);
mult.grid(row=4, column=3);
div.grid(row=5, column=3);
equal.grid(row=6, column=3);

num0.grid(row=6,column=1);
num1.grid(row=3,column=0);
num2.grid(row=3,column=1);
num3.grid(row=3,column=2);
num4.grid(row=4,column=0);
num5.grid(row=4,column=1);
num6.grid(row=4,column=2);
num7.grid(row=5,column=0);
num8.grid(row=5,column=1);
num9.grid(row=5,column=2);

body.mainloop();
