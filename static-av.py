import hashlib
import os

def file_as_bytes(file):
    with file:
        return file.read()

print("Welcome to static-av 1.0")

virus_file_name = input("File Name (with extension): ")
hashlist_file_name = input("Hash list file name : ")
virus_signature = hashlib.md5(file_as_bytes(open(virus_file_name, 'rb'))).hexdigest()

with open(hashlist_file_name , 'r') as scan:

    for sign in scan:
        
        os.system("clear")
        print("Comparing - > " , virus_signature ,"with", sign)

        if (virus_signature == sign):

            print("Signature Match. Exitting...")
            quit()
            
        
    print("File is not Malicious. Exitting...")
    quit()

