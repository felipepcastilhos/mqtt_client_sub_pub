# Define as configurações do broker MQTT / Dicionário mqtt_broker_configs, descrevendo o propósito de cada configuração
mqtt_broker_configs = {
    "HOST": "localhost",  # Endereço do broker MQTT
    "PORT": 1883,         # Porta do broker MQTT
    "CLIENT_NAME": "client_project",  # Nome do cliente MQTT
    "KEEPALIVE": 15,       # Tempo de vida da conexão em segundos
    "TOPIC": "/msgs"  # Tópico MQTT para publicação/assinatura de mensagens
}