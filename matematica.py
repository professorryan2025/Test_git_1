cargo = input("Digite o cargo do funcionário: ")
dia_da_semana = input("Digite o dia da semana: ")

permissoes_por_cargo = {
        "gerente": ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sabado", "domingo"],
        "analista": ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sabado"],
        "estagiario": ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
    }

if cargo in permissoes_por_cargo and dia_da_semana in permissoes_por_cargo[cargo]:
    print(f"Acesso concedido. O {cargo} pode acessar o escritório na {dia_da_semana}.")
elif cargo not in permissoes_por_cargo:
    print("Cargo inválido. Por favor, digite um cargo válido (gerente, analista ou estagiário).")
else:
    print(f"Acesso negado. O {cargo} não tem permissão para acessar o escritório na {dia_da_semana}.")





