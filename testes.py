import unittest
import requests


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://localhost:5000'

        requests.get(f'{self.base_url}/apagar')

        requests.get(f'{self.base_url}/criar')

    def tearDown(self):
        requests.get(f'{self.base_url}/apagar')
        pass

    def test_criar_banco_url(self):
        response = requests.get(f'{self.base_url}/criar')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'criado')

    def test_apagar_banco_url(self):
        response = requests.get(f'{self.base_url}/apagar')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'apagado')

    def test_buscar_nome_filme(self):
        response = requests.get(f'{self.base_url}/filme?name=taxi%20driver')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['nome'], 'Taxi Driver')


if __name__ == '__main__':
    unittest.main()