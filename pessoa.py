import re

class Email:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.emails = []

    def add_email(self, email):
        self.emails.append(email)

class PersonDAO:
    def save(self, p: Person):
        # Lógica de salvar a pessoa no banco de dados (não implementada aqui)
        pass

    def isValidToInclude(self, p: Person):
        errors = []

        # Validação do nome (deve ter ao menos duas partes e ser composto apenas por letras)
        if not p.name or len(p.name.split()) < 2 or not all(part.isalpha() for part in p.name.split()):
            errors.append("Nome deve conter ao menos duas partes compostas apenas por letras")

        # Validação da idade (deve estar no intervalo [1, 200])
        if p.age < 1 or p.age > 200:
            errors.append("Idade deve estar no intervalo de 1 a 200")

        # Verificar se há ao menos um email
        if not p.emails:
            errors.append("Person deve ter ao menos um Email associado")

        # Validação dos emails
        email_pattern = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        for email in p.emails:
            if not email_pattern.match(email.name):
                errors.append("Email deve estar no formato correto (ex: name@example.com)")

        return errors
