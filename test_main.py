"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
import random
from unittest.mock import call, patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_main(self):
        """Função que testa se a saída do programa corresponde ao que foi especificado."""
        # Lista de valores que serão retornados pela função input.
        h = random.uniform(0.1, 10)
        input_returns = [h]
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            ph = 72.7 * h - 58
            pm = 62.1 * h - 44.7
            calls = [
                call(f'Se você for homem o seu peso ideal é {ph}.'),
                call(f'Se você for mulher o seu peso ideal é {pm}.')
            ]
            mock_print.assert_has_calls(calls)


if __name__ == '__main__':
    unittest.main()
