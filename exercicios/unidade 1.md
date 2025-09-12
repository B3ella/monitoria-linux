## informações necessárias
### grupos
wheel (groupo de usuários que tem acesso mais alto)
### Diretórios
#### /home/NOME 
diretório padrão do usuário NOME

#### /etc/sudoers
definição de quais usuários podem usar sudo

#### ~ 
equivale à /home/nome do usuário logado
### Comandos
#### ls PATH
mostra todos os arquivos e diretórios na path, se não receber uma PATH usa . como padrão
#### cat PATH
Lê o arquivo em PATH como um arquivo de texto
#### grep ALVO
Substitua alvo pelo que você quer procurar
recebe um testo como entrada padrão e retorna somente as linhas que contem o texto ALVO
#### programa1 | programa2
executa os 2 programas em sequência e passa a saída padrão do programa 1 como entrada padrão do programa 2
#### touch PATH 
substitua PATH pelo caminho relativo ou absoluto até o local desejado

Cria um arquivo vazio na path definida
#### mkdir PATH
cria um diretório na path recebida
#### cd PATH
se movimenta para o diretório PATH
#### groups
mostra os grupos que seu usuário faz parte
#### useradd -m USUARIO 
substitua USUARIO pelo nome que desejar

cria usuário chamado USUARIO e adiciona uma pasta diretório pra ele em home/USUARIO
#### passwd USUARIO
Muda ou cria uma senha pro usuário chamado USUARIO
#### su USUARIO:
faz login como o usuário chamado USUARIO
#### usermod -aG USUARIO GROUPO
Adiciona o usuário USUARIO ao grupo GRUPO
#### chmod MODE PATH 
substitua PATH pelo caminho relativo ou absoluto até o local desejado

muda as permissões do arquivo
##### Modos Comuns
Todo modo começa com a identificação de quem afeta u (o dono do arquivo) g (o grupo dono do arquivo) o (outros usuários) ou a (todos, é o padrão se você não escolher outro)
depois vem o sinal de adicionar ou retirar permição (+, -)
E por último o tipo de permição (rxw) como explicado na última aula

u-r tira a permissão de leitura do usuário dono do arquivo
#### chow USER:GROUP PATH
muda o usuário dono do arquivo ou diretório em PATH pra USER e o grupo dono para GROUP
#### ps aux 
mostra todos os processos ativos e qual comando começou eles
#### kill PID 
subistituir PID pelo id do processo alvo:
manda um sinal SIGINT pro processo alvo. Solicitando que ele se interrompa de maneira adequada
#### kill s -9 PID
manda um sinal SIGKILL pro processo alvo. forçando ele a encerrar
## Exercícios
### 1 - Parando um programa que se recusa a parar
clone esse repositório e execute o arquivo imparavel.py, agora interrompa ele
### 2 -  criando um arquivo na pasta de outro usuário e não deixando ele ler
### 3 -  Criando um arquivo na pasta home do seu usuário usando outro usuário
