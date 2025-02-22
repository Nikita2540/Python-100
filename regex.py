import re

Date_1 = input("What's your date of birth? ").strip()

if re.search(r"^(0[1-9]|[12][0-9]|3[0-1])[./-](0[1-9]|1[0-2])[./-][0-9]{4}$", Date_1):
    print("Valid")
else:
    print("Invalid")


