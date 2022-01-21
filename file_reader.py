import os
from sys import exit

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def check_dir(dir):
    if os.path.isdir(dir):
        return True
    return False

def getDic(content):
    dic = {}
    for i, v in zip(alpha,content):
        dic[v] = i
    return dic

def readKey():
    if check_dir("decryption_key"):
        file = open("decryption_key/key","r")
        content = [ x for x in file.read() if x != " "]
        file.close
        key = getDic(content)
        return key
    else:
        print("Directory 'decryption_key' does not exist, please create it and add 'key' file in it with decryption key")
        exit()