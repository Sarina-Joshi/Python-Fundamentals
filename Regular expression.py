'''import re
pattern = r"eggs"
if re.match(pattern, "eggs"):
    print("Match found")
else:
    print("No match found")
if re.search(pattern, "eggsnoteggs"):
    print("Match found")
else:
    print("No match found")
print(re.findall(pattern, "eggsnoteggs"))

import  re
string = "My name is Sam and I am 12 years old"
pattern = r"Sam"
newstring = re.sub(pattern, "Rob", string)
print(newstring)'''

# Dot Metacharacter
'''import re
pattern = r"solve"
if re.match(pattern, "solve"):
    print("Pattern found")'''
# Caret dollar metacharacter
'''import re
pattern = r"^gre.t$"# URl pattern specify garna

if re.match(pattern, "great"):
    print("Match 1")'''
# Character Class
'''
import re
pattern = r"[A-Z][A-Z][0-9]"
if re.search(pattern, "LL2 "):
    print("Match found")'''
# Group
import re
pattern = r"school(class)*college"
if re.match(pattern, "schoolclassclassclasscollege"):
    print("Match found!!!")