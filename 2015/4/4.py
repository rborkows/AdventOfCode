import hashlib

secret_key = "ckczppom"
#secret_key = "abcdef"

n=1
hash=""
while not hash.startswith("00000"):
    key = f"{secret_key}{n}"
    hash = hashlib.md5(key.encode()).hexdigest()
    n += 1

print("part1 =", n-1)

while not hash.startswith("000000"):
    key = f"{secret_key}{n}"
    hash = hashlib.md5(key.encode()).hexdigest()
    n += 1

print("part2 =", n-1)