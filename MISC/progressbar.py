# COPYRIGHT 2022 MATT SERDUKOFF
# simple simulation of a download progress bar
# just a small fun little coding project

import random
import time

# define the bar
BAR = chr(9608) # 9608 is the black square char

def main():
    print('Progress Bar Simulation by Matt Serdukoff\n\n')
    print('Progress:')
    bytes_done = 0
    download_size = 5096
    while bytes_done < download_size:
        bytes_done += random.randint(0,100)
        bar_string = getProgress(bytes_done, download_size)
        print(bar_string, end='', flush = True)
        time.sleep(0.2)
        print('\b' * len(bar_string), end='', flush = True)

def getProgress(barProgress, total, barWidth = 50):
    progress_bar = ''
    progress_bar += '['
    if barProgress > total:
        barProgress = total
    if barProgress < 0:
        progress = 0
    numBars = int((barProgress / total) * barWidth)
    progress_bar += BAR * numBars
    progress_bar += ' ' * (barWidth - numBars)
    progress_bar += ']'
    completion = round(barProgress / total * 100, 1)
    progress_bar += ' ' + str(completion) + '%'
    progress_bar += ' ' + str(barProgress) + '/' + str(total)

    return progress_bar

if __name__ == '__main__':
    main() 
