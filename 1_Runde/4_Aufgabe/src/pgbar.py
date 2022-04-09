from time import time
from sys import stdout
from os import get_terminal_size

def setup(total_, rate_=100):
    global total
    global i
    global starttime
    global percent
    global rate
    rate = rate_
    total = total_
    i = 0
    starttime = time()

def update(i_):
    global total
    global percent
    global rate
    global i
    i = i_
    if i % rate != 0:
        return
    percent = int(i / (total / 100))
    advanced_info = get_advanced_info()
    screen_size = get_terminal_size()[0]
    bar_size_max = screen_size - len(advanced_info) - 1
    percent_multiplier = 0
    bar_size = 0
    if bar_size_max > 0:
        percent_multiplier = bar_size_max / 100
        bar_size = int(percent * percent_multiplier)
    stdout.write("\r{}{}{}".format("█" * bar_size, " " * (bar_size_max - bar_size), advanced_info))
    if percent == 100:
        stdout.write("\n")

def get_advanced_info():
    global percent
    global starttime
    time_ = int(time() - starttime)
    seconds = time_ % 60
    minutes = int((time_ - (time_ % 60)) / 60)
    percent_display = "{}%".format(norm_length(str(percent), 3))
    if percent == 100:
        percent_display = "Done"
    return " {} {}/{} {}:{}".format(percent_display, norm_length(str(i), len(str(total))), total, norm_length(str(minutes), 2, "0"), norm_length(str(seconds), 2, "0"))

def norm_length(text, length, fill_with=" "):
    return fill_with * (length - len(text)) + text
