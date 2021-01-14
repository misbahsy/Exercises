def create(filename):
    f = open(f'{filename}.txt', 'w+')
    f.close()

def write(filename, content):
    with open(f"{filename}.txt", "a+") as file:
        file.write(content)

def read(filename):
    with open(f'{filename}.txt', 'r') as file:
        data = file.read()
    return data