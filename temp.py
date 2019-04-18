# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""




from functools import reduce

minha_lista = [2, 4, 5, 2]

produto_total = reduce(lambda x, y: x * y, minha_lista)
print(produto_total)  # 80