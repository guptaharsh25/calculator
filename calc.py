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

#Buttons
add = Button(body, text="+", bd=0, command = lambda: onOprPress(numReader, numReaderStr, 0));
sub = Button(body, text="-", bd=0, command = lambda: onOprPress(numReader, numReaderStr, 1));
mult = Button(body, text="x", bd=0, command = lambda: onOprPress(numReader, numReaderStr, 2));
div = Button(body, text="/", bd=0, command = lambda: onOprPress(numReader, numReaderStr, 3));
equal=Button(body, text="=", bd=0, command = lambda: onEqualPress(numReader, numReaderStr, oprT, num));

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

#Add to grid
numReader.grid(row=1, column=0, columnspan=2);
add.grid(row=2, column=0);
sub.grid(row=2, column=1);
mult.grid(row=3, column=0);
div.grid(row=3, column=1);
equal.grid(row=4, columnspan=2);

body.mainloop();
