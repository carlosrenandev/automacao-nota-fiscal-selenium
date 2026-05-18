from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
from pathlib import Path
import shutil

# Abre o navegador Firefox - aqui voce pode trocar para o navegador de sua escolha
navegador = webdriver.Firefox()

# Acessa a página de login local, más voce pode adaptar tambem para funcionar em sites na internet
navegador.get(r'file:///home/renan/Downloads/Python%20-%20Projetos/Exerc%C3%ADcio%20-%20Automatizar%20Emiss%C3%A3o%20de%20Nota%20Fiscal/login.html')

# Maximiza a janela do navegador
navegador.maximize_window()

# Preenche o campo de usuário
navegador.find_element(By.XPATH, '/html/body/div/form/input[1]').send_keys('seu usuario', Keys.TAB)
# Espera 1 segundo
time.sleep(1)
# Preenche o campo de senha e faz login
navegador.find_element(By.XPATH, '/html/body/div/form/input[2]').send_keys('sua senha', Keys.TAB, Keys.ENTER)
time.sleep(1)


# Lê os dados da planilha Excel
tabela = pd.read_excel('vendas.xlsx')

for index, row in tabela.iterrows():
    # Localiza o campo nome
    nome = navegador.find_element(By.NAME, 'nome')
    # Limpa o campo antes de preencher
    nome.clear()
    # Preenche o campo com o nome/razão social
    nome.send_keys(row['Nome/Razão Social'], Keys.TAB)

    time.sleep(0.2)

    endereco = navegador.find_element(By.NAME, 'endereco')
    endereco.clear()
    endereco.send_keys(row['Endereço'], Keys.TAB)

    time.sleep(0.2)

    bairro = navegador.find_element(By.NAME, 'bairro')
    bairro.clear()
    bairro.send_keys(row['Bairro'], Keys.TAB)

    time.sleep(0.2)

    municipio = navegador.find_element(By.NAME, 'municipio')
    municipio.clear()
    municipio.send_keys(row['Município'], Keys.TAB)

    time.sleep(0.2)

    cep = navegador.find_element(By.NAME, 'cep')
    cep.clear()
    cep.send_keys(row['CEP'], Keys.TAB)

    time.sleep(0.2)

    uf = navegador.find_element(By.NAME, 'uf')
    uf.send_keys(row['UF'], Keys.TAB)

    time.sleep(0.2)

    cnpj = navegador.find_element(By.NAME, 'cnpj')
    cnpj.clear()
    cnpj.send_keys(row['CNPJ/CPF'], Keys.TAB)

    time.sleep(0.2)

    inscricao = navegador.find_element(By.NAME, 'inscricao')
    inscricao.clear()
    inscricao.send_keys(row['Inscrição estadual'], Keys.TAB)

    time.sleep(0.2)

    descricao = navegador.find_element(By.NAME, 'descricao')
    descricao.clear()
    descricao.send_keys(row['Descrição do produto/serviço'], Keys.TAB)

    time.sleep(0.2)

    quantidade = navegador.find_element(By.NAME, 'quantidade')
    quantidade.clear()
    quantidade.send_keys(row['Quantidade'], Keys.TAB)

    time.sleep(0.2)

    valor_unitario = navegador.find_element(By.NAME, 'valor_unitario')
    valor_unitario.clear()
    valor_unitario.send_keys(row['Valor Unitário'], Keys.TAB)

    time.sleep(0.2)

    valor_total = navegador.find_element(By.NAME, 'total')
    valor_total.clear()
    valor_total.send_keys(row['Valor Total'], Keys.TAB)
    
    time.sleep(0.2)

    botao = navegador.find_element(By.CLASS_NAME, 'registerbtn').click()

    navegador.refresh()

    time.sleep(0.2)

# Fecha o navegador
navegador.quit()

# Define o caminho da pasta onde os XMLs serão armazenados
caminho = Path(r'/home/renan/Downloads/notas-fiscais')
# Cria a pasta caso ela não exista
caminho.mkdir(exist_ok=True)

# Define a pasta Downloads
pasta = Path(r'/home/renan/Downloads/')

# Percorre todos os arquivos da pasta Downloads
for arquivo in pasta.iterdir():
     # Verifica se o arquivo possui extensão .xml
    if arquivo.suffix == ".xml":
         # Move o arquivo XML para a pasta notas-fiscais
        shutil.move(arquivo, caminho)