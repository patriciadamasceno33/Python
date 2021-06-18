def make_text_funcs(texto):
    t = u = v = ''
    def size():
        return len(texto)
    def word_count(t):
        return texto.count(t)
    def char_count(u):
        return texto.count(u)
    def append(v):
        nonlocal texto
        texto = texto + v
        return texto
    d = dict()
    d['size'] = size
    d['word_count'] = word_count
    d['char_count'] = char_count
    d['append'] = append
    return d


text = """\
This is some text. It has much text in it.
There is much of the text.
text, text, text.
"""

funcs = make_text_funcs(text)
#print(funcs)
print("Total length of text:", funcs['size']())
print("Occurrences of 'text':", funcs['word_count']("text"))
print("Occurrences of the letter 't':", funcs['char_count']("t"))
funcs['append']("text text text")
print("After appending:")
print("Total length of text:", funcs['size']())
print("Occurrences of 'text':", funcs['word_count']("text"))
print("Occurrences of the letter 't':", funcs['char_count']("t"))