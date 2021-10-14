from faker import Faker

fake = Faker('pt_BR')

for _ in range(5):
    print(f'Nome: {fake.name()}\n'
          f'CPF: {fake.cpf()}\n'
          f'Endereço: {fake.address()}\n')
