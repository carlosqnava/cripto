import codecs
from Crypto.Cipher import DES
from Crypto.Cipher import AES
from tkinter import messagebox

class Cifrados:
    
        
    def rc4(key, plaintext,accion):
        def KSA(key):
            ''' Key Scheduling Algorithm (from wikipedia):
                for i from 0 to 255
                    S[i] := i
                endfor
                j := 0
                for i from 0 to 255
                    j := (j + S[i] + key[i mod keylength]) mod 256
                    swap values of S[i] and S[j]
                endfor
            '''
            key_length = len(key)
            # create the array "S"
            S = list(range(MOD))  # [0,1,2, ... , 255]
            j = 0
            for i in range(MOD):
                j = (j + S[i] + key[i % key_length]) % MOD
                S[i], S[j] = S[j], S[i]  # swap values

            return S


        def PRGA(S):
            ''' Psudo Random Generation Algorithm (from wikipedia):
                i := 0
                j := 0
                while GeneratingOutput:
                    i := (i + 1) mod 256
                    j := (j + S[i]) mod 256
                    swap values of S[i] and S[j]
                    K := S[(S[i] + S[j]) mod 256]
                    output K
                endwhile
            '''
            i = 0
            j = 0
            while True:
                i = (i + 1) % MOD
                j = (j + S[i]) % MOD

                S[i], S[j] = S[j], S[i]  # swap values
                K = S[(S[i] + S[j]) % MOD]
                yield K


        def get_keystream(key):
            ''' Takes the encryption key to get the keystream using PRGA
                return object is a generator
            '''
            S = KSA(key)
            return PRGA(S)


        def encrypt_logic(key, text):
            ''' :key -> encryption key used for encrypting, as hex string
                :text -> array of unicode values/ byte string to encrpyt/decrypt
            '''
            # For plaintext key, use this
            key = [ord(c) for c in key]
            # If key is in hex:
            # key = codecs.decode(key, 'hex_codec')
            # key = [c for c in key]
            keystream = get_keystream(key)

            res = []
            for c in text:
                val = ("%02X" % (c ^ next(keystream)))  # XOR and taking hex
                res.append(val)
            return ''.join(res)


        def encrypt(key, plaintext):
            ''' :key -> encryption key used for encrypting, as hex string
                :plaintext -> plaintext string to encrpyt
            '''
            plaintext = [ord(c) for c in plaintext]
            return encrypt_logic(key, plaintext)


        def decrypt(key, ciphertext):
            ''' :key -> encryption key used for encrypting, as hex string
                :ciphertext -> hex encoded ciphered text using RC4
            '''
            try:
                ciphertext = codecs.decode(ciphertext, 'hex_codec')
                res = encrypt_logic(key, ciphertext)
                return codecs.decode(res, 'hex_codec').decode('utf-8')

            except:
                messagebox.showerror(message="No puedo descifrar un archivo que no haya sido cifrado anteriormente", title="Error")
                return False
            

        

        
        MOD = 256
        if accion == 'cifrar':
            print(encrypt(key, plaintext))
            return encrypt(key, plaintext)
        else:
            return decrypt(key, plaintext)
        

    def cifrar(llave, archivo, accion, algoritmo):
        nombreArchivo = ''
        charIdx = 0
        rutaStr=archivo 
        while(rutaStr.find('/',charIdx,-1)!=-1):
            charIdx = rutaStr.find('/',charIdx,-1) +1
            # print(charIdx)

        nombreArchivo = rutaStr[charIdx:len(rutaStr)]
        
        
        
        extension = nombreArchivo[nombreArchivo.find('.'):len(nombreArchivo)] 
        nombreNuevo = nombreArchivo[0:nombreArchivo.find('.')]
       
        if(accion == 'descifrar'):
            archivo2 = archivo
            nombreNuevo = nombreNuevo + '-desc'+extension
            archivo2 = archivo2.replace(nombreArchivo, nombreNuevo)
            archivoPlano = open (archivo,'r')
            archivoCifrado = open(archivo2, 'w')
            
            if algoritmo == 'AES-128':
                if len(llave)%16 == 0:
                    archivoPlano = open(archivo, "rb")
                    nonce,tag, ciphertext = [ archivoPlano.read(x) for x in (16, 16, -1) ]
                    # let's assume that the key is somehow available again
                    cipher = AES.new(llave.encode("utf8"), AES.MODE_EAX, nonce)
                    data = cipher.decrypt(ciphertext)
                    archivoCifrado.write(str(data)+"\n")
                
                    return nombreNuevo
                else:
                    messagebox.showerror(message="La longitud de la llave debe ser un multiplo de 16", title="Error")
                    return False
        
            Lines = archivoPlano.readlines()
 
            count = 0
            # Strips the newline character
            for line in Lines:
                count += 1
                if algoritmo == 'RC4':
                    if(Cifrados.rc4(llave, line.strip(),accion)!=False):
                        archivoCifrado.write(Cifrados.rc4(llave, line.strip(), accion)+'\n')
                    else:
                        return False
                elif algoritmo == 'DES':
                    if len(llave)%8 == 0:

                        cipher = DES.new(llave.encode("utf8"), DES.MODE_OFB)
                        msg = cipher.iv + cipher.decrypt(line.encode("utf8"))
                        print(msg)
                        archivoCifrado.write(str(msg)+"\n")
                    else:
                        messagebox.showerror(message="La longitud de la llave debe ser un multiplo de 8", title="Error")
                        return False

                
            archivoCifrado.close()
            archivoPlano.close()
            return nombreNuevo
            
        else:
            
            archivo2 = archivo
            nombreNuevo = nombreNuevo + '-cif'+extension
            archivo2 = archivo2.replace(nombreArchivo, nombreNuevo)
            archivoPlano = open (archivo,'r')
            archivoCifrado = open(archivo2, 'w')
            Lines = archivoPlano.readlines()

            count = 0
            if algoritmo == 'AES-128':
                archivoCifrado = open(archivo2, 'wb')
            # Strips the newline character
            for line in Lines:
                count += 1
                if algoritmo == 'RC4':
                    if(Cifrados.rc4(llave, line.strip(),accion)!=False):
                        archivoCifrado.write(Cifrados.rc4(llave, line.strip(), accion)+'\n')
                    else:
                        return False
                elif algoritmo == 'DES':
                    if len(llave)%8 == 0:
                        cipher = DES.new(llave.encode("utf8"), DES.MODE_OFB)
                        msg = cipher.iv + cipher.encrypt(line.encode("utf8"))
                        print(msg)
                        archivoCifrado.write(str(msg)+"\n")
                    else:
                        messagebox.showerror(message="La longitud de la llave debe ser un multiplo de 8", title="Error")
                        return False
                elif algoritmo == 'AES-128':
                    
                    if len(llave)%16 == 0:
                        cipher = AES.new(llave.encode("utf8"), AES.MODE_EAX)
                        ciphertext= cipher.encrypt(line.encode("utf8"))

                        
                        [ archivoCifrado.write(x) for x in (cipher.nonce, ciphertext) ]
                    else:
                        messagebox.showerror(message="La longitud de la llave debe ser un multiplo de 16", title="Error")
                        return False

            
            archivoCifrado.close()
            archivoPlano.close()
            return nombreNuevo
        