import crypt
import random
import string

# パスワードの文字列
password = input()

# 任意の8文字のsaltを生成する関数
def generate_salt(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

# saltの生成
salt = generate_salt()

# ハッシュの生成
hashed_password = crypt.crypt(password, f"$1${salt}$")

# 出力
print("Password:", password)
print("Salt:", salt)
print("Hashed Password:", hashed_password)

