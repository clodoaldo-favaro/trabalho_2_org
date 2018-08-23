import os
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
    

    
def mostrarRegistrosArquivo(caminho):
    tamanhoRegistro = struct.calcsize('ii20sic')
    tamanhoArquivo = os.stat(caminho).st_size
    print('Tamanho do arquivo:', tamanhoArquivo, 'bytes')
    print('Tamanho do registro: ', tamanhoRegistro)
    print('Total de registros: ', tamanhoArquivo // tamanhoRegistro)
    
    with open(caminho, 'rb') as arq:
        
        entrada = arq.read(tamanhoRegistro)
        print('Tamanho da entrada: ', len(entrada))
        
        while entrada != b'':
            mostrarRegistro(entrada)
            entrada = arq.read(tamanhoRegistro)
            
           
        

def mostrarTamanhoRegistro():
    print(struct.calcsize('i20siic'))


def buscaBinaria(file, l, r, chave, tamanhoArquivo):
    tamanhoRegistro = struct.calcsize('i20siic')
    
    
    if r >= l:
        meio = ((tamanhoArquivo//tamanhoRegistro)//2)*tamanhoRegistro 
        file.seek(meio)
        print('Meio do arquivo:',meio)
        registro = struct.unpack('i20siic',file.read(tamanhoRegistro))
        print('Registro[0]', registro[0])
        print('len(registro[0]', len(str(registro[0])))
        print('len(chave)', len(chave))
        print('str(registro[0]) == chave', str(registro[0]) == chave)
        if str(registro[0]) == chave:
            print('registro[0] == chave')
            return meio
        
    
    
    
    
        
    
        
        
def buscaBinariaHelper(caminho, chave):
    fim = os.stat(caminho).st_size
    tamanhoArquivo = fim
    arq = open(caminho, 'rb')
    meio = buscaBinaria(arq, 0, fim, chave, tamanhoArquivo)
    arq.close()
    return meio
    
    
    
    
    


def mostrarMenuPrincipal():
    print('1. NOVO REGISTRO')
    print('2. GRAVAR REGISTROS NO ARQUIVO')
    print('3. MOSTRAR REGISTROS NO ARQUIVO')
    print('4. PESQUISA BINARIA')
    print('7. SAIR')



    

def binarySearch(arr, l, r, x):
 
    # Check base case
    if r >= l:
 
        mid = l + (r - l)/2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
         
        # If element is smaller than mid, then it 
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
 
        # Else the element can only be present 
        # in right subarray
        else:
            return binarySearch(arr, mid+1, r, x)
 
    else:
        # Element is not present in the array
        return -1



def main():

    listaRegistros = []
    caminho = './dados'
    while True:
        mostrarMenuPrincipal()
        opcao = input('Informe a opcao desejada: ')
        if opcao == '7':
            break
        elif opcao == '1':
            listaRegistros.append(criarRegistroHelper())
        elif opcao == '2':
            gravarArquivo(listaRegistros, caminho)
            listaRegistros = []
        elif opcao == '3':
            mostrarRegistrosArquivo(caminho)
        elif opcao == '4':
            chave = input('Qual chave deseja buscar: ')
            meio = buscaBinariaHelper(caminho, chave)
            print('Encontrado: ', meio)
            
            
            












if __name__ == "__main__":
    main()