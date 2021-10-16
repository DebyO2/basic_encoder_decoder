import pyperclip
import string

layout = list("qwertyuiopasdfghjklzxcvbnm")

while True:

    mode = input("mode'encode/encode -c/decode/decode -c': ")

    if mode.startswith('encode'):

        sentance = input("sentance to encode : ").translate(str.maketrans('', '', string.punctuation)).lower().split()

        encoded_sentance = ""

        for i in sentance:
            
            encoded_sentance = encoded_sentance + " " + "".join(layout[0] if h == 'm' else layout[layout.index(h)+1] for j,h in enumerate(i))

        print("Output> ",encoded_sentance.lstrip(' '))

        if mode.endswith('-c'):

            pyperclip.copy(encoded_sentance.lstrip(' '))
            

    if mode.startswith('decode'):

        sentance = input("sentance to decode : ").translate(str.maketrans('', '', string.punctuation)).lower().split()


        decoded_sentance = ""

        for i in sentance:

            decoded_sentance = decoded_sentance + " " + "".join(layout[-1] if h == 'q' else layout[layout.index(h)-1] for j,h in enumerate(i))

        if mode.endswith('-c'):

            pyperclip.copy(encoded_sentance.lstrip(' '))

        print(decoded_sentance.lstrip(' '))
