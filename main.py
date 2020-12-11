"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    h = float(input('Digite uma altura: '))
    print(f'Se você for homem o seu peso ideal é {72.7 * h - 58}.')
    print(f'Se você for mulher o seu peso ideal é {62.1 * h - 44.7}.')

if __name__ == '__main__':
    main()
