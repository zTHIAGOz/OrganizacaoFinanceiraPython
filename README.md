# Sistema de Controle Financeiro

Projeto desenvolvido em Python com foco em organização financeira, lógica de programação e arquitetura de software.

O sistema começou como um simples CRUD criado durante minha transição de estudos de Java para Python e, ao longo do desenvolvimento, evoluiu para uma aplicação mais estruturada, utilizando modularização, persistência de dados e geração de relatórios financeiros.

O objetivo do projeto é continuar sua evolução até se tornar uma aplicação completa, seja através de uma interface gráfica ou de uma API.

---

# Funcionalidades

* Adicionar movimentações
* Listar movimentações
* Editar movimentações
* Remover movimentações
* Mostrar saldo atual
* Filtrar movimentações por categoria
* Filtrar movimentações por data
* Gerar relatório financeiro
* Identificar maior entrada e maior saída
* Identificar categorias com maiores receitas e despesas
* Consultar histórico mensal
* Exportar dados para CSV
* Salvamento automático em JSON
* Carregamento automático dos dados ao iniciar o sistema

---

# Estrutura do Projeto

```text
controle-financeiro/
│
├── main.py
├── models.py
├── crud.py
├── persistencia.py
├── relatorios.py
└── utils.py
```

### Responsabilidade de cada módulo

* **main.py** → Inicialização do sistema e controle do menu principal.
* **models.py** → Classe responsável pelas movimentações financeiras.
* **crud.py** → Operações de cadastro, edição, listagem e remoção.
* **persistencia.py** → Salvamento, carregamento e exportação de dados.
* **relatorios.py** → Geração e análise dos relatórios financeiros.
* **utils.py** → Funções auxiliares e reutilizáveis do sistema.

---

# Tecnologias Utilizadas

* Python
* JSON
* CSV
* Programação Orientada a Objetos (POO)
* Modularização de Código

---

# O que pratiquei nesse projeto

Durante o desenvolvimento deste sistema, pratiquei conceitos importantes como:

* Estruturas de repetição
* Condicionais
* Funções
* Classes e Objetos
* Programação Orientada a Objetos (POO)
* Modularização
* Persistência de dados
* Manipulação de arquivos JSON
* Manipulação de arquivos CSV
* Estruturas de dados (listas e dicionários)
* Organização e refatoração de código
* Separação de responsabilidades
* Arquitetura de aplicações em Python

---

# Relatórios Financeiros

O sistema é capaz de gerar análises sobre os dados cadastrados, apresentando:

* Total de entradas
* Total de saídas
* Saldo final
* Maior entrada registrada
* Maior saída registrada
* Categoria que mais recebeu dinheiro
* Categoria com maior gasto
* Total movimentado por categoria

---

# Objetivo do Projeto

Além de praticar a estrutura da programação, o objetivo deste projeto foi simular um sistema mais próximo de aplicações reais, focando não apenas em fazer funcionar, mas também em organização, clareza, manutenção e evolução do código.

---

# Evolução do Projeto

### v1.0

* CRUD financeiro básico.
* Persistência em JSON.

### v1.1

* Relatórios financeiros.
* Histórico mensal.
* Exportação para CSV.

### v1.2

* Modularização do sistema.
* Separação em múltiplos arquivos.
* Organização da arquitetura do projeto.

### Próxima Versão (Planejada)

* Interface gráfica.
* API com Flask.
* Banco de dados.
* Dashboard financeiro.
* Sistema de usuários.

---

# Como Executar

Clone o repositório:

```bash
git clone LINK_DO_REPOSITORIO
```

Acesse a pasta:

```bash
cd controle-financeiro
```

Execute o projeto:

```bash
python main.py
```

---

# Próximas Melhorias

* Interface gráfica com Tkinter ou CustomTkinter
* API REST com Flask
* Banco de dados SQLite/PostgreSQL
* Dashboard financeiro
* Sistema de autenticação
* Testes automatizados
* Geração de gráficos e indicadores financeiros

---

Desenvolvido por Thiago Figueiredo 🚀

