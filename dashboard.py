
import pandas as pd

def exibir_dashboard():
    dados = pd.DataFrame([
        ["🎬 Roteiro (GP)", "gestor_projetos.py", "Cria roteiro 8+8 com base no problema e solução"],
        ["🗣️ Comercial", "comercial.py", "Gera copy magnética e hashtags alinhadas"],
        ["📈 Tráfego Orgânico", "trafego.py", "Otimiza roteiro para Reels e Shorts com áudio"],
        ["🎨 Design", "designer.py", "Gera capa e identidade visual com base na ECA"],
        ["🔥 Produtos Virais", "produtos_virais.py", "Lista produtos em alta na Temu com base nas tendências"],
        ["📷 Tendências Visuais", "tendencias_visuais.py", "Sugestões de estética e estilo por plataforma"],
        ["🚀 Tráfego Pago", "gestor_de_midias_pagas.py", "Configura campanhas patrocinadas no Instagram e TikTok com foco em cliques qualificados"]
    ], columns=["Área", "Arquivo", "Descrição"])

    print("\n🧠 PAINEL DA AGÊNCIA LUNA – Setores ativos:\n")
    print(dados.to_string(index=False))

if __name__ == "__main__":
    exibir_dashboard()
