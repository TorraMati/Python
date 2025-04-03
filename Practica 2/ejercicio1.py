#Guardamos el zen de python en una variable
zen_text = """Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

#Separamos el texto en lineas
texto = zen_text.split("\n")

vocales = "AEIOUaeiou"

#Recorremos las lineas
for linea in texto:
    palabras = linea.split()    #Separamos la linea en palabras

    #Chequeamos que haya mas de una palabra y guardamos la segunda
    if len(palabras) > 1:
        segunda_palabra= palabras[1]

        #Chequeamos que empiece con vocal e imprimimos
        if segunda_palabra[0] in vocales:
            print(linea)