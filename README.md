# NUTRITRACK 🥗

## Planeador Alimentar e Monitorização Nutricional

O **NUTRITRACK** é uma aplicação desenvolvida em Python que permite registar e acompanhar a alimentação diária do utilizador.

O projeto permite guardar informações sobre os alimentos consumidos, consultar o consumo diário, definir objetivos nutricionais e acompanhar a evolução relativamente aos objetivos definidos.

---

## 🎯 Objetivo do Projeto

O objetivo do NUTRITRACK é facilitar o registo e acompanhamento da alimentação diária, permitindo ao utilizador ter uma visão geral dos seus consumos nutricionais.

A aplicação foi desenvolvida como projeto académico, com o objetivo de aplicar conhecimentos de programação, utilização de bases de dados, tratamento de dados e desenvolvimento de interfaces.

---

## ✨ Funcionalidades

A aplicação disponibiliza as seguintes funcionalidades:

* 👤 Registo de utilizadores
* 🔐 Login com email e password
* 🔒 Proteção das passwords através de hash com `bcrypt`
* 🍎 Registo de alimentos consumidos
* 📅 Registo da data da refeição
* 🍽️ Registo do tipo de refeição
* ⚖️ Registo da quantidade consumida
* 🔥 Registo de calorias
* 💪 Registo de proteínas
* 🍞 Registo de hidratos de carbono
* 🥑 Registo de gorduras
* 📋 Listagem dos registos alimentares
* 📊 Consulta do consumo diário
* 🎯 Definição de objetivos nutricionais
* 📈 Acompanhamento dos objetivos
* 🗑️ Remoção de registos alimentares
* 💾 Armazenamento dos dados

---

## 🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido utilizando:

* **Python**
* **MySQL**
* **MySQL Connector**
* **Tkinter**
* **bcrypt**
* **JSON**

### Python

É a principal linguagem utilizada no desenvolvimento da aplicação.

### MySQL

É utilizado para armazenar e gerir os dados dos utilizadores.

### Tkinter

É utilizado para criar a interface gráfica da aplicação.

### bcrypt

É utilizado para criar um hash seguro das passwords dos utilizadores.

### JSON

É utilizado para armazenar determinados dados da aplicação.

---

## 📂 Estrutura do Projeto

Uma possível estrutura do projeto é:

```text
NUTRITRACK/
│
├── main.py
├── interface.py
├── mysql_database.py
├── utilizadores.py
│
├── dados_utilizador_*.json
│
├── .gitignore
├── README.md
│
└── .venv/
```

> Os nomes dos ficheiros podem variar de acordo com a versão atual do projeto.

---

## ⚙️ Requisitos

Para executar o projeto é necessário ter instalado:

* Python 3
* MySQL Server
* MySQL Connector para Python
* bcrypt
* Tkinter

---

## 📥 Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/tchelon-silva/NUTRITRACK.git
```

### 2. Entrar na pasta do projeto

```bash
cd NUTRITRACK
```

### 3. Criar um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual

No Windows:

```bash
.venv\Scripts\activate
```

### 5. Instalar as bibliotecas necessárias

```bash
pip install mysql-connector-python bcrypt
```

> O Tkinter normalmente já vem incluído na instalação do Python no Windows.

---

## 🗄️ Configuração da Base de Dados

Antes de executar a aplicação, é necessário ter o MySQL instalado e em funcionamento.

Deve ser criada uma base de dados chamada:

```sql
CREATE DATABASE nutritrack;
```

Também é necessário configurar os dados de ligação à base de dados no ficheiro responsável pela conexão.

Exemplo:

```python
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="A_TUA_PASSWORD",
    database="nutritrack"
)
```

Substitui `A_TUA_PASSWORD` pela password do teu utilizador MySQL.

---

## ▶️ Executar a Aplicação

Depois de configurar o ambiente e a base de dados, executar:

```bash
python main.py
```

A aplicação deverá iniciar e apresentar o menu principal do NUTRITRACK.

---

## 📋 Menu Principal

O programa disponibiliza as seguintes opções:

```text
1 - Registar alimento
2 - Listar registos alimentares
3 - Consultar consumo diário
4 - Definir objetivos
5 - Acompanhar objetivos
6 - Remover registo
0 - Sair
```

Cada opção permite realizar uma determinada operação dentro da aplicação.

---

## 🔐 Segurança

As passwords dos utilizadores **não são guardadas diretamente** na aplicação.

Antes de serem armazenadas, são transformadas através do `bcrypt`, criando um hash da password.

Durante o login, a password introduzida pelo utilizador é comparada com o hash armazenado.

---

## 💾 Armazenamento de Dados

O NUTRITRACK utiliza diferentes formas de armazenamento de acordo com os dados utilizados pela aplicação.

O **MySQL** é utilizado para armazenar informações relacionadas com os utilizadores.

Ficheiros **JSON** podem ser utilizados para armazenar determinados dados dos registos alimentares.

---

## 🧪 Projeto Académico

Este projeto foi desenvolvido para fins académicos, com o objetivo de aplicar conceitos de:

* Programação em Python
* Funções e métodos
* Classes e objetos
* Estruturas de dados
* Validação de dados
* Tratamento de erros
* Bases de dados
* SQL
* Interfaces gráficas
* Autenticação de utilizadores
* Organização de projetos

---

## 🚀 Possíveis Melhorias Futuras

Algumas funcionalidades que podem ser adicionadas no futuro:

* 📊 Gráficos de evolução nutricional
* 📅 Histórico alimentar por períodos
* 🔎 Pesquisa de alimentos
* 🥘 Base de dados com alimentos pré-definidos
* 📱 Versão para dispositivos móveis
* 📈 Estatísticas nutricionais mais detalhadas
* 🔔 Alertas relacionados com os objetivos
* 👤 Gestão mais completa do perfil do utilizador

---

## 👨‍💻 Autor

**tchelon-silva**

Projeto académico — **NUTRITRACK**

---

## 📄 Licença

Este projeto foi desenvolvido para fins académicos.
