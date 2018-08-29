'''
#Question1:->Write a python code to find a valid email address from a text.
'''
#Solution1:->
\w[_a-zA-Z0-9.]*(@)(gmail.com|yahoo.com)
print()

'''
#Question2:->Write a python program to find a valid Indian phone number from a text.
(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )
'''
#Solution2:->
(+91)^[6-9][0-9]{9}
print()
