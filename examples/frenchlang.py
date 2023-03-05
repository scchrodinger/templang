import sys
path = sys.argv[1]

#fill *** with your own file extention
file = path;
f = open(file, "r", encoding="utf-8")
if file[len(file) - 4:] != ".frlang":
    print("transpiler can just open .frlang files");
    quit()

#fil the blanks with your own keywords
main_lang = [
        ("saisir", "input"),
        ("sinon si", "elif"),
        ("comme", "as"),
        ("importer", "import"),
        ("autre", "else"),
        ("si", "if"),
        ("imprimer", "print"),
        ("essayer", "try"),
        ("sauf", "except"),
        ("définir", "def"),
        ("classe", "class"),
        ("retour", "return"),
        ("gamme", "range"),
        ("rendement", "yield"),
        ("depuis", "from"),
        ("continuer", "continue"),
        ("longueur", "len"),
        ("avec", "with"),
        ("pas", "not"),
        ("est", "is"),
        ("dans", "in"),
        ("pour", "for"),
        ("affirmer", "assert"),
        ("passer", "pass"),
        ("ou", "or"),
        ("vraie", "True"),
        ("faux", "False"),
        ("alors que", "while"),
        ("augmenter", "raise"),
        ("et", "and"),
        ("aucune", "None"),
        ("sortie", "exit"),
        ("casser", "break"),
        ("ouvrir", "open")
]

content = f.read()
for (lang, py) in main_lang:
    content = content.replace(lang , py);
exec(content)
