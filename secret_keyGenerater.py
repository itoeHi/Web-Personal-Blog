import secrets
# 生成64位（512bit）的随机密钥
secure_secret = secrets.token_hex(32)
print(f"生成的安全密钥: {secure_secret}")  # 复制打印出来的新key给.env文件里的SERCRET_KEY值
