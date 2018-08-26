import os
import struct

# Ler o nome. Controla para que no máximo seja de 20 caracteres
def ler_nome() -> str:

    while True:
        entrada = "{:<20}".format(input('Digite o nome: '))
        if len(entrada) <= 20:
            return entrada
        else:
            print('Entrada invalida. Tamanho maximo permitido: 20 caracteres')


def criar_registro(numero, nome, idade, salario):

    registro: bytes = struct.pack('i20siic', numero, nome.encode('utf-8'), idade, salario, b'\n')
    return registro


def criar_registro_helper():

    numero = int(input('Informe o numero:  '))
    nome = ler_nome()
    idade = int(input('Informe a idade:  '))
    salario = int(input('Informe o salario: '))
    registro = criar_registro(numero, nome, idade, salario)
    return registro


def gravar_arquivo(lista, caminhoArquivo):

    with open(caminhoArquivo, 'ab') as arq:
        for reg in lista:
            arq.write(reg)


def mostrar_registro(registro):
    tupla = struct.unpack('i20siic', registro)
    print('Numero: ', tupla[0])
    print('Nome: ', tupla[1].decode('utf-8'))
    print('Idade: ', tupla[2])
    print('Salario: ', tupla[3])
    

def mostrar_registros_arquivo(caminho):
    tamanhoRegistro = struct.calcsize('ii20sic')
    tamanhoArquivo = os.stat(caminho).st_size
    print('Tamanho do arquivo:', tamanhoArquivo, 'bytes')
    print('Tamanho do registro: ', tamanhoRegistro)
    print('Total de registros: ', tamanhoArquivo // tamanhoRegistro)
    
    with open(caminho, 'rb') as arq:
        
        entrada = arq.read(tamanhoRegistro)
        print('Tamanho da entrada: ', len(entrada))
        
        while entrada != b'':
            mostrar_registro(entrada)
            entrada = arq.read(tamanhoRegistro)


def mostrar_tamanho_registro():

    print(struct.calcsize('i20siic'))


def busca_binaria(file, l, r, chave: int):

    tamanho_registro = struct.calcsize('i20siic')

    if r >= l:

        mid = ((l + (r - l)//2)//tamanho_registro)*tamanho_registro
        file.seek(mid)
        print('Posicao: ', file.tell())
        file_read = file.read(tamanho_registro)
        if len(file_read) < tamanho_registro:
            return -1
        print('Bytes lidos:', len(file_read))
        registro = struct.unpack('i20siic', file_read)


        if registro[0] == chave:
            return mid
        elif registro[0] > chave:
            return busca_binaria(file, l, mid - tamanho_registro, chave)
        else:
            return busca_binaria(file, mid + tamanho_registro, r, chave)

    else:
        return -1
        
    
    
    

def busca_binaria_helper(caminho:str, chave:int):

    r = os.stat(caminho).st_size
    arq = open(caminho, 'rb')
    posicao = busca_binaria(arq, 0, r, chave)
    arq.close()
    return posicao
    

def mostrar_menu_principal():

    print('1. NOVO REGISTRO')
    print('2. GRAVAR REGISTROS NO ARQUIVO')
    print('3. MOSTRAR REGISTROS NO ARQUIVO')
    print('4. PESQUISA BINARIA')
    print('7. SAIR')


def main():

    lista_registros = []

    caminho = './dados'
    while True:
        mostrar_menu_principal()
        opcao = input('Informe a opcao desejada: ')
        if opcao == '7':
            break
        elif opcao == '1':
            lista_registros.append(criar_registro_helper())
        elif opcao == '2':
            gravar_arquivo(lista_registros, caminho)
            lista_registros = []
        elif opcao == '3':
            mostrar_registros_arquivo(caminho)
        elif opcao == '4':
            chave :int = int(input('Qual chave deseja buscar: '))
            posicao :int = busca_binaria_helper(caminho, chave)
            if posicao != -1:
                print('Registro encontrado na posicao: ', posicao)
            else:
                print('Registro não localizado')
            
            

if __name__ == "__main__":
    main()