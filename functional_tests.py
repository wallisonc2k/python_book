from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith ouviu falar de um novo aplicativo de tarefas online legal.
        # para verificar sua página inicial
        self.browser.get('http://localhost:8000')


        # Ela percebe o título da página e as listas de tarefas de menção de cabeçalho
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        # Ela é convidada a inserir um item de tarefa imediatamente


        # Ela digita "Compre penas de pavão" em uma caixa de texto (o hobby de Edith está amarrando iscas de pesca com mosca)

        # Quando ela pressiona enter, a página é atualizada e agora a página lista
        # "1: Compre penas de pavão" como um item de uma lista de tarefas

        # Ainda existe uma caixa de texto convidando-a para adicionar outro item. Ela
        # digita "Use penas de pavão para fazer uma mosca" (Edith é muito metódica)

        # A página é atualizada novamente e agora mostra os dois itens em sua lista
        # Edith se pergunta se o site se lembrará de sua lista. Então ela vê
        # que o site gerou um URL exclusivo para ela - há algumas
        # texto explicativo para esse efeito.

        # Ela visita esse URL - sua lista de tarefas ainda está lá.

        # Satisfeita, ela volta a dormir

if __name__ == '__main__':
    unittest.main(warnings='ignore')