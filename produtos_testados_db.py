
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Nome da sua planilha e aba
SHEET_NAME = "Produtos Testados – Agência Luna"
WORKSHEET_NAME = "Página1"

# Escopos e credenciais
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
CREDENTIALS_FILE = "hazel-freehold-467512-m0-0088eb241bf8.json"  # já enviado ao chat

# Inicializa o cliente
def conectar_planilha():
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME)
    return sheet.worksheet(WORKSHEET_NAME)

# Adiciona novo produto à planilha
def registrar_produto(produto, link_temu, testado, resultado, observacoes):
    ws = conectar_planilha()
    data = datetime.now().strftime("%d/%m/%Y")
    nova_linha = [produto, link_temu, testado, resultado, observacoes, data]
    ws.append_row(nova_linha)
    print(f"✅ Produto registrado com sucesso: {produto}")
