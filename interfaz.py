import tkinter as tk
from tkinter import ttk
from tkinter import *
# import filedialog module
from tkinter import filedialog

class Interfaz:

    def __init__(self, root):
        self.wind = root
        self.wind.title("Criptografía Simétrica")
        self.wind.geometry("850x600")

        frame = LabelFrame(self.wind, text="Criptografía Simétrica", font=("Calibri", 14))

        ruta = tk.StringVar()
        # inicio 
        lblArchivo = Label(frame,text="Archivo", font=("Calibri", 14))
        lblArchivo.grid(column=0,row=0, padx=150)

        rutaArchivo = ttk.Entry(frame, width=50, textvariable=ruta)
        rutaArchivo.grid(column=0,row=1, pady=20)
        
            
        def browseFiles():
            filename = filedialog.askopenfilename(initialdir = "/",
                                                title = "Select a File",
                                                filetypes = (("all files",
                                                                "*.*"),("Text files",
                                                                "*.txt*")
                                                            ))
            
            ruta.set(filename)
            
            return filename

            
        botonBuscarArchivo = ttk.Button(frame, text="Buscar", command=browseFiles)
        botonBuscarArchivo.grid(column=0,row=2)
            


        

       

        

        lblAlgoritmo = Label(frame,text="Algoritmo",font=("Calibri", 14))
        lblAlgoritmo.grid(column=1,row=0, padx=150)

        

        comboAlgoritmos = ttk.Combobox(frame, 
                            values=[
                                    "RC4", 
                                    "DES",
                                    "IDEA",
                                    "AES-128"], font=("Calibri", 12))

         
        comboAlgoritmos.grid(column=1, row=1)
        comboAlgoritmos.current(1)

        lblLlave = Label(frame,text="Llave", font=("Calibri", 14))
        lblLlave.grid(column=1,row=3, padx=150)

        inputLlave = ttk.Entry(frame, width=30)
        inputLlave.grid(column=1,row=4)

        radioValue = 0 

        radioCifrar = ttk.Radiobutton(frame, text='Cifrar',
                             variable=radioValue, value='cifrar') 
        radioDescifrar = ttk.Radiobutton(frame, text='Descifrar',
                                    variable=radioValue, value='descifrar')

        radioCifrar.grid(column=0, row=5, pady=60)
        radioDescifrar.grid(column=1, row=5)

        lblOpcionRadio = ttk.Label(frame, textvariable=radioValue)
        lblOpcionRadio.grid(column=1, row=6, sticky="E")

        btnEjecutar = ttk.Button(frame, text="Ejecutar", width=50)
        btnEjecutar.grid(column=0,row=7)


        print(comboAlgoritmos.current(), comboAlgoritmos.get()) #obtiene los datos del combo seleccionado

        frame.pack(fill="both", expand="yes", padx=20, pady=10)

        

    # Create the root window
       
        
if __name__ == '__main__':
    root = Tk()
    interfaz = Interfaz(root)
    root.mainloop() 