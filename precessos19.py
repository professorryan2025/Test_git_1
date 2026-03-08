
import random
class Simulador_pagina:

    def simular_carregamento(usuarios_simultaneos, dispositivo, horario):

        tempo_base = 0.5
        usuarios = usuarios_simultaneos / 100 
        fator_dispositivo = 0.0
    
        if dispositivo == 'mobile':
           fator_dispositivo = 0.2
        horario = 0.2

        if horario == 'pico':
            horario = 0.3

        variacao_aleatoria = random.uniform(0.1, 0.4)

        tempo_carregamento = tempo_base + usuarios + fator_dispositivo + horario + variacao_aleatoria

        return tempo_carregamento
 
    print("Iniciando simulação de desempenho da página...")
    print("-" * 40)

    usuarios_1 = 20
    dispositivo_1 = 'desktop'
    horario_1 = 'normal'
    tempo_1 = simular_carregamento(usuarios_1, dispositivo_1, horario_1)
    print(f"Cenário 1: {usuarios_1} usuários, {dispositivo_1}, horário {horario_1}")
    print(f"Tempo de carregamento simulado: {tempo_1:.2f} segundos\n")

    usuarios_2 = 300
    dispositivo_2 = 'mobile'
    horario_2 = 'pico'
    tempo_2 = simular_carregamento(usuarios_2, dispositivo_2, horario_2)
    print(f"Cenário 2: {usuarios_2} usuários, {dispositivo_2}, horário {horario_2}")
    print(f"Tempo de carregamento simulado: {tempo_2:.2f} segundos\n")

    usuarios_3 = 1000
    dispositivo_3 = 'desktop'
    horario_3 = 'pico'
    tempo_3 = simular_carregamento(usuarios_3, dispositivo_3, horario_3)
    print(f"Cenário 3: {usuarios_3} usuários, {dispositivo_3}, horário {horario_3}")
    print(f"Tempo de carregamento simulado: {tempo_3:.2f} segundos\n")

print("-" * 40)
print("Simulação concluída.")