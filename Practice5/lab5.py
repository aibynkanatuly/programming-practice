# 501
# import re

# txt = input()
# a = re.search("^Hello", txt)
# if a :
#     print("Yes")
# else:
#     print("No")


# 502
# import re

# txt = input()
# txt2 = input()

# a =re.search(txt2, txt)
# if a :
#     print("Yes")
# else:
#      print("No")


# 503
# import re 

# txt = input()
# txt2 = input()
# a = re.findall(txt2, txt)
# print(len(a))


# 504
# import re 

# txt = input()
# digits = re.findall(r"\d", txt)
# print(" ".join(digits))

# 505
# import re 

# txt = input()
# a = re.match(r"^[A-Za-z].*[0-9]$" , txt)
# if a:
#     print("Yes")
# else: 
#     print("No")

import re

s = input()

match = re.search(r"\S+@\S+\.\S+", s)

if match:
    print(match.group())
else:
    print("No email")