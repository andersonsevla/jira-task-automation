# 🛡️ Jira Task Automation for DevSecOps

Automatize a criação de tarefas no Jira a partir de uma planilha Excel organizada por Épico, História, Tarefa e Descrição.  
Este projeto foi desenvolvido com foco em projetos de **DevSecOps**, otimizando tempo, garantindo rastreabilidade e eliminando processos repetitivos.

---

## 🚀 Visão Geral

Ao invés de inserir manualmente dezenas de tarefas no Jira, este script Python permite que você:
- Leia automaticamente uma planilha `.xlsx` estruturada
- Crie sub-tarefas para histórias já existentes
- Vincule corretamente tarefas a suas histórias dentro de um épico
- Insira as descrições de forma limpa e padronizada

---

## 🧩 Pré-requisitos

- Python 3.8+
- Token da API do Jira
- Conta Atlassian com permissão para criar issues
- Biblioteca `pandas`, `requests`, `openpyxl`

Instale as dependências com:

```bash
pip install pandas requests openpyxl
