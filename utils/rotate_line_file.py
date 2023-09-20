def rotate_elements(filename:str):
    with open(file=filename, mode ='r', encoding='utf-8') as file:
        contents=file.readlines()

    first_element = contents.pop(0)
    contents.append(first_element)

    with open(file=filename, mode='w', encoding='utf-8') as file:
        file.writelines(contents)
    return first_element