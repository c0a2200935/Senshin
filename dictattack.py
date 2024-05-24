import crypt
import datetime
now1 = datetime.datetime.now()
password = input()
password = crypt.crypt(password,'')

f = open (dictpasswd.txt,'r')
dictpasswds = f.readlines()
f.close()

for i in range(len(dictpasswds)):
    print(dictpasswds[i])
    if password == crypt.crypt(dictpasswds[i].rstrip('\n'),''):
        print("yes")
        break

now2 = datetime.datetime.now()
print(now1)
print(now2)
