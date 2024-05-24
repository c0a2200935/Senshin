import crypt
import datetime
now1 = datetime.datetime.now()
password = input()
password = crypt.crypt(password,'')

f = open (passphrase.txt,'r')
dictpasswds = f.readlines()
f.close()

for i in range(len(dictpasswds)):
    for j in range(len(dictpasswds)):
        for s in range(len(dictpasswds)):
            for t in range(len(dictpasswds)):
                d = dictpasswds[i].rstrip('\n') + dictpasswds[j].rstrip('\n') + dictpasswds[s].rstrip('\n') + dictpasswds[t].rstrip('\n')
                print(d.rstrip('\n'))
                if password == crypt.crypt(d,''):
                    print("yes")
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break

now2 = datetime.datetime.now()
print(now1)
print(now2)

