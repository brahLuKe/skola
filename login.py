# Jednoduchy prihlasovaci system

import tkinter

def registrace_uzivatele():
    
    uzivatelskejmeno_info = uzivatelskejmeno.get()
    heslo_info = heslo.get()
    
    file = open(uzivatelskejmeno_info, "w")
    file.write(uzivatelskejmeno_info)
    file.write(heslo_info)
    file.close()

    uzivatelskejmeno_entry.delete(0, END)
    heslo_entry.delete(0, END)
    
    Label(stranka1, text = "Registrace byla uspesna", fg = "green", font =("calibri", 11)).pack()
    

def registrace():
    global stranka1
    stranka1 = Toplevel(stranka)
    stranka1.title("Registrace") 
    stranka1.geometry("300x250")
    
    global uzivatelskejmeno
    global heslo
    global uzivatelskejmeno_entry
    global heslo_entry
  
    
    uzivatelskejmeno = StringVar()
    heslo = StringVar()
    
    Label(stranka1, text = "Prosim zadejte podrobnosti nize").pack()
    Label(stranka1, text = "").pack()
    Label(stranka1, text = "Uzivatelske jmeno * ").pack()
    uzivatelskejmeno_entry = Entry(stranka1, textvariable = uzivatelskejmeno)
    uzivatelskejmeno_entry.pack()
    Label(stranka1, text = "Heslo * "). pack()
    heslo_entry = Entry(stranka1, textvariable = heslo)
    heslo_entry.pack()
    Label(stranka1, text = "").pack()
    Button(stranka1, text = "Registrace", width = 10, height = 1, command = registrace_uzivatele).pack()
    
def prihlaseni_verify():
    uzivatelskejmeno1 = uzivatelskejmeno_verify.get()
    heslo1 = heslo_verify.get()
    uzivatelskejmeno_entry1.delete(0, END)
    heslo_entry1.delete(0, END)

def prihlaseni():
    global stranka2
    stranka2 = Toplevel(stranka)
    stranka2.title("Prihlaseni")
    stranka2.geometry("300x250")
    Label(stranka2, text = "Prosim zadejte podrobnosti nize pro prihlaseni").pack()
    Label(stranka2, text = "").pack() 
    
    global uzivatelskejmeno_verify
    global heslo_verify
    
    uzivatelskejmeno_verify = StringVar()
    heslo_verify = StringVar()
    
    global uzivatelskejmeno_entry1
    global heslo_entry1
    
    Label(stranka2, text = "Uzivatelske jmeno * ").pack()
    uzivatelskejmeno_entry1 = Entry(stranka2, textvariable = uzivatelskejmeno_verify)
    uzivatelskejmeno_entry1.pack()
    Label(stranka2, text = "").pack()
    Label(stranka2, text = "Heslo * ").pack()
    heslo_entry1 = Entry(stranka2, textvariable = heslo_verify)
    heslo_entry1.pack()
    print("")
    Button(stranka2, text = "Login", width = 10, height = 1, command = prihlaseni_verify).pack()


def hlavni_stranka():
    global stranka
    stranka = Tk()    
    stranka.geometry("300x250")
    stranka.title("Prihlasovaci System 1.0")
    Label (text = "Prihlasovaci System 1.0", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Prihlasit se", height = "2", width = "30", command = prihlaseni).pack()
    Label(text = "").pack()
    Button(text = "Registrace", height = "2", width = "30", command = registrace).pack()
    
    stranka.mainloop()
    
hlavni_stranka()

    
           
