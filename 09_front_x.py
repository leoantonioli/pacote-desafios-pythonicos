"""
09. front_x

Dada uma lista de strings, retorne a lista com as strings
ordenadas, porém agrupe todas as strings que começam com 'x' primeiro.

Exemplo: ['mix', 'banana' ,'xyz', 'apple', 'xanadu', 'aardvark']
Irá retornar: ['xanadu', 'xyz', 'aardvark', 'apple', 'banana' ,'mix']

Dica: Isso pode ser resolvido criando 2 listas e ordenando cada uma
antes de combina-las.
"""

def front_x(words):
    listaX = [] # Cria lista vazia para palavras com X
    lista2 = [] # Cria lista vazia pro resto
    for word in words: #  Para cada palavra na lista de palavras...
        if word[0] == "x": # Se a palavra da vez começa com X...
            listaX.append(word) # ...coloca a palavra na Lista X
        else:
            lista2.append(word) # ...senão coloca na Lista 2
    listaX.sort() # Ordena as listas
    lista2.sort()
    return listaX + lista2


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_x, ['bbb', 'ccc', 'axx', 'xzz', 'xaa'],
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x, ['ccc', 'bbb', 'aaa', 'xcc', 'xaa'],
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x, ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'],
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
