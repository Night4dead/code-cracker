from sys import exit
from file_reader import readKey

def user_input():
    while True: 
        msg = input("Please enter message to decrypt : ")
        if msg == "":
            print("Enter text ...")
            pass
        else:
            break
    return msg

def decrypt(key, msg):
    result = ""
    for x in msg:
        if x in key:
            result += key[x]
        elif x == " ":
            result += x
        else: 
            print("message contains characters not in the decrypt key : " + x)
            exit()
    return result

def main():
    key = readKey()
    msg = user_input()
    decrypted = decrypt(key, msg)
    print("decrypted message : " + decrypted)
    

if __name__ == "__main__":
    main()