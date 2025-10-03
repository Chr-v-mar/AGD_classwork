

def cipher(message,shift):
    message = f"{message}"
    message = message.lower()
    test_shift = str(shift)
    codedmessage = ""
    if test_shift.lstrip('-').isdigit():
        shift = shift//1
        for letter in message:
            if letter in "abcdefghijklmnopqrstuvwxyz":
                num = ord(letter)
                num = num + shift
                if num > ord("z"):
                    num = num - 26
                char = chr(num)
                codedmessage += char
            else:
                codedmessage += letter
        return codedmessage
    else:
        raise TypeError("Shift must be an integer")

cipher("hello",5000)