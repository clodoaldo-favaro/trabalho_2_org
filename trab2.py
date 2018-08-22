
import struct

def lerNome():

    while True:
        entrada = "{:<20}".format(input('Digite o nome: '))
        if len(entrada) <= 20:
            entrada
            return entrada
        else:
            print('Entrada invalida. Tamanho maximo permitido: 20 caracteres')


def criarRegistro(numero, nome, idade, salario):

    registro = struct.pack('i20siic', numero, nome.encode('utf-8'), idade, salario, b'\n')
    return registro


def criarRegistroHelper():

    numero = int(input('Informe o numero:  '))
    nome = lerNome()
    idade = int(input('Informe a idade:  '))
    salario = int(input('Informe o salario: '))
    registro = criarRegistro(numero, nome, idade, salario)
    return registro

def gravarArquivo(lista, caminhoArquivo):

    with open(caminhoArquivo, 'ab') as arq:
        for reg in lista:
            arq.write(reg)

def mostrarRegistro(registro):
    tupla = struct.unpack('i20siic', registro)
    print('Numero: ', tupla[0])
    print('Nome: ', tupla[1].decode('utf-8'))
    print('Idade: ', tupla[2])
    print('Salario: ', tupla[3])

def mostrarTamanhoRegistro():
    print(struct.calcsize('i20siic'))


def main():
    lista = []
    reg = criarRegistroHelper()
    lista.append(reg)
    mostrarRegistro(lista[0])
    mostrarTamanhoRegistro()
    print(len(reg))







if __name__ == "__main__":
    main()