from faker import Faker

fake = Faker('pt_BR')

for _ in range(5):
    print(fake.name(), '\n')
    print(fake.address(), '\n')
