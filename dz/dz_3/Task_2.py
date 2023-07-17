text = "While The Python Language Reference describes the exact syntax and semantics " \
       "of the Python language, this library reference manual describes the standard " \
       "library that is distributed with Python. It also describes some of the optional " \
       "components that are commonly included in Python distributions."

text_list = text.lower().split()

text_dict = {}

for i in text_list:
    cl = i.strip(".,!:;")
    if cl not in text_dict:
        text_dict[cl] = 1
    else:
        text_dict[cl] += 1

print(text_dict)

result = dict(sorted(text_dict.items(), key=lambda x: x [1], reverse = True))
print(result)