def json_format(file_input, final_output):
    with open(file_input, 'r', encoding='utf-8') as istr:
        with open(final_output, 'w', encoding='utf-8') as ostr:
            for line in istr:
                line = line.rstrip('\n') + ','
                print(line, file=ostr)

        istr.close()

    with open(final_output, "r+", encoding='utf-8') as file:
        file.write('{"data":[{"id":')
        file.seek(0)
        content = file.read()
        print(content)

    buggy_name = open(final_output, 'r', encoding='utf-8')
    name = buggy_name.read()
    name = name[:-2]
    newFile = open(final_output, 'w', encoding='utf-8')
    newFile.write(name)

    file = open(final_output, 'a', encoding='utf-8')
    file.write(']}')

    return final_output