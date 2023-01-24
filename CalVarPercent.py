import os

os.system("cls") or None

while True:
    ValIni = input("Digite o valor inicial: ")
    ValIni = int(ValIni)
    if ValIni > 0:
        break

print()

while True:
    ValFim = input("Digite o valor final: ")
    ValFim = int(ValFim)
    if ValFim >= 0:
        break
print()

DifVal = ValFim - ValIni

Perc = (abs(DifVal) / ValIni) * 100

if DifVal < 0:
    print("A variação percentual foi de -", Perc, "%")
else:
     print("A variação percentual foi de +", Perc, "%")
