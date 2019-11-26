from tkinter import *
import Pmw
import string

Calculadora = Pmw.initialise(fontScheme = 'pmw1')
#Calculadora = Tk()
Calculadora.title("GRAPH_CALC")
Calculadora.config(bg='gray40')

#PANTALLA
display = Pmw.ScrolledText(Calculadora, hscrollmode='none',#dynamic
                      vscrollmode='none', hull_relief='sunken',#vscrollmode=dynamic
                      hull_background='gray40', hull_borderwidth=10, 
                      text_background='honeydew4', text_width=29, #ancho pantalla
                      text_foreground='black', text_height=9, #alto pantalla
          text_padx=10, text_pady=10, text_relief='groove',
                      text_font=('arial', 12, 'bold'))
display.pack(padx=0,pady=0)
buttons1 = Pmw.ButtonBox(Calculadora
                         ,hull_background='gray40')
def escribe():
    display.appendtext("Hola")
    #print("Hola")
def clear():
    display.clear()

buttons1.pack(fill='both', expand=1, padx=1, pady=1)
#buttons1.alignbuttons()

buttons1.add('2nd',width=5,bg='steelblue3',fg='white')
buttons1.add('Mode',bg='gray30',fg='white')
buttons1.add('Del',bg='gray30',fg='white',command=clear)
buttons1.add('Alpha',bg='gray50',fg='white')
buttons1.add('Stat',bg='gray30',fg='white')

buttons2 = Pmw.ButtonBox(Calculadora,hull_background='gray40')
buttons2.pack(fill='y', expand=1, padx=1, pady=1)
#buttons2.alignbuttons()
buttons2.add('Math',width=5,fg='white',bg='gray30')
buttons2.add("Mtrx",fg='white',bg='gray30')
buttons2.add("Pgrm",fg='white',bg='gray30',command=escribe)
buttons2.add("Vars",fg='white',bg='gray30')
buttons2.add("Clr",fg='white',bg='gray30')

buttons3 = Pmw.ButtonBox(Calculadora,hull_background='gray40')
buttons3.pack(fill='y', expand=1, padx=1, pady=1)
buttons3.add('X-1',width=5,fg='white',bg='gray30')
buttons3.add("Sin",fg='white',bg='gray30')
buttons3.add("Cos",fg='white',bg='gray30')
buttons3.add("Tan",fg='white',bg='gray30')
buttons3.add("^",fg='white',bg='gray30')

buttons4 = Pmw.ButtonBox(Calculadora,hull_background='gray40')
buttons4.pack(fill='y', expand=1, padx=1, pady=1)
buttons4.add('X2',width=5,fg='white',bg='gray30')
buttons4.add(",",fg='white',bg='gray30')
buttons4.add("(",fg='white',bg='gray30')
buttons4.add(")",fg='white',bg='gray30')
buttons4.add("/",bg='steelblue3',fg='white')

buttons5 = Pmw.ButtonBox(Calculadora,hull_background='gray40')
buttons5.pack(fill='y', expand=1, padx=1, pady=1)
buttons5.add('Log',width=5,bg='gray30',fg='white')
buttons5.add("7",bg='gray50',fg='white')
buttons5.add("8",bg='gray50',fg='white')
buttons5.add("9",bg='gray50',fg='white')
buttons5.add("x",bg='steelblue3',fg='white')

buttons6 = Pmw.ButtonBox(Calculadora,hull_background='gray40')
buttons6.pack(fill='y', expand=1, padx=1, pady=1)
buttons6.add('Ln',width=5,bg='gray30',fg='white')
buttons6.add("4",bg='gray50',fg='white')
buttons6.add("5",bg='gray50',fg='white')
buttons6.add("6",bg='gray50',fg='white')
buttons6.add("-",bg='steelblue3',fg='white')

buttons7 = Pmw.ButtonBox(Calculadora,hull_background='gray40')
buttons7.pack(fill='y', expand=1, padx=1, pady=1)
buttons7.add('STO',width=5,bg='gray30',fg='white')
buttons7.add("1",bg='gray50',fg='white')
buttons7.add("2",bg='gray50',fg='white')
buttons7.add("3",bg='gray50',fg='white')
buttons7.add("+",bg='steelblue3',fg='white')

buttons8 = Pmw.ButtonBox(Calculadora,hull_background='gray40')
buttons8.pack(fill='y', expand=1, padx=1, pady=1)
buttons8.add('Off',width=5,bg='gray30',fg='white')
buttons8.add("0",bg='gray50',fg='white')
buttons8.add(".",bg='gray50',fg='white')
buttons8.add("(-)",bg='gray50',fg='white')
buttons8.add("Enter",bg='steelblue3',fg='white')

bts = (buttons1,buttons2,buttons3,buttons4,buttons5,buttons6,
       buttons7,buttons8)
for i in bts:
    i.alignbuttons()

Calculadora.mainloop()

