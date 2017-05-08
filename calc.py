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

"""
def checkClear(numReaderStr):
    pullText = numReaderStr.get();
    if pullText != "0":
        equal.config(text="C");
"""


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
numReader.grid(row=1, column=0, columnspan=2);
clear.grid(row=2, columnspan=2);
add.grid(row=3, column=0);
sub.grid(row=3, column=1);
mult.grid(row=4, column=0);
div.grid(row=4, column=1);
equal.grid(row=5, columnspan=2);

body.mainloop();
