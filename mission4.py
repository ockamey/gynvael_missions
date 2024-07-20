# Mission4 https://www.youtube.com/watch?v=kZtHy9GqQ8o

message_hexstring = """E0 81 8F 76 65 72 C1 AC E0 81 AF E0 81 AE C1 A7
                       E0 80 A0 E0 81 95 C1 94 E0 81 86 2D E0 80 B8 E0
                       80 A0 F0 80 81 B7 C1 A1 73 20 C1 B3 F0 80 81 B5
                       63 C1 A8 20 E0 81 A1 F0 80 80 A0 E0 81 A6 F0 80
                       81 B5 F0 80 81 AE 20 E0 81 A6 E0 81 A5 F0 80 81
                       A1 C1 B4 75 E0 81 B2 E0 81 A5 F0 80 80 AE"""

message_bytes = bytes.fromhex(message_hexstring)
ascii_message = []

for i in range(len(message_bytes)):
    if message_bytes[i] <= 0x7F:
        ascii_message.append(message_bytes[i])
        i += 1
    elif (message_bytes[i] & 0b11100000) == 0b11000000:
        char_bin = bin(message_bytes[i])[5:] + bin(message_bytes[i+1])[4:]
        ascii_message.append(int(char_bin, 2))
        i += 2
    elif (message_bytes[i] & 0b11110000) == 0b11100000:
        char_bin = bin(message_bytes[i])[6:] + bin(message_bytes[i+1])[4:] + bin(message_bytes[i+2])[4:]
        ascii_message.append(int(char_bin, 2))
        i += 3
    elif (message_bytes[i] & 0b11111000) == 0b11110000:
        char_bin = bin(message_bytes[i])[7:] + bin(message_bytes[i+1])[4:] + bin(message_bytes[i+2])[4:] + bin(message_bytes[i+3])[4:]
        ascii_message.append(int(char_bin, 2))
        i += 4

print(bytes(ascii_message).decode())
