import sys
path = sys.argv[1]

#fill *** with your own file extention
file = path;
f = open(file, "r", encoding="utf-8")
if file[len(file) - 4:] != ".spalang":
    print("transpiler can just open .spalang files");
    quit()

#fil the blanks with your own keywords
main_lang = [
        ("aporte", "input"),
        ("más si", "elif"),
        ("como", "as"),
        ("importar", "import"),
        ("demás", "else"),
        ("si", "if"),
        ("imprimir", "print"),
        ("intentar", "try"),
        ("excepto", "except"),
        ("definir", "def"),
        ("clase", "class"),
        ("devolver", "return"),
        ("rango", "range"),
        ("producir", "yield"),
        ("de", "from"),
        ("continuar", "continue"),
        ("longitud", "len"),
        ("con", "with"),
        ("no", "not"),
        ("es", "is"),
        ("en", "in"),
        ("para", "for"),
        ("afirmar", "assert"),
        ("aprobar", "pass"),
        ("o", "or"),
        ("Verdadera", "True"),
        ("Falsa", "False"),
        ("mientras", "while"),
        ("aumentar", "raise"),
        ("y", "and"),
        ("Ninguna", "None"),
        ("salida", "exit"),
        ("romper", "break"),
        ("abierta", "open")
]

content = f.read()
for (lang, py) in main_lang:
    content = content.replace(lang , py);
exec(content)
