from tkinter import *
from tkinter import ttk
root = Tk()
root.title('Jwngdaocrypto')
root.resizable(True,True)
root.configure(background='blue')

root.frame_header = ttk.Frame()

ttk.Label(root.frame_header, text = 'CRYPTOGRAPHY', style = 'Header.TLabel').grid(row = 0, column = 1)

##################################
ttk.Label(root.frame_header, text='Shift:', style='Header.TLabel').grid(row=1, column=0)
ttk.Label(root.frame_header, text='Text:', style='Header.TLabel').grid(row=2, column=0)

cipher_shift_menu = StringVar()
Spinbox(root.frame_header, from_=1, to=25, textvariable=cipher_shift_menu).grid(row=1, column=1)

text_entry = ttk.Entry(root.frame_header, width=100)
text_entry.grid(row=2, column=1)


def caesar():

    ##################################
    ttk.Label(root.frame_header, text='CAESAR CIPHER', style='Header.TLabel').grid(row=0, column=1)
    key = 'abcdefghijklmnopqrstuvwxyz'
    def encrypt(n, plaintext):
        result = ''

        for l in plaintext.lower():
            try:
                i = (key.index(l) + n) % 26
                result += key[i]
            except ValueError:
                result += l

        return result.lower()


    def decrypt(n, ciphertext):
        result = ''
        for l in ciphertext:
            try:
                i = (key.index(l) - n) % 26
                result += key[i]
            except ValueError:
                result += l

        return result

    shift = cipher_shift_menu.get()
    shift = int(shift)
    text = text_entry.get()
    text=str(text)
    encrypted = encrypt(shift, text)



    decrypted = decrypt(shift,text)



    def finalencrypted():
        enc_dec_text.insert(0, encrypted)
    def finaldecrypted():
        enc_dec_text.insert(0, decrypted)

    choose =ttk.Label(root.frame_header, text='select->', style='Header.TLabel').grid(row=3, column=0)
    encrypt_button = ttk.Button(root.frame_header, text='Encrypt', command=lambda:finalencrypted()).grid(row=3, column=1)
    decrypt_button = ttk.Button(root.frame_header, text='Decrypt', command=lambda: finaldecrypted()).grid(row=3, column=2)
    ttk.Label(root.frame_header, text='Encrypted/Decrypted Text:', style='Header.TLabel').grid(row=4, column=0)
    enc_dec_text = ttk.Entry(root.frame_header, width=110)
    enc_dec_text.grid(row=4, column=1)
    root.frame_header.pack()
    root.mainloop()


#####################################################################



def playfair():
        ttk.Label(root.frame_header, text='PLAYFAIR CIPHER', style='Header.TLabel').grid(row=0, column=1)
        ttk.Label(root.frame_header, text='__________________NOT REQUIRED__________________', style='Header.TLabel').grid(row=1, column=1)
        key = "abcdefghijklmnopqrstuvwxyz"
        key = key.replace(" ", "")
        key = key.upper()
        def matrix(x, y, initial):
            return [[initial for i in range(x)] for j in range(y)]


        result = list()
        for c in key:
            if c not in result:
                if c == 'J':
                    result.append('I')
                else:
                    result.append(c)
        flag = 0
        for i in range(65, 91):
            if chr(i) not in result:
                if i == 73 and chr(74) not in result:
                    result.append("I")
                    flag = 1
                elif flag == 0 and i == 73 or i == 74:
                    pass
                else:
                    result.append(chr(i))
        k = 0
        my_matrix = matrix(5, 5, 0)
        for i in range(0, 5):
            for j in range(0, 5):
                my_matrix[i][j] = result[k]
                k += 1


        def locindex(c):
            loc = list()
            if c == 'J':
                c = 'I'
            for i, j in enumerate(my_matrix):
                for k, l in enumerate(j):
                    if c == l:
                        loc.append(i)
                        loc.append(k)
                        return loc


        def encrypt():
            msg =text_entry.get()
            msg=str(msg)
            msg = msg.upper()
            msg = msg.replace(" ", "")
            end=''
            i = 0
            for s in range(0, len(msg) + 1, 2):
                if s < len(msg) - 1:
                    if msg[s] == msg[s + 1]:
                        msg = msg[:s + 1] + 'X' + msg[s + 1:]
            if len(msg) % 2 != 0:
                msg = msg[:] + 'X'
            encrypted=ans=''
            enc_dec_text.insert(0,encrypted)
            while i < len(msg):
                loc = list()
                loc = locindex(msg[i])
                loc1 = list()
                loc1 = locindex(msg[i + 1])
                if loc[1] == loc1[1]:
                    enc_dec_text.insert(0,"{}{}".format(my_matrix[(loc[0] + 1) % 5][loc[1]], my_matrix[(loc1[0] + 1) % 5][loc1[1]]))
                elif loc[0] == loc1[0]:
                    enc_dec_text.insert(0,"{}{}".format(my_matrix[loc[0]][(loc[1] + 1) % 5], my_matrix[loc1[0]][(loc1[1] + 1) % 5]))
                else:
                    enc_dec_text.insert(0,"{}{}".format(my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]))
                i = i + 2


        def decrypt():
            msg = text_entry.get()
            msg = str(msg)
            msg = msg.upper()
            msg = msg.replace(" ", "")
            ans = ''


            i = 0
            for s in range(0, len(msg) + 1, 2):
                if s < len(msg) - 1:
                    if msg[s] == msg[s + 1]:
                        msg = msg[:s + 1] + 'X' + msg[s + 1:]
            if len(msg) % 2 != 0:
                msg = msg[:] + 'X'
            decrypted = ans = ''
            enc_dec_text.insert(0, decrypted)
            
            while i < len(msg):
                loc = list()
                loc = locindex(msg[i])
                loc1 = list()
                loc1 = locindex(msg[i + 1])
                if loc[1] == loc1[1]:
                    enc_dec_text.insert(0,"{}{}".format(my_matrix[(loc[0] - 1) % 5][loc[1]], my_matrix[(loc1[0] - 1) % 5][loc1[1]]))
                elif loc[0] == loc1[0]:
                    enc_dec_text.insert(0,"{}{}".format(my_matrix[loc[0]][(loc[1] - 1) % 5], my_matrix[loc1[0]][(loc1[1] - 1) % 5]))
                else:
                    enc_dec_text.insert(0,"{}{}".format(my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]))
                i = i + 2

        choose = ttk.Label(root.frame_header, text='select->', style='Header.TLabel').grid(row=3, column=0)
        encrypt_button = ttk.Button(root.frame_header, text='Encrypt', command=lambda:encrypt()).grid(row=3,column=1)
        decrypt_button = ttk.Button(root.frame_header, text='Decrypt', command=lambda:decrypt()).grid(row=3,column=2)
        ttk.Label(root.frame_header, text='Encrypted/Decrypted Text:', style='Header.TLabel').grid(row=4, column=0)
        enc_dec_text = ttk.Entry(root.frame_header, width=110)
        enc_dec_text.grid(row=4, column=1)
        root.frame_header.pack()
        root.mainloop()



#################################################################################


def des():
    import pyDes
    ttk.Label(root.frame_header, text='DATA ENCRYPTION STANDARD', style='Header.TLabel').grid(row=0, column=1)
    ttk.Label(root.frame_header, text='__________________NOT REQUIRED__________________', style='Header.TLabel').grid(row=1, column=1)
    # For Python3, you'll need to use bytes, i.e.:
    msg = text_entry.get()
    data = str(msg)

    k = pyDes.des(b"DESCRYPT", pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    d = k.encrypt(data)

    def finalencrypted():
        enc_dec_text.insert(0,d)
    def finaldecrypted():
        enc_dec_text.insert(0,k.decrypt(d))

    choose = ttk.Label(root.frame_header, text='Select->:', style='Header.TLabel').grid(row=3, column=0)
    encrypt_button = ttk.Button(root.frame_header, text='Encrypt', command=lambda:finalencrypted()).grid(row=3, column=1)
    decrypt_button = ttk.Button(root.frame_header, text='Decrypt', command=lambda:finaldecrypted()).grid(row=3, column=2)
    ttk.Label(root.frame_header, text='Encrypted/Decrypted Text:', style='Header.TLabel').grid(row=4, column=0)
    enc_dec_text = ttk.Entry(root.frame_header, width=110)
    enc_dec_text.grid(row=4, column=1)
    root.frame_header.pack()
    root.mainloop()

caesar_button = ttk.Button(root.frame_header,text='Caesar',command = lambda: caesar()).grid(row=3,column=0)
playfair_button = ttk.Button(root.frame_header,text='Playfair',command = lambda: playfair()).grid(row=3,column=1)
DES_button = ttk.Button(root.frame_header,text='DES',command = lambda: des()).grid(row=3,column=2)

root.frame_header.pack()
root.mainloop()