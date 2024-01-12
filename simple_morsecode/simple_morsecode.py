from telemetrix import telemetrix
import sys
import time


CODE = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.',
    'H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.',
    'O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-',
    'V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',
    '0':'-----','1':'.----','2':'..---','3':'...--','4':'....-',
    '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'}

data = []

DIGITAL_PIN = 13
board = telemetrix.Telemetrix()
board.set_pin_mode_digital_output(DIGITAL_PIN)

try:
    choice = input('1 to send some words in morse - 2 to send an entire document: ')
    if choice == "1":
        word = input('Send text in morse code: ').upper()
        for w in word:
            data.append(w)
    elif choice == "2":
        doc = input('Drag and drop a document: ')
        with open(doc, 'r') as file:
            for i in file.read():
                data.append(i.upper())
    else:
        print('Wrong!')

    for x in data:
        print(f'Character: {x}')
        if(x.find(" ")!=-1):
            print('Space character = 7 sec')
            board.digital_write(DIGITAL_PIN, 1)
            spacechar = time.sleep(7)
            board.digital_write(DIGITAL_PIN, 0)
            time.sleep(0.3)
        if x in CODE:
            morse = CODE[x]
            for y in morse:
                if y == '.':
                    print(f'{y} (Dot = 1 sec)')
                    board.digital_write(DIGITAL_PIN, 1)
                    dot = time.sleep(1)
                    board.digital_write(DIGITAL_PIN, 0)
                    time.sleep(0.3)
                if y == '-':
                    print(f'{y} (Dash = 3 sec)')
                    board.digital_write(DIGITAL_PIN, 1)
                    dash = time.sleep(3)
                    board.digital_write(DIGITAL_PIN, 0)
                    time.sleep(0.3)
    print('\nDone')
except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)
