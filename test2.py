import re
s = "b b\naab 123"
m = re.search("(a?)b([^a]*)(a+)b", s)             # ? is zero or one
assert str(type(m)) == "<class 're.Match'>"
assert m.group(0) == "b b\naab"
assert m.group(1) == ""
assert m.group(2) == " b\n"
assert m.group(3) == "aa"