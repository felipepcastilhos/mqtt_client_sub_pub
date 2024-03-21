import time  # Importa o módulo time para lidar com o tempo
from application.configs.broker_configs import mqtt_broker_configs  # Importa as configurações do broker MQTT
from .mqtt_connection.mqtt_client_connection import MqttClientConnection  # Importa a classe MqttClientConnection do módulo mqtt_client_connection

def start(): 
    # Cria um objeto de conexão com o MQTT = uma instância de MqttClientConnection com as configurações do broker MQTT
    mqtt_client_connection = MqttClientConnection(
        mqtt_broker_configs["HOST"],            # Passa o endereço IP do broker MQTT
        mqtt_broker_configs["PORT"],            # Passa a porta do broker MQTT
        mqtt_broker_configs["CLIENT_NAME"],     # Passa o nome do cliente MQTT
        mqtt_broker_configs["KEEPALIVE"]        # Passa o tempo de vida da conexão MQTT
    )
    # Inicia a conexão com o broker MQTT
    mqtt_client_connection.start_connection()
  
    # Mantém o programa em execução indefinidamente/looping
    while True:
        time.sleep(0.001)  # Espera um curto período de tempo para evitar consumo excessivo de CPU