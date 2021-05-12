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

        
        # inicio 
        lblArchivo = Label(frame,text="Archivo", font=("Calibri", 14))
        lblArchivo.grid(column=0,row=0, padx=150)

        botonBuscarArchivo = ttk.Button(frame, text="Buscar")
        botonBuscarArchivo.grid(column=0,row=2)

        rutaArchivo = ttk.Entry(frame, width=30)
        rutaArchivo.grid(column=0,row=1, pady=20)

        

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

        def browseFiles():
            filename = filedialog.askopenfilename(initialdir = "/",
                                                title = "Select a File",
                                                filetypes = (("Text files",
                                                                "*.txt*"),
                                                            ("all files",
                                                                "*.*")))
            
            # Change label contents
            label_file_explorer.configure(text="File Opened: "+filename)

    # Create the root window
        window = Tk()
        
        # Set window title
        window.title('File Explorer')
        
        # Set window size
        window.geometry("500x500")
        
        #Set window background color
        window.config(background = "white")
        
        # Create a File Explorer label
        label_file_explorer = Label(window,
                                    text = "File Explorer using Tkinter",
                                    width = 100, height = 4,
                                    fg = "blue")
        
            
        button_explore = Button(window,
                                text = "Browse Files",
                                command = browseFiles)
        
        button_exit = Button(window,
                            text = "Exit",
                            command = exit)
        
        # Grid method is chosen for placing
        # the widgets at respective positions
        # in a table like structure by
        # specifying rows and columns
        label_file_explorer.grid(column = 0, row = 0)
        
        button_explore.grid(column = 0, row = 1)
        
        button_exit.grid(column = 0,row = 2)
        
if __name__ == '__main__':
    root = Tk()
    interfaz = Interfaz(root)
    root.mainloop() 