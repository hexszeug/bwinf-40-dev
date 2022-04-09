import ascii_box

SSN_CODE = [0b1110111, 0b0010010, 0b1011101, 0b1011011, 0b0111010, 0b1101011, 0b1101111, 0b1010010, 0b1111111, 0b1111011, 0b1111110, 0b0101111, 0b1100101, 0b0011111, 0b1101101, 0b1101100]

def generate_ascii_display(num, bolds = []):
    num = num[:]
    num.reverse()
    lines = ["", "", ""]
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
        lines[0] = "".join(pixels[0:3]) + lines[0]
        lines[1] = "".join(pixels[3:6]) + lines[1]
        lines[2] = "".join(pixels[6:9]) + lines[2]
    return f"{lines[0]}\n{lines[1]}\n{lines[2]}"
