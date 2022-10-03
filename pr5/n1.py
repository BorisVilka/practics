while True:
    inp = input().strip()
    if inp.isspace() or len(inp)==0:
        break
    if '>' in inp or '<' in inp or '\\' in inp or '|' in inp or '*' in inp or '?' in inp or '/' in inp:
        print('Имя строки неверно')
    else:
        if '.' not in inp:
            print('Строка не может быть файлом')
        else:
            ext = inp.split('.')[1]
            if ext.isspace():
                print('Строка не может быть файлом')
            elif not (ext == "txt" or ext == "doc" or ext == "docx" or ext == "odt" or ext == "rtf"):
                print('Строка не может быть текстовым файлом')
            else:
                print('Строка может быть текстовым файлом')
