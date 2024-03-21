# Importa a função start do arquivo main.py no pacote main dentro do pacote application
from application.main.main import start

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    # Chama a função start do arquivo main.py para iniciar o programa
    start()