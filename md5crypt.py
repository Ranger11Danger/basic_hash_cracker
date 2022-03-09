#!/usr/bin/python2
from hashlib import md5
			
"""
All comments and steps pulled from from vidarholen.net/contents/blog/?p=32
"""

def md5crypt(password, salt):

    magic = '$1$'
    
    #special base64 characters used for md5 crypt
    itoa64 = './0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    hash_result= password + magic + salt

    final_hash = md5(password + salt + password).digest()
    
    

#    Let password be the users ascii password salt the ascii salt (truncated to 8 chars), and magic the string $1$
#    Start by computing the Alternate sum, md5(password + salt + password)
#    Compute the Intermediate0 sum by hashing the concatenation of the following strings:
#        Password
#        Magic
#        Salt
#        length(password) bytes of the Alternate sum, repeated as necessary
#        For each bit in length(password), from low to high and stopping after the most significant set bit
#            If the bit is set, append a NUL byte
#            If its unset append the first byte of the password

    for i in range(len(password),0,-16):
        if i > 16:
            hash_result= hash_result+ final_hash[:16]
        else:
            hash_result= hash_result+ final_hash[:i]

    i = len(password)
    while i:
        if i & 1:
            hash_result= hash_result+ chr(0)
        else:
            hash_result= hash_result+ password[0]
        i = i >> 1

    final_hash = md5(hash_result).digest()
    
#    For i = 0 to 999 (inclusive), compute Intermediatei+1 by concatenating and hashing the following:
#
#    If i is even, Intermediatei
#    If i is odd, password
#    If i is not divisible by 3, salt
#    If i is not divisible by 7, password
#    If i is even, password
#    If i is odd, Intermediatei
#
#    At this point you dont need Intermediatei anymore. 

# make it run slower...
    for i in range(1000):
        hash_temp = ''
        if i & 1:
            hash_temp = hash_temp + password
        else:
            hash_temp = hash_temp + final_hash[:16]
        if i % 3:
            hash_temp = hash_temp + salt

        if i % 7:
            hash_temp = hash_temp + password

        if i & 1:
            hash_temp = hash_temp + final_hash[:16]
        else:
            hash_temp = hash_temp + password
            
        final_hash = md5(hash_temp).digest()


    
#    Output the magic
#    Output the salt
#    Output a $ to separate the salt from the encrypted section
#    Pick out the 16 bytes in this order: 11 4 10 5 3 9 15 2 8 14 1 7 13 0 6 12.
#        For each group of 6 bits (there are 22 groups), starting with the least significant
#            Output the corresponding base64 character with this index
#
                                
    
    result = ''
    for a, b, c in ((0, 6, 12), (1, 7, 13), (2, 8, 14), (3, 9, 15), (4, 10, 5)):
        v = ord(final_hash[a]) << 16 | ord(final_hash[b]) << 8 | ord(final_hash[c])
        for i in range(4):
            result += itoa64[v & 0x3f]
            v >>= 6

    v = ord(final_hash[11])
    for i in range(2):
        result += itoa64[v & 0x3f]
        v >>= 6


    return magic + salt + '$' + result

#for testing purposes if this script is ran it test our password
#else the function for md5crypt can be imported into our other script
if __name__ == "__main__":
    print(md5crypt("fgobof", "4fTgjp6q"))