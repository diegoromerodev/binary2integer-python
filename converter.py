def convert(binary_string):
    if(len(binary_string) > 8):
        return "Please enter up to 8 binary digits"
    curr_pos = len(binary_string) - 1
    total = 0
    for char in binary_string:
        if char != '1' and char != '0':
            return "We can only accept a sequence of 0s and 1s."
        total += int(char) * 2 ** curr_pos
        curr_pos -= 1
    return "Your total is %d" % (total,)