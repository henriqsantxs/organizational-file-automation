# Organizador de arquivos em PYTHON
Este é um script desenvolvido em python para automatizar a organização de arquivos dentro das pastas do Windows 11(focado originalmente na pasta "Downloads"), o Script escaneia a pasta alvo(Downloads), identifica as extensões dos arquivos e os move automatizamente para suas respectivas pastas organizadas, se a pasta destino não existir, o proprio Script cria se encarrega de cria-la.

Projeto desenvolvido com foco pratico para resolver o problema de acumulo de arquivos e otimizar o fluxo de trabalho diário.

## Tecnologias e Ferramentas Utilizadas

* **Python 3.x**: Linguagem para o desenvolvimento do script.
* **Biblioteca "os"**: Utilizada para mapear o sistema de arquivos, verificar a existência de diretórios e manipular caminhos de pastas.
* **Biblioteca "shutil"**: Utilizada para realizar a movimentação física dos arquivos de forma segura dentro do sistema de operação.
* **Visual Studio Code**: IDE utilizada para o desenvolvimento, testes e depuração do código.
* **Git & GitHub**: Ferramentas utilizadas para o controle de versão e hospedagem do código na nuvem.

## 📋 Funcionalidades

* Mapeamento automatizado de arquivos em diretórios locais.
* Filtragem inteligente por extensões de arquivos (imagens, documentos, instaladores e compactados).
* Criação dinâmica de diretórios de destino sob demanda.
* Tratamento de caminhos nativos do Windows utilizando strings brutas (`r""`) para evitar falhas de leitura no sistema.
* Pasta de escape ("Outros") para armazenar arquivos que não se encaixam nas regras predefinidas, evitando perda de dados.


## 🔧 Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado na sua máquina.
2. Clone este repositório ou baixe o arquivo `organizador.py`.
3. Abra o arquivo no seu editor de código (recomendo o VS Code).
4. No arquivo `organizador.py`, altere a variável `pasta_alvo` para o caminho da pasta que você deseja organizar no seu computador:
   ```python
   pasta_alvo = r"C:\Users\SEU_USUARIO\Downloads"