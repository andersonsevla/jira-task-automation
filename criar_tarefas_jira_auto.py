
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
import json

# === CONFIGURAÇÕES DO JIRA ===
email = "SEU_EMAIL_JIRA"
api_token = "SEU_TOKEN_DE_API"  # <- Substitua pelo seu token
jira_domain = "https://xyzbr.atlassian.net"
issue_type = "Sub-task"
excel_file = "DEVSECOPS_2025.xlsx"

# Mapeamento de História para sua Issue Key
historia_to_issue = {
    "[DevSecOps] Revisão e Atualização da Política": "YTSEC-101",
    "[DevSecOps] Integração e Avaliação de Segurança – Projeto A": "YTSEC-102",
    "[DevSecOps] Integração e Avaliação de Segurança – Projeto B": "YTSEC-103",
    "[DevSecOps] Integração e Avaliação de Segurança – Projeto C": "YTSEC-104",
    "[DevSecOps] Alinhamento de Indicadores de Gestão de SEC": "YTSEC-105"
}

# Função para criar uma sub-tarefa no Jira
def criar_subtarefa(titulo, descricao, historia):
    parent_key = historia_to_issue.get(historia)
    if not parent_key:
        print(f"⚠️ História não mapeada: {historia}")
        return

    url = f"{jira_domain}/rest/api/3/issue"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "fields": {
            "project": { "key": parent_key.split('-')[0] },
            "summary": titulo,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [{
                    "type": "paragraph",
                    "content": [{ "type": "text", "text": descricao }]
                }]
            },
            "issuetype": { "name": issue_type },
            "parent": { "key": parent_key }
        }
    }

    response = requests.post(
        url,
        headers=headers,
        auth=HTTPBasicAuth(email, api_token),
        data=json.dumps(payload)
    )

    if response.status_code == 201:
        issue_key = response.json()["key"]
        print(f"✅ Criado: {issue_key} - {titulo}")
    else:
        print(f"❌ Erro ao criar '{titulo}': {response.status_code} - {response.text}")

# === Execução ===
df = pd.read_excel(excel_file)

for _, row in df.iterrows():
    historia = row["História"]
    tarefa = row["Tarefa"]
    descricao = row["Descrição"]
    criar_subtarefa(tarefa, descricao, historia)
