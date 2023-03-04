import sys
path = sys.argv[1]

#fill *** with your own file extention
file = path;
f = open(file, "r", encoding="utf-8")
if file[len(file) - 4:] != "***":
    print("transpiler can just open *** files");
    quit()

#fil the blanks with your own keywords
main_lang = [
        ("", "input"
        ("", "elif"),
        ("", "as"),
        ("", "import"),
        ("", "else"),
        ("", "if"),
        ("", "print"),
        ("", "try"),
        ("", "except"),
        ("", "def"),
        ("", "class"),
        ("", "return"),
        ("", "range"),
        ("", "yield"),
        ("", "from"),
        ("", "continue"),
        ("", "len"),
        ("", "with"),
        ("", "not"),
        ("", "is"),
        ("", "in"),
        ("", "for"),
        ("", "assert"),
        ("", "pass"),
        ("", "or"),
        ("", "True"),
        ("", "False"),
        ("", "while"),
        ("", "raise"),
        ("", "and"),
        ("", "None"),
        ("", "exit"),
        ("", "break"),
        ("", "open"),
]

content = f.read()
for (lang, py) in main_lang:
    content = content.replace(lang , py);
exec(content)
