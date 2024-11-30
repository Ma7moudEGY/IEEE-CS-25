shift = input("")
blind_txt = input("")

def OriginalText(text):
    orignal = []
    keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"

    for i in range(len(text)):
        if shift == "R":
            j = keyboard.index(text[i])
            orignal.append(keyboard[j-1])

        else:
            j = keyboard.index(text[i])
            orignal.append(keyboard[j+1])

    print(''.join(orignal))

OriginalText(blind_txt)