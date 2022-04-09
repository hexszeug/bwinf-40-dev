import ascii_box
from ssncode import SSN_CODE

def generate_ascii_display(num, bolds = [], max_width = 70):
    num = num[:]
    lines = ["", "", ""]
    result = ""
    for pointer, digit in enumerate(num):
        ssn = [((digit >> x) & 0b1) for x in range(7)]
        ssn.reverse()
        for bold in bolds:
            if pointer == bold[0] and ssn[6 - bold[1]] == 1: ssn[6 - bold[1]] = 2
        pixels = [None] * 9
        for pixel in range(9):
            value = [0, 0, 0, 0]
            if pixel in [1, 4, 7]: value = [0, ssn[pixel-1], 0, ssn[pixel-1]]
            if pixel == 3: value = [ssn[1], ssn[3], ssn[4], 0]
            if pixel == 5: value = [ssn[2], 0, ssn[5], ssn[3]]
            if pixel == 0: value = [0, ssn[0], ssn[1], 0]
            if pixel == 2: value = [0, 0, ssn[2], ssn[0]]
            if pixel == 6: value = [ssn[4], ssn[6], 0, 0]
            if pixel == 8: value = [ssn[5], 0, 0, ssn[6]]
            pixels[pixel] = ascii_box.generate_pixel(value)
        lines[0] += "".join(pixels[0:3])
        lines[1] += "".join(pixels[3:6])
        lines[2] += "".join(pixels[6:9])
        if max_width - len(lines[0]) < 3:
            result += f"\n{lines[0]}\n{lines[1]}\n{lines[2]}"
            lines = ["", "", ""]
    return result + f"\n{lines[0]}\n{lines[1]}\n{lines[2]}"

def generate_ascii_display_from_bin_num(num, bolds = [], max_width = 70):
    return generate_ascii_display([SSN_CODE[x] for x in num], bolds, max_width)