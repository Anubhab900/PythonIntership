from datetime import date

# Getting user input for name , internship role, and today's date
name=input("Enter your name:") 
internshipRole=input("Enter your internship role:")
todaysDate=date.today()

# Displaying the hello world message with user details
print(f"Hello, World! My name is {name}. I am a {internshipRole} intern. Today's date is {todaysDate}.")

