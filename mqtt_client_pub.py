import time
import json
import paho.mqtt.client as mqtt

# Define as configurações do broker MQTT
mqtt_broker_configs = {
    "HOST": "localhost",        # Endereço do broker MQTT
    "PORT": 1883,               # Porta do broker MQTT
    "CLIENT_NAME": "publisher", # Nome do cliente MQTT
    "KEEPALIVE": 60,            # Tempo de vida da conexão em segundos
    "TOPIC": "/msgs"            # Tópico MQTT para publicação de mensagens
}

def on_publish(client, userdata, result):
    print("Mensagem publicada com sucesso!")

def on_log(client, userdata, level, buf):
    print("Log do Broker MQTT:", buf)

# Cria um cliente MQTT
client = mqtt.Client(mqtt_broker_configs["CLIENT_NAME"])

# Define a função de callback para quando a mensagem for publicada
client.on_publish = on_publish

# Define a função de callback para o log do broker MQTT
client.on_log = on_log

# Conecta-se ao broker MQTT
client.connect(mqtt_broker_configs["HOST"], mqtt_broker_configs["PORT"], mqtt_broker_configs["KEEPALIVE"])

# Loop principal
while True:
    # Publica uma mensagem no tópico MQTT
    message = {"data": "mensagem de exemplo"}
    client.publish(mqtt_broker_configs["TOPIC"], json.dumps(message))

    # Aguarda 15 segundos antes de publicar a próxima mensagem
    time.sleep(15)
