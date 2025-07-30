
def mostrar_tutorial():
    print("""
🧠 BEM-VINDO À AGÊNCIA INTELIGENTE DA LUNA – GUIA DE USO

🚀 O que essa ferramenta faz?
Essa agência virtual automatiza tudo o que você precisa para vender produtos Temu como afiliado(a), sem precisar aparecer.

Ela executa:
1. Roteiro com base na dor da Carla.
2. Sugestão estética e visual por plataforma.
3. Copy e hashtags prontas para atrair cliques.
4. Sugestão de áudio viral.
5. Design de capa transformadora.
6. Pesquisa de produtos em alta na Temu.
7. Configuração de tráfego pago (Instagram, TikTok Ads).

🎯 Como usar:
1. Digite “Vamos começar o projeto da semana”.
2. Envie a foto do produto.
3. Receba roteiro, copy, áudio, capa e campanha.

💡 Dica: Digite “0” para abrir a dashboard.
🆘 Para ver este guia novamente, digite:
>>> ajuda
    """)

if __name__ == "__main__":
    comando = input("Digite um comando ('0' = dashboard, 'ajuda' = tutorial): ").strip().lower()
    if comando == "0":
        from dashboard import exibir_dashboard
        exibir_dashboard()
    elif comando == "ajuda":
        mostrar_tutorial()
    else:
        print("⛔ Comando não reconhecido. Use '0' para dashboard ou 'ajuda' para o tutorial.")
