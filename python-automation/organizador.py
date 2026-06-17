import os
import shutil

#Defina o caminho de pastas que voce quer organizar
pastaAlvo = r"C:\Users\Henrique\Documents\testevscode"

#Pastas e suas extensões.
RegrasOrganizacao = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Instaladores": [".exe", ".msi"],
    "Compactados": [".zip", ".rar", ".7z"] 
}

def organizarPastas(caminho):
    if not os.path.exists(caminho):
        print("Esta pasta não existe.\n Verifique o caminho.")
        return
    
    #lista todos os arquivos da pasta
    arquivos = os.listdir(caminho)

    for arquivo in arquivos:
        Caminnho_Completo_Arquivo = os.path.join(caminho, arquivo)

    #Vai ignorar se for uma pasta, queremos apenas arquivos
        if os.path.isdir(Caminnho_Completo_Arquivo):
            continue

        #pega a extensão do arquivo em letras minusculas
        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()

        #descobre para qual pasta o arquivo vai
        pastaDestino =  "Outros"
        for pasta, extensoes in RegrasOrganizacao.items():
            if extensao in extensoes:
                pasta_destino = pasta
                break
        #cria a pasta destino se ela não existir.
        caminhoPastaDestino = os.path.join(caminho, pasta_destino)
        if not os.path.exists(caminhoPastaDestino):
            os.makedirs(caminhoPastaDestino)
        
        #move o arquivo para a pasta nova
        caminhoFinalArquivo = os.path.join(caminhoPastaDestino, arquivo)
        shutil.move(Caminnho_Completo_Arquivo, caminhoFinalArquivo)
        print(f"Movido: {arquivo} para {pasta_destino}")

    print("\n Organização concluida com sucesso.")


#main
organizarPastas(pastaAlvo)






