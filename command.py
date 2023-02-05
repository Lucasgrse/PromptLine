##dir <diretório> Lista o conteúdo do diretório. /> dir
## cat <arquivo> Exibe o conteúdo de um arquivo. /> cat arquivo
##edit <arquivo> Permite editar um arquivo texto. /> edit arquivo
##exit Finaliza o interpretador de comandos. /> exit
##cd [<diretório>] Muda de diretório. /> cd caminho/diretorio
##mkdir <diretório> Cria um diretório. /> mkdir diretorio
##rm [ -d ] <diretório> Apaga um diretório. /> rm -r diretorio
##cp <arquivo> <diretorio> Copia um arquivo para um diretório. /> cp a.txt /lib/apparmor/b.txt
##mv <arquivo1> <arquivo2> Modifica o nome de um arquivo. /> mv a.txt b.txt
#rm [ -a ] <arquivo> Apaga um arquivo. /> rm -a /lib/a.txt
##ver Exibe a versão do sistema operacional. /> ver

import os
import shutil
import platform
import re
import sys

def removeFile(path):
  os.remove(path)
  ## passar o diretório da pasta e colar dentro da função

def listFile(path): 
    listFiles = os.listdir(path)
    ##retorna uma lista com todos os arquivos de um diretório e atribui em uma variável
    listFiles = ', '.join(listFiles) #realiza a conversão da lista para uma String separadas por ','
    print(listFiles)

      
def removeDir(path): ##/> rm -r diretorio
  os.path.exists(path)
  shutil.rmtree(path) ##remove o diretorio


def createDir(path):
  if not os.path.exists(path): ##cria um diretorio /> mkdir diretorio
    os.makedirs(path)
  else:
    print("Não foi possível encontrar" + path)  

def moveDir(path, path2): ##mover arquivos
    shutil.move(path, path2)


def renameDir(path, path2):
  os.path.exists(path) and os.path.exists(path2)
  os.rename(path, path2)


def seeCheck():
  print(platform.system())
  print(platform.release())

def copyFile(path, path2):
  os.path.exists(path) and os.path.exists(path2)
  shutil.copyfile(path, path2) ##move um arquivo!


def openFile(path):
  os.path.exists(path)
  with open(path, 'r') as f: 
      data = f.read()
      print(data)
  return data

def edit_file(file_name, old_text, new_text):
    with open(file_name, "r") as file:
        contents = file.read()       
    contents = contents.replace(old_text, new_text)   
    with open(file_name, "w") as file:
        file.write(contents)

def openDir(path):
  os.path.exists(path)
  os.chdir(path)
  cwd = os.getcwd() 


def exitCmd():
   sys.exit()
##não é obrigatório passar no linux 'C:', 'D:'...
##porém no windows é obrigatório
regex_dir = '(([A-Z]:)?(\/.*?\/)((?:[^\/]|\/\/\/)+?)(?:(?<!\/\/)\s|$))' ##expressão regular para coletar os caminhos informado da string digitada pelos usuários
regex_comondos = 'rm (-a|-r|-d)?|cd|ver|copy|exit|cat|edit|mkdir|cp|del|systeminfo|dir|mv' #expressão regular para coletar o comando informado pelo usuário
#Utilizando 'ou' para coletar cada comando
  

while True:
    comando = input('/>')
    diretorios =[x.group() for x in re.finditer(regex_dir,comando)] ##Aplica a expressão regular na String digitada e retorna uma lista com os caminhos encontrados
    comando =  re.match(regex_comondos,comando) ##Aplica a expressão regualr de comandos na String e retorna o comando informado pelo usuário
    if diretorios:
        print(diretorios)
    if comando:
        comando = comando.group()
        print(comando)
    if(comando == 'dir'):
        listFile(diretorios[0])
    elif(comando == 'rm -a' or comando == 'del'): ## observacao
        removeFile(diretorios[0])
    elif(comando == 'rm -d'): ## observacao
        removeDir(diretorios[0])
    elif(comando == 'mkdir'):
        createDir(diretorios[0])
    elif(comando == 'cp' or comando == "copy"):
        copyFile(diretorios[0], diretorios[1])
    elif(comando == 'cd' ):
        moveDir(diretorios[0], diretorios[1])
    elif(comando == 'ver' or comando == 'systeminfo'):
        seeCheck()
    elif(comando == 'mv'):
        renameDir(diretorios[0], diretorios[1])
    elif(comando == 'cat'):
        openFile(diretorios[0])
    elif(comando == 'exit'):
        exitCmd()
    elif(comando == 'edit'):
        question = input("Informe um novo texto: ")
        txt = openFile(diretorios[0])     
        edit_file(diretorios[0], str(txt), str(question))  
    else:
      print("Informe um comando válido")
    
      