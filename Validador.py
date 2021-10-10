import usuarioChecker
import passw

correcto = False
while correcto == False:
    nombre = input("Ingrese nombre de usuario: ")
    if usuario.nickname(nombre) == True:
        print("Usuario creado exitosamente")
        correcto = True

while correcto == True:
    contrasenia = input("Ingrese su Password: ")
    if passw.clave(contrasenia) == True:
        print("Contraseña creada exitosamente")
        correcto = False
