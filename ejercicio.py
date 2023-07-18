from tkinter import *
import sqlite3
from tkinter import messagebox

raiz=Tk()

Miframe=Frame(raiz)
Miframe.pack()

Miframe2=Frame(raiz)
Miframe2.pack()


#instruccion=("INSERT INTO persona VALUES(NULL,'{0}', '{1}', '{2}', '{3}', '{4}')".format(minombre.get(), miapellido.get(), micontrasena.get(), midirecion.get(), COMENTARIOS.get('1.0', END))
#--------------------funciones-------------

def conexion_():
	conexion=sqlite3.connect('mydatabase')

	cursor=conexion.cursor()


	try:
		cursor.execute('''CREATE TABLE persona(id INTEGER PRIMARY KEY AUTOINCREMENT, 
		nombre VARCHAR(50), 
		apellido VARCHAR(50), 
		contraseña varchar(20),
		direccion VARCHAR(50), 
		comentarios VARCHAR(200))''')
		messagebox.showinfo("Information","Base de datos creada")
	except sqlite3.OperationalError:
			
		messagebox.showerror("Error", "Base de datos ya existe")
	conexion.close()





def insert():
	Micon=sqlite3.connect('mydatabase')
	cursor=Micon.cursor()
	
	nombre_=minombre.get()
	apellido_=miapellido.get()
	contrasena_=micontrasena.get()
	direccion_=midirecion.get()
	comengtarios_=COMENTARIOS.get("1.0", END)
	ins=(nombre_, apellido_, contrasena_, direccion_, comengtarios_)
	
	cursor.execute('INSERT INTO persona VALUES(NULL,?,?,?,?,?)', ins)

	Micon.commit()
	Micon.close()
	messagebox.showinfo('BBDD', 'Datos insertados con exito')
	

def leer_():

	Micon=sqlite3.connect('mydatabase')
	cursor=Micon.cursor()
	
	cursor.execute("SELECT * FROM persona WHERE id="+ miid.get())
	elusuario=cursor.fetchall()
	for usuario in elusuario:

		miid.set(usuario[0])
		minombre.set(usuario[1])
		miapellido.set(usuario[2])
		micontrasena.set(usuario[3])
		midirecion.set(usuario[4])
		COMENTARIOS.insert(1.0, usuario[5])
	Micon.commit()	
	Micon.close()
	
	
def cerrar():
	miid.set("")
	minombre.set("")
	miapellido.set("")
	micontrasena.set("")
	midirecion.set("")
	COMENTARIOS.delete("1.0", END)

def delete():

	Micon=sqlite3.connect('mydatabase')
	cursor=Micon.cursor()
	
	cursor.execute("DELETE FROM persona WHERE id="+ miid.get())
	
	Micon.commit()	
	Micon.close()
	cerrar()
	messagebox.showinfo('DELETE', 'Se ha borrado exitosamente')


def actualizar():
	Micon=sqlite3.connect('mydatabase')
	cursor=Micon.cursor()
	
	nombre_=minombre.get()
	apellido_=miapellido.get()
	contrasena_=micontrasena.get()
	direccion_=midirecion.get()
	comengtarios_=COMENTARIOS.get("1.0", END)
	ins=(nombre_, apellido_, contrasena_, direccion_, comengtarios_)
	
	cursor.execute("UPDATE persona SET nombre=?, apellido=?, contraseña=?,direccion=?,comentarios=?"+"WHERE id="+miid.get(), (ins))
	messagebox.showinfo('UPDATE', 'Se ha actualizado')
	Micon.commit()
	Micon.close()

#-----------entrys-----------

miid=StringVar()
minombre=StringVar()
miapellido=StringVar()
micontrasena=StringVar()
midirecion=StringVar()




id=Label(Miframe, text='ID :')
id.grid(row=1, column=1, sticky='e', columnspan=2)
ID=Entry(Miframe, textvariable=miid)
ID.grid(row=1, column=3, padx=5, pady=5, columnspan=2)

nombre=Label(Miframe, text='NOMBRE :')
nombre.grid(row=2, column=1, sticky='e', columnspan=2)
NOMBRE=Entry(Miframe, textvariable=minombre)
NOMBRE.grid(row=2, column=3, padx=5, pady=5, columnspan=2)

apellido=Label(Miframe, text='APELLIDO :')
apellido.grid(row=3, column=1, sticky='e', columnspan=2)
APELLIDO=Entry(Miframe, textvariable=miapellido)
APELLIDO.grid(row=3, column=3, padx=5, pady=5, columnspan=2)

contrasena=Label(Miframe, text='CONTRASEÑA :')
contrasena.grid(row=4, column=1, sticky='e', columnspan=2)
CONTRASENA=Entry(Miframe, show='*', textvariable=micontrasena)
CONTRASENA.grid(row=4, column=3, padx=5, pady=5, columnspan=2)

direcion=Label(Miframe, text='DIRECCIÓN :')
direcion.grid(row=5, column=1, sticky='e', columnspan=2)
DIRECION=Entry(Miframe, textvariable=midirecion)
DIRECION.grid(row=5, column=3, padx=5, pady=5, columnspan=2)

comentarios=Label(Miframe, text='COMENTARIOS:')
comentarios.grid(row=6, column=1, sticky='e', columnspan=2)
COMENTARIOS=Text(Miframe, width=20, height=5) 
COMENTARIOS.grid(row=6, column=3, columnspan=2)




scrollvert=Scrollbar(Miframe, command= COMENTARIOS.yview)
scrollvert.grid(row=6, column=5, sticky='nsew')
COMENTARIOS.configure(yscrollcommand= scrollvert.set)

#-------------------botones---------------

crear=Button(Miframe2, text='Crear', command=insert)
crear.grid(row=0, column=1, sticky='s', padx=5, pady=5)


leer=Button(Miframe2, text='Leer', command=leer_)
leer.grid(row=0, column=2, sticky='s', padx=5, pady=5)

refresh=Button(Miframe2,text='Refresh', command=actualizar)
refresh.grid(row=0, column=3, sticky='s', padx=5, pady=5)

borrar=Button(Miframe2, text='Borrar', command=delete)
borrar.grid(row=0, column=4, sticky='s', padx=5, pady=5)

#------------------menu-------------

menubar = Menu(raiz)
raiz.config(menu=menubar)



bbddmenu = Menu(menubar, tearoff=0)
bbddmenu.add_command(label="Conectar", command=conexion_)
bbddmenu.add_separator()
bbddmenu.add_command(label="Salir", command=raiz.quit)

borrarmenu = Menu(menubar, tearoff=0)
borrarmenu.add_command(label="Borrar todo", command=cerrar)

crudmenu = Menu(menubar, tearoff=0)
crudmenu.add_command(label="Crear", command=insert)
crudmenu.add_command(label="Leer", command=leer_)
crudmenu.add_command(label="Refresh", command=actualizar)
crudmenu.add_command(label="Borrar", command=delete)

ayudamenu=Menu(menubar, tearoff=0)
ayudamenu.add_command(label="Acerca de...")

menubar.add_cascade(label="BBDD", menu=bbddmenu)
menubar.add_cascade(label="Borrar", menu=borrarmenu)
menubar.add_cascade(label="CRUD", menu=crudmenu)
menubar.add_cascade(label="Ayuda", menu=ayudamenu)

raiz.mainloop()