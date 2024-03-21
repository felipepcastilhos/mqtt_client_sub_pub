# Importa o módulo paho.mqtt.client como mqtt
import paho.mqtt.client as mqtt

# Cria uma instância do cliente MQTT com o nome 'meu_publisher'
mqtt_client = mqtt.Client('meu_publisher')

# Conecta-se ao broker MQTT local na porta 1883
mqtt_client.connect(host="localhost", port=1883)

# Publica uma mensagem no tópico '/msgs' com a carga útil '{"minha": "mensagem"}'
mqtt_client.publish(topic="/msgs", payload='{ "minha": "mensagem" }')

# Imprime uma mensagem indicando que o processo de publicação terminou
print('end')