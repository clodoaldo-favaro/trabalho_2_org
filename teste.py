with open('./bla', 'r+b') as file:
    file.seek(5)
    file.write(b'ABC')

