# 2016.4.23
# Python
#file_motion

# Caution:seek_position シークポジション

f = open("py_pra_1.txt","r+")
s = "aaa"
f.write(s)
s = f.read()# nothing 
f.close()
print(s)
