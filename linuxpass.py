import crypt
import datetime

now = datetime.datetime.now()
password = input()
passchar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#"

for a in range(len(passchar)):
    for b in range(len(passchar)):
        for c in range(len(passchar)):
            for d in range(len(passchar)):
                for e in range(len(passchar)):
                    for f in range(len(passchar)):
                        for g in range(len(passchar)):
                            now1 = datetime.datetime.now()
                            print(now)
                            for h in range(len(passchar)):
                                print(passchar[a] + passchar[b] + passchar[c] + passchar[d] + passchar[e] + passchar[f] + passchar[g] + passchar[h])
                                
                                if crypt.crypt(passchar[a] + passchar[b] + passchar[c] + passchar[d] + passchar[e] + passchar[f] + passchar[g] + passchar[h],'$y$j9T$3mSNhlyJyUJQSocdkW9T60$') ==password:
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
                else:
                    continue
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
print(now)
print(now2)
