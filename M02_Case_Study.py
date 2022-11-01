#Write a Python app that will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll. Your app will:
#ask for and accept a student's last name.
#quit processing student records if the last name entered is 'ZZZ'.
#ask for and accept a student's first name.
#ask for and accept the student's GPA as a float.
#test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
#test if the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.

studentFirstName=input(" Enter your first name")
studentLastName=input(" Enter your last name")
GPA=float(input ("Enter your GPA"))

if studentLastName ==("ZZZ"): 
    quit()
    if GPA >=3.5: 
        print(" Congratulations, you've made the Dean's List!")
    if GPA >=3.25:
        print(" Congratulations, you've made the Honor Roll!")

