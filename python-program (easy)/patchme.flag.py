### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('flag.txt.enc', 'rb').read()

def get_number():
    num_list = [1, 2, 3, 4]
    return sum(num_list) - len(num_list) - num_list[3]

magic = ["9nmbicrizi", "komlkpy7bv", "adfjhgj321", "0o4zpzpwq4", "87e3b1fq4v", "snq73ukmrg", "sleuth9000"]
unmagic = list(reversed(magic))

i = get_number()
j = i % 2

def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "ak98" + \
                   "-=90" + \
                   magic[i] + \
                   unmagic[j]):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return
    print("That password is incorrect")



level_1_pw_check()
