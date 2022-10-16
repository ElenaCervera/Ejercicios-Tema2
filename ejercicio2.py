# Ejercicio 2
#Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos... Transforma este texto:
#un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro
#En este otro:
#Un día que el viento soplaba con fuerza...
#- Mira como se mueve aquella banderola -dijo un monje.
#- Lo que se mueve es el viento -respondió otro monje.
#- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.
#Lo único prohibido es modificar directamente el texto.

class Texto:
    def __init__(self,texto):
        self.texto=texto

    def separar_texto(self):
        l=len(self.texto)
        frase=[]
        for i in range(l):
            print(self.texto[i])
            letra=self.texto[i]
            if letra=="#":
                frase.append(i)
        frase.append(l)      
        print(frase)      



texto="un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
