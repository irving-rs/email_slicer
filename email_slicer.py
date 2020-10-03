#email_slicer.py
#Date: 03/October/2020
#by irving-rs


#DESCRIPTION:
#Email-Slicer: A program that extracts the username and domain from an email.


#DETAILS:
#The user will be asked to enter his/her email address.
#The program will format the input (to prevent some errors).
#The program returns the username and domain.


#FUNCTIONS:
def email_slicer(mail): #Returns te username and domain. Identifies the @ symbol as a separator.
    mail = mail.strip(" .") #Formatting. In case the beginning or trailing characters include " " or "."
    username = mail[:mail.index("@")]
    domain = mail[mail.index("@")+1:]
    return username, domain


#PRESENTATION:
print("\nEMAIL SLICER:")
print("\nSlices an email int two parts: username and domain.\n")


#INSTRUCTIONS:
email = input("Enter your email: ")


#BODY:


if "@" in  email:
    username, domain = email_slicer(email)
    print("\nUser name:", username)
    print("Domain:", domain, "\n")
    print("The username '{}' is in the '{}' domain.\n".format(username, domain))
else:
    print("\nInvalid address.\n")
    




