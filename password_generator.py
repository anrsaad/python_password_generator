# password generator using python script
# code by : SAAD ANouar
# for my channel : technotech3301   << subscribe Me 

import random, os
from time import sleep

# let make the code more funny
# we gonna add a logo before started of program

logo = f"""

╔═╗╔═╗╔═╗╔═╗╦ ╦╔═╗╦═╗╔╦╗  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗
╠═╝╠═╣╚═╗╚═╗║║║║ ║╠╦╝ ║║  ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝
╩  ╩ ╩╚═╝╚═╝╚╩╝╚═╝╩╚══╩╝  ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═

"""

print(logo)   # now this logo gonna show up before the code

lower_case = "abcdefghijklmnopkrstvwxyzo"
upper_case = lower_case.upper()    # to not repeat the same alphabet
num = "0123456789"
symbols = "-:!%,?é&#'(_èà)@="    # you can add your custimoze symboles here

get_password = lower_case + upper_case + num + symbols


# we gonna give user ability to choose the lenght of password 
lenght = int(input("Enter the lenght of passwords :")) 

print("\n")  # jumping a line here

# we gonna also give user ability to choose the number of password generated
num_password = int(input("Enter the number of password a generated in file :"))

print("\n")  # jumping a line here
# what if we want to write this password into a file 
# we want also give user the choise to name his file 
name = str(input("Enter your password file name :"))
password_name = name+".txt"

with open(password_name, "a") as file :

    for i in range(0, num_password):
        password = "".join(random.sample(get_password, lenght))

        file.write(password+"\n")

# we want also show the file after generated 
# we gonna user the OS module for that

# we gonna adding a Successful message before execute the file 
print("\n\t\t File created Successfuly ")
#also we need a waiting time to read this message before show up the file created
# we gonna use the time module for that
sleep(1) # the program wait 1 second then execute the file
os.system(password_name)

