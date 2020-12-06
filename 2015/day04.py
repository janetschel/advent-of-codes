from hashlib import md5

with open("./inputs/day04.in") as file:
    secret_key: str = file.readline().strip()

hash: str = ""
ans: int = -1
while not hash.startswith("000000"): # for part 2 add an extra 0 (takes some time)
    ans += 1
    hash = md5(bytes(secret_key + str(ans), encoding="utf-8")).hexdigest()

print("Number to produce five leading zeroes:", int(ans))
