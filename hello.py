#!/usr/bin/env python3

"""
Documentação do projeto

Dependendo da língua configurada no ambiente o programa exibr a mensagem 
correspondente.

Como usar: 

Tenha a var LANG devidamente configurada ex:

    export LANG=pt_br

Execução:

    python3 hellorworld.py
    ou
    ./helloworld.py
"""
__version__ = "0.0.1"
__author__ = "Erick França"
__license__ = "Unlicense"

import os

#os.getenv obtem o valor de LANG diretamente do SO, e caso a variavel esteja
#vazia o valor padrao sera en_US, e utilizará até o quinto caracter da var

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)

