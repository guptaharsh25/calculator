try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

body = Tk();
body.title("Scientific Calculator");

#type of operation
global oprType;
global numReaderStr;
global allClear;
global num;
global num1;

oprType = -1;
num=0;
num1=0;

#String var for numReader
numReaderStr = StringVar();
numReaderStr.set("0");

#Dial
numReader = Entry(body,width=13,exportselection=0,justify="right",bd=5,font="Helvetica 32", textvariable = numReaderStr);

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
add = Button(body, text="+", width=5, height=2, background= "orange", foreground="black", bd=5, font="Helvetica 16 bold",command = lambda: onOprPress(numReader, numReaderStr, 0));
sub = Button(body, text="-", width=5, height=2, background= "orange", foreground="black", bd=5, font="Helvetica 16 bold",command = lambda: onOprPress(numReader, numReaderStr, 1));
mult = Button(body, text="x", width=5, height=2, background= "orange", foreground="black", bd=5, font="Helvetica 16 bold",command = lambda: onOprPress(numReader, numReaderStr, 2));
div = Button(body, text="/", width=5, height=2, background= "orange", foreground="black", bd=5, font="Helvetica 16 bold",command = lambda: onOprPress(numReader, numReaderStr, 3));
equal = Button(body, text="=", width=5, height=2, background= "orange", foreground="black", bd=5, font="Helvetica 16 bold",command = lambda: onEqualPress(numReader, numReaderStr, oprT, num));
clear = Button(body, text="AC", width=17, height=2, background= "orange", foreground="black", bd=5, font="Helvetica 16 bold",command = lambda: onClearPress(numReader, numReaderStr, num, num1));
signChange = Button(body, text="+/-", width=5, height=2, background= "orange", foreground="black", bd=5, font="Helvetica 16 bold",command = lambda: onSignChangePress(numReader, numReaderStr));

#Numbers
num0 = Button(body, text="0", width=10, height=2, background= "black", foreground="white", bd=5, font="Helvetica 16 bold", command = lambda: onNumPress(0, numReader, numReaderStr));
num1 = Button(body, text="1", width=5, height=2, background= "black", foreground="white", bd=5, font="Helvetica 16 bold", command = lambda: onNumPress(1, numReader, numReaderStr));
num2 = Button(body, text="2", width=5, height=2, background= "black", foreground="white", bd=5, font="Helvetica 16 bold", command = lambda: onNumPress(2, numReader, numReaderStr));
num3 = Button(body, text="3", width=5, height=2, background= "black", foreground="white", bd=5, font="Helvetica 16 bold", command = lambda: onNumPress(3, numReader, numReaderStr));
num4 = Button(body, text="4", width=5, height=2, background= "black", foreground="white", bd=5, font="Helvetica 16 bold", command = lambda: onNumPress(4, numReader, numReaderStr));
num5 = Button(body, text="5", width=5, height=2, background= "black", foreground="white", bd=5, font="Helvetica 16 bold", command = lambda: onNumPress(5, numReader, numReaderStr));
num6 = Button(body, text="6", width=5, height=2, background= "black", foreground="white", bd=5, font="Helvetica 16 bold", command = lambda: onNumPress(6, numReader, numReaderStr));
num7 = Button(body, text="7", width=5, height=2, background= "black", foreground="white", bd=5, font="Helvetica 16 bold", command = lambda: onNumPress(7, numReader, numReaderStr));
num8 = Button(body, text="8", width=5, height=2, background= "black", foreground="white", bd=5, font="Helvetica 16 bold", command = lambda: onNumPress(8, numReader, numReaderStr));
num9 = Button(body, text="9", width=5, height=2, background= "black", foreground="white", bd=5, font="Helvetica 16 bold", command = lambda: onNumPress(9, numReader, numReaderStr));

#onButtonPress
def onNumPress(inNum, numReader, numReaderStr):
        currentNum = float(numReaderStr.get());
        if currentNum == 0:
            numReaderStr.set(str(inNum));
        else:
            numConcat = numReaderStr.get();
            numReaderStr.set(numConcat+str(inNum));

def onOprPress(numReader, numReaderStr, oprType):
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

    if (isinstance(answer,float)):
        if (answer.is_integer()):
            numReaderStr.set(str(int(answer)));
        else:
            numReaderStr.set(str(answer));
    else:
        numReaderStr.set(answer);

def onClearPress(numReader, numReaderStr, num, num1):
        numReaderStr.set("0");
        onEqualPress(numReader, numReaderStr, 0, 0);

def onSignChangePress(numReader, numReaderStr):
    checkNum = float(numReaderStr.get());
    if (checkNum.is_integer()):
        checkNum = int(checkNum);
    if checkNum > 0:
        numReaderStr.set("-" + str(checkNum));
    elif checkNum < 0:
        checkNum = checkNum * (-1);
        numReaderStr.set(str(checkNum));


#Add to grid
numReader.grid(row=1, column=0, columnspan=4,ipadx=5);
clear.grid(row=2, columnspan=3,ipadx=9);
add.grid(row=3, column=3);
sub.grid(row=4, column=3);
mult.grid(row=5, column=3);
div.grid(row=6, column=3);
equal.grid(row=6, column=2,ipadx=2);
signChange.grid(row=2, column=3);

num0.grid(row=6,column=0,columnspan=2,ipadx=12);
num1.grid(row=3,column=0,ipadx=2);
num2.grid(row=3,column=1,ipadx=2);
num3.grid(row=3,column=2,ipadx=2);
num4.grid(row=4,column=0,ipadx=2);
num5.grid(row=4,column=1,ipadx=2);
num6.grid(row=4,column=2,ipadx=2);
num7.grid(row=5,column=0,ipadx=2);
num8.grid(row=5,column=1,ipadx=2);
num9.grid(row=5,column=2,ipadx=2);

body.mainloop();
