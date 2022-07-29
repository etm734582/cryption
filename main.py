import tkinter as tk
import math
import pyperclip

a = 'а'
b = 'б'
v = 'в'
g = 'г'
d = 'д'
e = 'е'
ee = 'ё'
j = 'ж'
z = 'з'
i = 'и'
ii = 'й'
k = 'к'
l = 'л'
m = 'м'
n = 'н'
o = 'о'
p = 'п'
r = 'р'
s = 'с'
t = 'т'
u = 'у'
f = 'ф'
h = 'х'
c = 'ц'
ch = 'ч'
sh = 'ш'
shh = 'щ'
tvz = 'ъ'
iii = 'ы'
mkz = 'ь'
eee = 'э'
yu = 'ю'
ya = 'я'
space = ' '

alphabet = [a, b, v, g, d, e, ee, j, z, i, ii, k, l, m, n, o, p, r, s, t, u, f, h, c, ch, sh, shh, tvz, iii, mkz, eee, yu, ya, space]

win = tk.Tk()
win['bg'] = 'lightgrey'
win.wm_attributes('-alpha', 0.95)
win.geometry('470x205')
win.wm_resizable(False, False)
win.title('7dc')

# функции

def crypt():
    global text
    global alphabet

    msg = text.get()

    cipher = []
    cipher2 = str()

    peremennaya1 = 0
    peremennaya2 = 0

    if len(msg) % 7 != 0:
        while len(msg) % 7 != 0:
            msg = msg + ' '

    # Зашифровка
    for i in range(int(len(msg)/7)):
        pl1 = msg[peremennaya1]
        pl2 = msg[peremennaya1 + 1]
        pl3 = msg[peremennaya1 + 2]
        pl4 = msg[peremennaya1 + 3]
        pl5 = msg[peremennaya1 + 4]
        pl6 = msg[peremennaya1 + 5]
        pl7 = msg[peremennaya1 + 6]
        for i in alphabet:
            if pl1 == i:
                pos1 = int(peremennaya2)
            if pl2 == i:
                pos2 = int(peremennaya2)
            if pl3 == i:
                pos3 = int(peremennaya2)
            if pl4 == i:
                pos4 = int(peremennaya2)
            if pl5 == i:
                pos5 = int(peremennaya2)
            if pl6 == i:
                pos6 = int(peremennaya2)
            if pl7 == i:
                pos7 = int(peremennaya2)
            peremennaya2 += 1
        print(pos1, pos2, pos3, pos4, pos5, pos6, pos7)
        peremennaya1 += 7
        peremennaya2 = 0
        cipseg = 10000000000 + pos1 + pos2 * 34 + pos3 * 34**2 + pos4 * 34**3 + pos5 * 34**4 + pos6 * 34**5 + pos7 * 34**6
        cipher.append(cipseg)

    for i in range(len(cipher)):
        cipher2 = cipher2 + str(cipher[i])
    print(cipher)
    print(cipher2)

    text.delete(0, tk.END)
    text.insert(0, cipher2)



def decrypt():
    global text
    global alphabet

    perem1 = 0

    decrypted_msg = str()

    ciph = text.get()
    ciph = str(ciph)

    for i in range(int(len(ciph) / 11)):
        n1 = ciph[perem1]
        n2 = ciph[perem1 + 1]
        n3 = ciph[perem1 + 2]
        n4 = ciph[perem1 + 3]
        n5 = ciph[perem1 + 4]
        n6 = ciph[perem1 + 5]
        n7 = ciph[perem1 + 6]
        n8 = ciph[perem1 + 7]
        n9 = ciph[perem1 + 8]
        n10 = ciph[perem1 + 9]
        n11 = ciph[perem1 + 10]

        num = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11

        l7 = alphabet[int((int(num) - 10000000000) // 34 ** 6)]
        num = str((int(num) - 10000000000) % 34 ** 6 + 10000000000)
        l6 = alphabet[int((int(num) - 10000000000) // 34 ** 5)]
        num = str((int(num) - 10000000000) % 34 ** 5 + 10000000000)
        l5 = alphabet[int((int(num) - 10000000000) // 34 ** 4)]
        num = str((int(num) - 10000000000) % 34 ** 4 + 10000000000)
        l4 = alphabet[int((int(num) - 10000000000) // 34 ** 3)]
        num = str((int(num) - 10000000000) % 34 ** 3 + 10000000000)
        l3 = alphabet[int((int(num) - 10000000000) // 34 ** 2)]
        num = str((int(num) - 10000000000) % 34 ** 2 + 10000000000)
        l2 = alphabet[int((int(num) - 10000000000) // 34)]
        l1 = alphabet[int((int(num) - 10000000000) % 34)]

        decrypted_msg = decrypted_msg + str(l1) + str(l2) + str(l3) + str(l4) + str(l5) + str(l6) + str(l7)
        perem1 += 11

    text.delete(0, tk.END)
    text.insert(0, decrypted_msg)

def copytext():
    global text
    pyperclip.copy(text.get())
def pastetext():
    global text
    txtforpaste = pyperclip.paste()
    text.insert(0, txtforpaste)

#Кнопки
crypt = tk.Button(text='Зашифровать', width=14, font=('Verdena', 10), command=crypt)
crypt.grid(row=2, column=0)
decrypt = tk.Button(text='Дешифровать', width=14, font=('Verdena', 10), command=decrypt)
decrypt.grid(row=3, column=0)
copytext = tk.Button(text = 'Скопировать', font=('Verdena', 9), command=copytext)
copytext.grid(row=4, column=0)
pastetext = tk.Button(text = 'Вставить', font=('Verdena', 9), command=pastetext)
pastetext.grid(row=5, column=0)

#Вводы
text = tk.Entry(win, font=('Verdena', 11), width = 50)
text.grid(row=1, column=0, padx=15, pady=15)

win.grid_columnconfigure(0, minsize=470)

win.mainloop()
