import crypt
passchar_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
pas = "$2y$10$ecRmAWY4n/jLa0tTzIaG7.SMhb1TfdROy3nXeG5aVZorUX1n6/WHO"

for a in range(len(passchar_list)):
    for b in range(len(passchar_list)):
        for c in range(len(passchar_list)):
            for d in range(len(passchar_list)):
                for e in range(len(passchar_list)):
                    for f in range(len(passchar_list)):
                        for g in range(len(passchar_list)):
                            for h in range(len(passchar_list)):
                                total = passchar_list[a] + passchar_list[b] + passchar_list[c] + passchar_list[d] + passchar_list[e] + passchar_list[f] + passchar_list[g] + passchar_list[h]
                                total = crypt.crypt(total,"$2y$10$ecRmAWY4n/jLa0tTzIaG7.")
                                print(total)
                                if total == pas:
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
