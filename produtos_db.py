
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Escopo para acessar o Google Sheets e Drive
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Conectar à API usando seu credentials.json (coloque esse arquivo na mesma pasta do script)
def conectar_planilha(nome_planilha, aba="BD"):
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    cliente = gspread.authorize(creds)
    planilha = cliente.open(nome_planilha).worksheet(aba)
    return planilha

# Adiciona um novo produto testado
def adicionar_produto(planilha, produto, link, testado, resultado, observacao):
    data_hoje = datetime.today().strftime('%d/%m/%Y')
    nova_linha = [produto, link, testado, resultado, observacao, data_hoje]
    planilha.append_row(nova_linha)
    print("✅ Produto adicionado com sucesso!")

# Lista todos os produtos
def listar_produtos(planilha):
    dados = planilha.get_all_records()
    print("📋 PRODUTOS CADASTRADOS:")
    for item in dados:
        print(item)

# Exemplo de uso
if __name__ == "__main__":
    nome_da_planilha = "Produtos Testados – Agência Luna"
    aba = "BD"
    planilha = conectar_planilha(nome_da_planilha, aba)

    # Exemplo: adicionar_produto(planilha, "Organizador Giratório", "https://temu.link", "Sim", "Alto engajamento", "Testado no TikTok")
    # Exemplo: listar_produtos(planilha)
