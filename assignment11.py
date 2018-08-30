import re
'''
#Question1:->Write a python code to find a valid email address from a text.
'''
#Solution1:->
mailid=str(input("ENTER AN EMAIL ID OF THE USER "))
matcher=re.finditer('\w[_a-zA-Z0-9.]*(@)(gmail.com|yahoo.com)',mailid)
for m in matcher:
    print("Match is at :{},end :{},Pattern found :{}"\
          .format(m.start(),m.end(),m.group()))
#print()


'''
#Question2:->Write a python program to find a valid Indian phone number from a text.
(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )
'''
#Solution2:->
phoneno=input("ENTER PHONE NUMBER OF THE PERSON")
m1=re.finditer('(\+91)[6789]{1}[0-9]{9}',phoneno)
for m in m1:
    print("Match is at :{},end :{},Pattern found :{}"\
          .format(m.start(),m.end(),m.group()))
print()

