import crypt
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import datetime

passchar_list = 'aps01'
ph = PasswordHasher()
target = '$argon2id$v=19$m=65536,t=4,p=1$bXJLaFpCc0ZqUm5RZkhobA$9re6dU8R892t4nlTgd4T/EyuwrpOoAXVF0NuZ2yxBk0'

for a in range(len(passchar_list)):
    for b in range(len(passchar_list)):
        for c in range(len(passchar_list)):
            for d in range(len(passchar_list)):
                for e in range(len(passchar_list)):
                    print(datetime.datetime.now())
                    for f in range(len(passchar_list)):
                        total = passchar_list[a] + passchar_list[b] + passchar_list[c] + passchar_list[d] + passchar_list[e] + passchar_list[f]
                        flag = False
                        
                        try:
                            flag = ph.verify(target,total)
                        except VerifyMismatchError:
                            pass
                        
                        if flag:
                            print('yes')
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
