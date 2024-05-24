import crypt
import datetime
passchar_list = "aps01"
pas = "$2y$10$sDHri8P3GcFs9RafCgLkv.0.1rHzlRAmlyG0o5GB0H8UXoEUMqTQO"

for a in range(len(passchar_list)):
    for b in range(len(passchar_list)):
        for c in range(len(passchar_list)):
            for d in range(len(passchar_list)):
                for e in range(len(passchar_list)):
                    print(datetime.datetime.now())
                    for f in range(len(passchar_list)):
                        total = passchar_list[a] + passchar_list[b] + passchar_list[c] + passchar_list[d] + passchar_list[e] + passchar_list[f]
                        total = crypt.crypt(total,"$2y$10$sDHri8P3GcFs9RafCgLkv.")
                        print(total)
                        if total == pas:
                            print("yes " + total)
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
