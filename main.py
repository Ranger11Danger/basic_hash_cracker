from itertools import combinations
import string as str_list
import time
seconds = 1
from md5crypt import md5crypt

"""
password is: fgobof
for ease of testing after cracking the password the first time
i placed it at the top of the len4_wordlist.txt file so it cracked faster
during testing
"""
def main(hash):
    
    start_time = time.time()
    count = 0

    #change this tp false if you dont want it to display passwords per second
    show_time = True
    has_shown_time = False

    #print what hash we are checking
    print("Checking passwords agains the hash {}".format(hash))


    #loop through our wordlist files
    #this uses much less memory than generating the possible combinations in memory
    for i in range(1,7):
        print("Checking passwords with a length of {}".format(i))

        #open each file with the 'with' keyword so the file is closed once its done reading
        with open("len{}_wordlist.txt".format(i)) as file:
            for line in file:

                #this is where we check how long the program has been running and update the count
                current_time = time.time()
                elapsed_time = current_time - start_time
                if elapsed_time < 1:
                    count += 1
                #elif to print the count after 1 sencond and to only print it once
                elif show_time == True and has_shown_time == False:
                    print("Checking approximately {} passwords a second!".format(count))
                    has_shown_time = True

                #our custom function that returns the unix md5crypt version of the hash    
                crypt = md5crypt(line.strip(), '4fTgjp6q')

                #test out md5crypt against our teams hash team34:$1$4fTgjp6q$KgIA/01F8iC.q5i4HrZIm0:16653:0:99999:7:::
                if crypt == hash:
                    print("Hash cracked! password='{}'".format(line.strip()))
                    return

#this function requires a lot of memory to run
#specifically the combinations of 4 5 6 length passwords
#I have already generated them once so this is just here to show how I generated the wordlists
def gen_wordlists():
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(1,7):
        combos = combinations(alphabets, i)
        with open("len{}_wordlist.txt".format(i), 'w') as file:
            for combo in combos:
                file.write("{}\n".format(combo))


if __name__ == "__main__":
    main('$1$4fTgjp6q$KgIA/01F8iC.q5i4HrZIm0')