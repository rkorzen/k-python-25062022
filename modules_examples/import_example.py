import mod

mod.foo("1")


from mod import foo as f1
from mod1 import foo as f2

f1("10")
f2("10")

