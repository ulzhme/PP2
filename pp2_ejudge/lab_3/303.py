s = input().strip()

s = s.replace("ZER", "0")
s = s.replace("ONE", "1")
s = s.replace("TWO", "2")
s = s.replace("THR", "3")
s = s.replace("FOU", "4")
s = s.replace("FIV", "5")
s = s.replace("SIX", "6")
s = s.replace("SEV", "7")
s = s.replace("EIG", "8")
s = s.replace("NIN", "9")

if "+" in s:
    parts = s.split("+")
    res = int(parts[0]) + int(parts[1])
elif "-" in s:
    parts = s.split("-")
    res = int(parts[0]) - int(parts[1])
elif "*" in s:
    parts = s.split("*")
    res = int(parts[0]) * int(parts[1])

res_str = str(res)

res_str = res_str.replace("0", "ZER")
res_str = res_str.replace("1", "ONE")
res_str = res_str.replace("2", "TWO")
res_str = res_str.replace("3", "THR")
res_str = res_str.replace("4", "FOU")
res_str = res_str.replace("5", "FIV")
res_str = res_str.replace("6", "SIX")
res_str = res_str.replace("7", "SEV")
res_str = res_str.replace("8", "EIG")
res_str = res_str.replace("9", "NIN")

print(res_str)