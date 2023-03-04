import sys
path = sys.argv[1]

#fill *** with your own file extention
file = path;
f = open(file, "r", encoding="utf-8")
if file[len(file) - 4:] != ".uklang":
    print("transpiler can just open .uklang files");
    quit()

#fil the blanks with your own keywords
main_lang = [
        ("vvedennya", "input"),
        ("inakshe, yakshcho", "elif"),
        ("yak", "as"),
        ("import", "import"),
        ("inshe", "else"),
        ("yakshcho", "if"),
        ("drukuvaty", "print"),
        ("sprobuvaty", "try"),
        ("krim", "except"),
        ("vyznachyty", "def"),
        ("klas", "class"),
        ("povernennya", "return"),
        ("diapazon", "range"),
        ("vrozhaynist", "yield"),
        ("vid", "from"),
        ("prodovzhuvaty", "continue"),
        ("dovzhyna", "len"),
        ("z", "with"),
        ("ni", "not"),
        ("ye", "is"),
        ("v", "in"),
        ("dlya", "for"),
        ("stverdzhuvaty", "assert"),
        ("propusk", "pass"),
        ("abo", "or"),
        ("pravda", "True"),
        ("pomylkovyy", "False"),
        ("poky", "while"),
        ("blef", "raise"),
        ("i", "and"),
        ("nemaye", "None"),
        ("vykhid", "exit"),
        ("pererva", "break"),
        ("vidchyneno", "open")
]

content = f.read()
for (lang, py) in main_lang:
    content = content.replace(lang , py);
exec(content)
