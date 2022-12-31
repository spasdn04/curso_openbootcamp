import sqlite3
import getpass

def main():
    username = input('Nombre del usuario: ')
    password = getpass.getpass('Contraseña: ')

    if verifica_credenciales(username, password):
        print('Login correcto')
    else:
        print('login incorrecto')
        i = 3
        usuario = input('Nombre de usuario: ')
        clave = getpass.getpass('Clave: ')
        crear_usuario(i, usuario, clave)
        i += 1


def verifica_credenciales(username, password):
    conn = sqlite3.connect('mifichero.db')
    cursor = conn.cursor()
    
    rows = cursor.execute(
        f'SELECT id FROM users WHERE username="{username}" AND password="{password}"'
        )
    data = rows.fetchone()
    print('data es: ', type(data))
    
    cursor.close()
    conn.close()
    
    if data == None:
        return False
    
    return True

def crear_usuario(identificador, usuario, clave):
    conn = sqlite3.connect('mifichero.db')
    cursor = conn.cursor()
    
    rows = cursor.execute(
        f'INSERT INTO users(id, username, password) VALUES(?, ?, ?)',
        (identificador, usuario, clave)
        )
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__=='__main__':
    main()