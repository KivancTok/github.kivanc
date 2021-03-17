def create_variable(file, name, value):
    with open(file, 'a') as f:
        f.write(f'{name} = {value}')


def create_def(file, name, p, function):
    with open(file, 'a') as f:
        f.write(f'def {name}({p}):\n\t{function}')

def create_class(file, name, p, function):
    with open(file, 'a') as f:
        f.write(f'class {name}:\n\tdef __init__(self, {p}):\n\t\t{function}')


def create_if(file, statement, function):
    with open(file, 'a') as f:
        f.write(f'if {statement}:\n\t{function}')

def create_else(file, function):
    with open(file, 'a') as f:
        f.write(f'else:\n\t{function}')

def create_elif(file, statement, function):
    with open(file, 'a') as f:
        f.write(f'elif {statement}:\n\t{function}')
