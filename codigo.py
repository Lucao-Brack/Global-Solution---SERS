temperatura = float(input("Digite a temperatura do foguete (°C): "))

if temperatura < 60:
    print("Status: NORMAL ")
elif temperatura < 80:
    print("Status: ALERTA, houve aumento indesejável de calor no motor, mantenha cautela")
else:
    print("Status: CRITICO - Temperatura acima do limite seguro, reduza imediatamente!")


sinal = int(input("Digite a qualidade do sinal de comunicação (%): "))

if sinal >= 80:
    print("Status: NORMAL")
    print("Previsão: Comunicação estável com o foguete.")
elif sinal >= 50:
    print("Status: ALERTA")
    print("Previsão: Possíveis interferências na comunicação.")
else:
    print("Status: CRITICO")
    print("Previsão: Risco de perda de comunicação. Ação imediata necessária!")

combustivel = int(input("Digite o nível da bateria (%): "))

if combustivel >= 70:
    print("Status: NORMAL")
    print("Previsão: Energia suficiente para a operação.")
elif combustivel >= 35:
    print("Status: ALERTA")
    print("Previsão: Menos de 70% de combústivel. Recomendado iniciar o modo de economia antes de atingir 40% da energia por precaução")
else:
    print("Status: CRITICO")
    print("Previsão: Nível de bateria relativamente baixo. A potência dos motores foram reduzidas para reduzir o ácumulo de energia")

estabilidade = float(input("Digite o índice de estabilidade do centro gravitacional: "))

if estabilidade >= 90:
    print("Status: NORMAL")
    print("Previsão: O foguete mantém excelente equilíbrio durante o voo, continue prosseguindo normalmente.")
elif estabilidade >= 65:
    print("Status: ALERTA")
    print("Previsão: Pequenas oscilações detectadas. Recomenda-se monitoramento.")
else:
    print("Status: CRITICO")
    print("Previsão: Foguete saindo de controle devido ao deslocamento do centro gravitacional! Mude a tragetória imediatamente!")

pressao = float(input("Digite a pressão do sistema (kPa): "))

if 90 <= pressao <= 120:
    print("Status: NORMAL")
    print("Previsão: Pressão dentro dos limites seguros para a missão.")
elif (70 <= pressao < 90) or (120 < pressao <= 140):
    print("Status: ALERTA")
    print("Previsão: Identificado certa interferência em componentes e tubulações. Recomenda-se atenção.")
else:
    print("Status: CRITICO")
    print("Previsão: Pressão extremamente forte nos tanques e vazamento excessivo no combústivel. Ação imediata necessária!")

oxigenio = float(input("Digite o nível de oxigênio em porcentagem(%): "))

if 95 <= oxigenio <= 100:
    print("Status: NORMAL")
    print("Previsão: Controle de oxigênio perfeito para a tripulação.")
elif 85 <= oxigenio < 95:
    print("Status: ALERTA")
    print("Previsão: Identificado transpiração indevida de passageiros, recomenda-se prevenção imediata.")
else:
    print("Status: CRITICO")
    print("Previsão: Nível de oxigênio muito baixo. Protocolo de Segurança ativo!")

# Resultado e avaliação do foguete

# Definição dos pontos para cada status
NORMAL = 0
ALERTA = 1
CRITICO = 2

total_pontos = 0

# Pontuação para Temperatura
if temperatura < 60:
    total_pontos += NORMAL # 0
elif temperatura < 80:
    total_pontos += ALERTA # 1
else:
    total_pontos += CRITICO # 2

# Pontuação para Sinal de Comunicação
if sinal >= 80:
    total_pontos += NORMAL # 0
elif sinal >= 50:
    total_pontos += ALERTA # 1
else:
    total_pontos += CRITICO # 2

# Pontuação para Combustível
if combustivel >= 70:
    total_pontos += NORMAL # 0
elif combustivel >= 35:
    total_pontos += ALERTA # 1
else:
    total_pontos += CRITICO # 2

# Pontuação para Estabilidade
if estabilidade >= 90:
    total_pontos += NORMAL # 0
elif estabilidade >= 65:
    total_pontos += ALERTA # 1
else:
    total_pontos += CRITICO # 2

# Pontuação para Pressão
if 90 <= pressao <= 120:
    total_pontos += NORMAL # 0
elif (70 <= pressao < 90) or (120 < pressao <= 140):
    total_pontos += ALERTA # 1
else:
    total_pontos += CRITICO # 2

# Pontuação para Oxigênio
if 95 <= oxigenio <= 100:
    total_pontos += NORMAL # 0
elif 85 <= oxigenio < 95:
    total_pontos += ALERTA # 1
else:
    total_pontos += CRITICO # 2

pontuacao = total_pontos # Atribui a soma dos pontos à variável pontuacao

# Exibe a pontuação final e sua avaliação
print(f"Pontuação total do foguete: {pontuacao} pontos.")
if 0 <= pontuacao <= 3:
    print("Avaliação: O foguete é seguro para missões.")
elif 4 <= pontuacao <= 7:
    print("Avaliação: Aconselhável revisar alguns ajustes.")
else:
    print("Avaliação: Não é ideal para voo de forma alguma.")
