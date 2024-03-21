# Importa a biblioteca paho.mqtt.client e a renomeia como mqtt
import paho.mqtt.client as mqtt
from .callbacks import on_connect, on_subscribe, on_message

# Encapsula as funcionalidades relacionadas à conexão e comunicação com o broker MQTT, 
# Fornecendo métodos para iniciar e encerrar a conexão, enquanto gerencia os detalhes de implementação, como a configuração do cliente MQTT e a definição das funções de callback
class MqttClientConnection:
    # Método construtor com todos elementos das configurações do broker (permite que você forneça valores iniciais para os atributos da classe quando a instância é criada)
    def __init__(self, broker_ip: str, port: int, client_name: str, keepalive=60): 
        # Inicializa as variáveis de conexão MQTT. Estes atributos são privados para essa classe (broker_ip)
        self.__broker_ip = broker_ip  # Endereço IP do broker MQTT
        self.__port = port  # Porta do broker MQTT
        self.__client_name = client_name  # Nome do cliente MQTT
        self.__keepalive = keepalive  # Tempo de vida da conexão MQTT
        self.__mqtt_client = None # Possibilita mqtt_client como atributo
 
    def start_connection(self):
        # Cria uma instância do cliente MQTT. O Broker enxerga esse projeto a partir desse name
        mqtt_client = mqtt.Client(self.__client_name) #.Client da biblioteca paho

        # Define as funções de callbacks
        mqtt_client.on_connect = on_connect 
        mqtt_client.on_subscribe = on_subscribe
        mqtt_client.on_message = on_message

        # Conecta-se ao broker MQTT
        mqtt_client.connect(host=self.__broker_ip, port=self.__port, keepalive=self.__keepalive)

        # Inicia o loop de comunicação MQTT em uma thread separada
        self.__mqtt_client = mqtt_client
        # Inicia o loop para todo momento verificar se recebeu mensagens do broker  
        self.__mqtt_client.loop_start() 

    def end_connection(self):
        # Encerra a conexão MQTT
        try:
            self.__mqtt_client.loop_stop() # Para loop
            self.__mqtt_client.disconnect() # Disconecta cliente
            return True  # Retorna True se a desconexão for bem-sucedida
        except:
            return False  # Retorna False se ocorrer um erro ao desconectar
