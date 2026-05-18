# 🧾 Automação de Emissão de Nota Fiscal com Selenium

## 📌 Sobre o projeto

Este projeto foi desenvolvido para automatizar o processo de emissão de notas fiscais utilizando Python e Selenium.

A automação realiza:
- Login automático no sistema;
- Leitura de dados de uma planilha Excel;
- Preenchimento automático dos formulários;
- Emissão das notas fiscais;
- Organização automática dos arquivos XML gerados.

O objetivo do projeto é reduzir tarefas repetitivas, aumentar a produtividade e minimizar erros manuais durante o processo de emissão.

---

## ⚙️ Tecnologias utilizadas

- Python 3
- Selenium
- Pandas
- OpenPyXL
- Firefox WebDriver (GeckoDriver)

---

## 🚀 Funcionalidades

- Automação de login
- Leitura de dados via Excel
- Preenchimento automático de formulários
- Emissão sequencial de notas fiscais
- Download e organização de arquivos XML
- Manipulação de arquivos e diretórios

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/carlosrenandev/automacao-nota-fiscal-selenium.git
```

### 2. Acesse a pasta do projeto

```bash
cd automacao-nota-fiscal-selenium
```

### 3. Instale as dependências

```bash
pip install selenium pandas openpyxl
```

### 4. Configure o WebDriver

Certifique-se de possuir:
- Firefox instalado
- GeckoDriver configurado no PATH do sistema

---

## ▶️ Executando o projeto

```bash
python main.py
```

---

## 📊 Dados utilizados

A automação utiliza uma planilha Excel contendo informações como:

- Nome/Razão Social
- Endereço
- Bairro
- Município
- CEP
- UF
- CNPJ/CPF
- Inscrição Estadual
- Produto/Serviço
- Quantidade
- Valor Unitário
- Valor Total

---

## 📁 Resultado da automação

Os arquivos XML gerados são automaticamente movidos para:

```bash
notas-fiscais/
```

---

## 🎯 Objetivo do projeto

Este projeto foi criado com foco em:
- Estudos de automação com Selenium;
- Manipulação de dados com Pandas;
- Automatização de processos administrativos;
- Ganho de produtividade em tarefas repetitivas.
