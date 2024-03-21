# Importa as configurações do broker MQTT do arquivo broker_configs.py
from application.configs.broker_configs import mqtt_broker_configs

# Execuções após as interrupções acontecerem 
# Função de callback chamada quando o cliente se conecta ao broker MQTT
def on_connect(client, userdata, flags, rc): # Propriedades exclusivas do método loop da biblioteca
    # Verifica se a conexão foi bem-sucedida
    if rc == 0: # Se não deu nenhum erro
        # Exibe uma mensagem indicando que o cliente foi conectado com sucesso
        print(f'Connected to MQTT Broker! Client: {client}')
        # Inscreve-se ao tópico especificado nas configurações do broker
        client.subscribe(mqtt_broker_configs["TOPIC"]) 
    else:
        # Exibe uma mensagem de erro se a conexão falhar
        print(f'Failed to connect, return code: ", rc, "\n') # 'rc' código de falha

# Função de callback chamada quando o cliente se inscreve em um tópico MQTT
def on_subscribe(client, userdata, mid, granted_qos):
    # Exibe uma mensagem indicando que o cliente foi inscrito no tópico especificado
    print(f'Client Subscribed at {mqtt_broker_configs["TOPIC"]}')
    # Exibe o QoS (Quality of Service) concedido / Segurança e informação da mensagem
    print(f'QOS: {granted_qos}')

# Função de callback chamada quando o cliente recebe uma mensagem MQTT
def on_message(client, userdata, message):
    # Exibe uma mensagem indicando que uma mensagem foi recebida
    print('Message received!')
    # Exibe informações sobre o cliente
    print(client)
    # Exibe o conteúdo da mensagem recebida
    print(message.payload)
