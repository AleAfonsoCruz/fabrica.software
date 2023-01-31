nascimento = int(input("Digite o ano do seu nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual-nascimento
print(f"\nSua idade é em anos é {idade}"
      f"\nSua idade em meses é {idade*12}"
      f"\nSua idade em semanas é {idade*12*4}"
      f"\nSua idade em dias é {idade*365}")