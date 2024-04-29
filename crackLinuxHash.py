#!/usr/bin/python

import sys
import crypt

if len(sys.argv) < 4:
    print("\nCrack Linux Hash - Tool")
    print("Modo de uso: python ./crackLinuxHash hashesFile wordlist arquivoVazio")
    print("Exemplo: python ./crackLinuxHash myhashes.txt wordlist.txt senhasEncontradas.txt")
    sys.exit()

hashFile = sys.argv[1]
wordlist = sys.argv[2]
arquivoVazio = sys.argv[3]

try:
    with open(hashFile, "r") as hashesBuscados:
        with open(wordlist, "r") as listaDePalavras:
            with open(arquivoVazio, "w") as senhasEncontradas:
                for hash in hashesBuscados:
                    partes = hash.strip().split("$")
                    if len(partes) >= 4:
                        id = partes[1]
                        salt = partes[2]
                        passwd = "$" + partes[3]  # Restaura o caractere $ para a senha
                    salt = f"${id}${salt}$"
                    listaDePalavras.seek(0)  # Reinicia a lista de palavras para o início
                    for palavra in listaDePalavras:
                        palavra = palavra.strip()
                        hash_gerado = crypt.crypt(palavra, salt)
                        if hash_gerado == hash.strip():
                            senhasEncontradas.write(f"Senha Encontrada: {palavra} {hash}\n")
                            print (f"\nSenha Encontrada: {palavra} {hash}\n")
                            break  # Uma vez encontrada a senha, podemos parar a busca
                          
except Exception as e:
    print(f"Erro: {e}")
