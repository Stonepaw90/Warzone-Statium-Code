import streamlit as st
import logging

from PIL import Image
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def printit(string, firstlist=[], firstnum=314, secondlist=[], secondnum=314, thirdlist=[], thirdnum=314):
    toprint = ""
    for pos in range(len(string)):
        if pos in firstlist:
            toprint += str(firstnum)
        elif pos in secondlist:
            toprint += str(secondnum)
        elif pos in thirdlist:
            toprint += str(thirdnum)
        else:
            toprint += string[pos]
    st.write(toprint)


def code(string):
    #print(string)
    poslistt = []
    numlist = []
    for m in range(len(string)):
        try:
            numlist.append(int(string[m]))
        except:
            poslistt.append(m)
    if poslistt == []:
        st.write("Your code is already solved!")
        return 0
    #print("letter positions are: \n" + str(poslistt))
    #print("numbers unused are:")
    all10 = list(range(10))
    numleft = set(all10) - set(numlist)
    numleftlist = list(numleft)
    #print(numleftlist)
    NL = []
    AL = []
    SL = []
    counter = [0, 0, 0]
    for i in poslistt:
        b = string[i]
        if b == "N":
            NL.append(i)
            counter[0] = 1
        if b == "S":
            SL.append(i)
            counter[1] = 1
        if b == "H":
            AL.append(i)
            counter[2] = 1
    #print(NL, AL, SL)
    variables = sum(counter)
    #print(variables)
    num_to_try = factorial(len(numleftlist)) / factorial(len(numleftlist) - variables)
    st.header("There are " + str(int(num_to_try)) + " possible codes to try:")
    if st.button("Click here if you want to see all possible codes."):
        if counter[0] == 1:
            firstvar = NL
            if counter[1] == 1:
                secondvar = SL
                if counter[2] == 1:
                    thirdvar = AL
            elif counter[2] == 1:
                secondvar = AL
        elif counter[1] == 1:
            firstvar = SL
            if counter[2] == 1:
                secondvar = AL
        else:
            firstvar = AL

        for i in numleftlist:
            if variables == 1:
                printit(string, firstvar, i)
            else:
                secondl = numleftlist.copy()
                secondl.remove(i)
                for j in secondl:
                    if variables == 2:
                        printit(string, firstvar, i, secondvar, j)
                    else:
                        thirdl = secondl.copy()
                        thirdl.remove(j)
                        for k in thirdl:
                            printit(string, firstvar, i, secondvar, j, thirdvar, k)


def combine(string1, string2):
    pairlist = [[string1[i], string2[i]] for i in range(len(string1))]
    for i in range(len(pairlist)):
        for j in [0, 1]:
            if str(pairlist[i][j]).isdigit():
                pairlist[i][j] = int(pairlist[i][j])
    final = [0] * len(string1)
    keydict = {}
    for i in range(len(pairlist)):
        if type(pairlist[i][0]) == type(pairlist[i][1]):
            final[i] = pairlist[i][0]
        else:
            if str(pairlist[i][0]).isdigit():
                keydict[pairlist[i][1]] = pairlist[i][0]
                final[i] = pairlist[i][0]
            elif str(pairlist[i][1]).isdigit():
                keydict[pairlist[i][0]] = pairlist[i][1]
                final[i] = pairlist[i][1]
    for i in range(len(pairlist)):
        if final[i] in keydict.keys():
            final[i] = keydict[final[i]]
    final = ''.join([str(elem) for elem in final])
    return (final)
def main():
    im = Image.open("enigma.png")
    st.image(im, caption='This Blueprint for the CR-56 AMAX comes after collecting key cards in Stadium.', use_column_width=True)
    st.write("Input your code or codes, with N for the nose symbol, H for the house symbol, \
             and S for the squiggly symbol that looks like a dollar sign. This webapp will crack \
             the code for you and will show you the \
             codes that you should guess.")
    im1 = Image.open("conversions1.png")
    st.image(im1, caption='', width=400)
    user_code2 = ""
    user_code3 = ""
    user_code1 = st.text_input("Input your first code", "Example: 4H8N3SHN")
    user_code2 = st.text_input("Input your second code", "")
    user_code3 = st.text_input("Input your third code if you have one", "")
    if not user_code2:
        finalstring = user_code1
    else:
        string3 = combine(user_code1, user_code2)
        if user_code3:
            finalstring = combine(string3, user_code3)
        else:
            finalstring = string3
    st.header("Your code is: " + finalstring)
    logging.basicConfig(filename='codes.log', encoding='utf-8', level=logging.DEBUG)
    logging.info(user_code1 + " " + usercode_2 + " " + user_code3 + " :" + finalstring)
    
    code(finalstring)
if __name__ == "__main__":
    main()
