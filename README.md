# Script-Crack-Linux-Hash

Este script trabalha com os hashes encontrados no arquivo /etc/shadow, de forma a buscar descobrir a senha que deu origem àquele hash.

## Como funciona?
O código recebe 3 arquivos, um deles contém os hashes Linux, normalmente encontrados no arquivo /etc/shadow, que pretendemos descobrir (pode estar baseado em algoritmos como sha256, sha512, md5...), 
o outro é uma wordlist, e por fim um arquivo vazio.
Este código abre os dois primeiros em modo leitura e o último em modo escrita, de modo que itera sobre o primeiro, dividindo o hash em 3 partes: ID, SALT e PASSWORD. o Id e salt são juntados na solução
de 'salt'. Então, ele itera sobre cada palavra da wordlist, aplicando aquele salt e vendo se o hash gerado é compatível com o hash que estamos buscando. Se sim, ele salva tanto a senha descoberta quanto o 
hash no 3º arquivo.


# Como Usar?
O crackLinuxHash.py é um script que recebe 3 argumentos:
--> HashFile: Um arquivo que contenha apenas os hashs que queremos descobrir, um por linha. O formato padrão de um hash é "$id$salt$password".
--> Wordlist: Lista de palavras que a solução irá se basear para tentar encontrar a senha correspondente ao hash.
--> ArquivoVazio: Um arquivo sem conteúdo, para que o script salve o que ele encontrar.


Para executar o script, a forma de utilizá-lo é similar a esta:
python -W ignore crackLinuxHash.py myhashes wordlist.txt senhasEncontradas.txt



