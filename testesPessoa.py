import unittest
from pessoa import Person, PersonDAO, Email

class TestPersonDAO(unittest.TestCase):

    def setUp(self):
        self.dao = PersonDAO()

    def test_valid_person(self):
        person = Person(1, "Frederick Bulsara", 30)
        person.add_email(Email(1, "queen@example.com"))
        errors = self.dao.isValidToInclude(person)
        self.assertEqual(errors, [])

    def test_invalid_name(self):
        person = Person(2, "Frederick", 30)
        person.add_email(Email(2, "queen@example.com"))
        errors = self.dao.isValidToInclude(person)
        self.assertIn("Nome deve conter ao menos duas partes compostas apenas por letras", errors)

    def test_invalid_age(self):
        person = Person(3, "Frederick Bulsara", 201)
        person.add_email(Email(3, "queen@example.com"))
        errors = self.dao.isValidToInclude(person)
        self.assertIn("Idade deve estar no intervalo de 1 a 200", errors)

    def test_no_email(self):
        person = Person(4, "Frederick Bulsara", 30)
        errors = self.dao.isValidToInclude(person)
        self.assertIn("Person deve ter ao menos um Email associado", errors)

    def test_invalid_email_format(self):
        person = Person(5, "Frederick Bulsara", 30)
        person.add_email(Email(4, "queenexample.com"))  # Email sem '@'
        errors = self.dao.isValidToInclude(person)
        self.assertIn("Email deve estar no formato correto (ex: name@example.com)", errors)

    def test_multiple_errors(self):
        person = Person(6, "Frederick", 300)
        person.add_email(Email(5, "queenexample.com"))
        errors = self.dao.isValidToInclude(person)
        self.assertEqual(len(errors), 3)
        self.assertIn("Nome deve conter ao menos duas partes compostas apenas por letras", errors)
        self.assertIn("Idade deve estar no intervalo de 1 a 200", errors)
        self.assertIn("Email deve estar no formato correto (ex: name@example.com)", errors)

if __name__ == '__main__':
    unittest.main()
