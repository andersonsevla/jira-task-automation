
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
```

---

## 🗂️ Estrutura da Planilha

O arquivo `.xlsx` deve conter as seguintes colunas:

| Épico            | História                                                | Tarefa                                               | Descrição                                              |
|------------------|----------------------------------------------------------|------------------------------------------------------|---------------------------------------------------------|
| DEVSECOPS - 2025 | [DevSecOps] Integração e Avaliação de Segurança – ...   | [CRE] Solicitar e acompanhar configuração da esteira | Garantir que as esteiras estejam corretamente ...       |

---

## ⚙️ Como usar

1. Edite o script `criar_tarefas_jira.py` com seu e-mail e API Token:

```python
email = "seu_email@empresa.com"
api_token = "SEU_TOKEN_DA_API"
```

2. Certifique-se de que sua planilha esteja no mesmo diretório e com o nome:

```bash
DEVSECOPS_2025_Historias_Tarefas_Jira.xlsx
```

3. Execute o script:

```bash
python criar_tarefas_jira.py
```

O script criará todas as sub-tarefas no Jira, vinculando cada uma à sua história correspondente.

---

## 🔒 Segurança

Nunca compartilhe seu token da API publicamente. Para manter sua segurança:
- Use variáveis de ambiente
- Adicione `.env` com `python-dotenv` (opcional)
- Ignore arquivos sensíveis no `.gitignore`

---

## ✨ Autor

Desenvolvido por [Anderson Araújo Alves](https://www.linkedin.com/in/andersonaraujoalves/), especialista em Segurança da Informação e defensor do DevSecOps na prática.

---

## 📜 Licença

Este projeto está sob a licença GNU. Sinta-se à vontade para utilizar, modificar e contribuir.

---

## 💬 Feedbacks, ideias ou dúvidas?

Me encontre no [LinkedIn](https://www.linkedin.com/in/andersonaraujoalves/) ou abra uma issue aqui no repositório.
