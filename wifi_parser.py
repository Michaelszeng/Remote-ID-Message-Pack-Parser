input_string = "50 00 00 00 F4 CE 36 00 14 84 10 91 A8 3B 7D C5 10 91 A8 3B"


SEQUENCE_0D = "00001101"

input_string = input_string.replace(" ", "")
input_string = int("0x" + input_string, 16)  # convert from string into hex object

binary = f'{input_string:0>42b}'  # string of binary


print(binary)

hex = (len(binary) + 3) // 4, int(binary, 2)
print('%0*X' % (hex))
print("0D" in hex)

binary = binary[:-1]
hex = (len(binary) + 3) // 4, int(binary, 2)
print('%0*X' % (hex))
print("0D" in hex)

binary = binary[:-2]
hex = (len(binary) + 3) // 4, int(binary, 2)
print('%0*X' % (hex))
print("0D" in hex)

binary = binary[:-3]
hex = (len(binary) + 3) // 4, int(binary, 2)
print('%0*X' % (hex))
print("0D" in hex)