# Importar archivo que esta en la misma carpeta
import modulo_funciones as mf

# importart archivo dentro de una carpeta en la misma ruta
import funciones.modulo_funciones as fmf

# importar archivo que esta fuera de la misma ruta
import sys
sys.path.append("c:\\Juansi\\Proyectos\\Code\\Python\\python-course\\")
import funciones.modulo_funciones as efmf

saludar = mf.Saludar("Roberto")

print(saludar)