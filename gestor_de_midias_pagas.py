
def configurar_campanha(produto, plataforma):
    print(f"🛠️ Configurando campanha de tráfego pago para: {produto}")

    if plataforma.lower() == "instagram":
        objetivo = "Conversões (cliques no link Temu)"
        publico = "Mulheres 25-40, interessadas em casa, organização, decoração"
        formato = "Reels patrocinado com criativo curto (8+8), som trend e copy emocional"
        verba = "R$20/dia com teste A/B de 3 criativos"
        cta = "Link na bio ou botão 'Saiba Mais'"
    elif plataforma.lower() == "tiktok":
        objetivo = "Engajamento + tráfego qualificado"
        publico = "Mulheres 20-35, que seguem perfis de organização e viralizadores"
        formato = "UGC ou review testado em voz natural + ângulo que mostre transformação"
        verba = "R$30/dia com otimizador de vídeo (Spark Ads ou Vídeo View)"
        cta = "Link direto no vídeo ou loja"
    else:
        objetivo = "Conversões"
        publico = "Geral com base em comportamento"
        formato = "Vídeo viral + benefício direto"
        verba = "R$10/dia para teste"
        cta = "Link no botão"

    print(f"📈 Plataforma: {plataforma}")
    print(f"🎯 Objetivo: {objetivo}")
    print(f"👥 Público-alvo: {publico}")
    print(f"🎞️ Criativo: {formato}")
    print(f"💰 Verba recomendada: {verba}")
    print(f"🔗 CTA: {cta}")
    print("\n✅ Campanha sugerida com base na ECA. Pronta para veicular.")
