some_numbers = [1, 2, 3]
a = 20

def add(x, y):
    return x+y

class Something:
    pass

#Este if se va a ejecutar unicamente cuando quieres correr el script directamente
#No cuando lo importas como módulo.
#La variable __name__ se rellena con __main__ cuando se ejecuta como script

if (__name__ == '__main__'):
    print(f"Root Number = {a}")
    print(f"Number List = {some_numbers}")
    print(f"Adding both = {[add(a, number) for number in some_numbers]}")