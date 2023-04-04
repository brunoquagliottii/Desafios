import unittest
import requests

class TestAPI(unittest.TestCase):

    def test_criar_banco_url(self):
        response = requests.get('http://localhost:5000/criar')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'criado')

    def test_apagar_banco_url(self):
        response = requests.get('http://localhost:5000/apagar')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'apagado')

    def test_buscar_nome_filme(self):
        response = requests.get('http://localhost:5000/teste?name=taxi%20driver')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['nome'], 'Taxi Driver')

if __name__ == '__main__':
    unittest.main()