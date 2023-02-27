import sys
path = sys.argv[1]

file = path;
f = open(file, "r", encoding="utf-8")
if file[len(file) - 4:] != ".hc":
    print("transpiler can just open .hc files (hclang files)");
    quit()

main_lang = [
        ("!!", "elif"),
        ("ols", "as"),
        ("add", "import"),
        ("!.", "else"),
        ("!", "if"),
        ("..", "print"),
        ("t!", "try"),
        ("e!", "except"),
        ("f!", "def"),
        ("clss!", "class"),
        ("rtn!", "return"),
        ("rng!", "range"),
        ("yld!", "yield"),
        ("from", "from"),
        ("cnt!", "continue"),
        ("lng!", "len"),
        ("wth!", "with"),
        ("not!", "not"),
        ("is!", "is"),
        ("in!", "in"),
        ("for!", "for"),
        ("asrt!", "assert"),
        ("pass!", "pass"),
        ("or!", "or"),
        ("T!", "True"),
        ("F!", "False"),
        ("whl!", "while"),
        ("rs!", "raise"),
        ("and!", "and"),
        ("null!", "None"),
        ("ext!", "exit"),
        ("brk!", "break"),
        ("opn!", "open"),
]

content = f.read()
for (hc, py) in main_lang:
    content = content.replace(hc , py);
exec(content)