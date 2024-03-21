# ANOTAÇÕES:

- Mqtt publish and subscribe / biblioteca PAHO / broker MQTT Mosquitto / O que importa é como será INTERPRETADO(json, string) e O TÓPICO em que será inscrito, se está apato para enviar/receber dados pelo servidor mqtt; \
- Protocolo mqtt para comunicação leve entre computadores(sensores)-computadores/sensores; \
- Mosquitto é o programa/a ferramenta instalável para realizar a função do broker(broker MQTT que faz o gerenciamento de mensagens, fornecendo um servidor MQTT robusto e confiável para facilitar a troca de mensagens); \
- Biblioteca paho-mqtt para permitir codar por exemplo em python para que estes se comuniquem com o broker MQTT; \
- Publisher pode conectar rapidamente e desconectar, assim apenas conectando, publicando a mensagem e desconectando; \
- Cita o tópico primeiramente pelo subscribe a principio. Na verdade pode publicar antes e após inscrever, porém só irá receber os novos dados publicados após a inscrição estar realizada; \
- Componentes MQTT: \
  - Client MOQTT publisher; mensagem CONNECT. Agente retorna mensagem CONNACK para conexão estabelecida\
  - Client MQTT receiver; mensagem SUBSCRIBE\
  - Agente MQTT(broker): sistema backend que coordena mensagens entre os diferentes clientes; \
    - Responsabilidades: \
      -Receber e filtrar mensagens; \
      -Identificar os clientes inscritos em cada mensagem e enviar mensagens a eles; \
      -Autorizar e autenticar clientes MQTT; \
      -Transmitir mensagens a outros sistemas para análise posterior; \
      -Solucionar mensagens e sessões de clientes perdidas; \
- Servidor disponibilizado pelo broker MQTT Mosquitto; \
- host/IP: "192..." foi usado localhost; \
- Porta: 1883; \
- Tópico: '/msgs'; \

## Comandos:

- Comandos utilizados para instalação broker mosquitto no Linux Mint: \
  - "sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa"; \
  - "sudo apt-get update"; \
  - "sudo apt-get install mosquitto"; \
  - "sudo apt-get install mosquitto-clients"; \
- Comandos para instalação biblioteca paho-mqtt: \
  - "pip3 install paho-mqtt"; \
  - "pip3 install "paho-mqtt<2.0.0""; \
- Comandos Gerais: \
  - "mosquitto -v" (para ver o broker/servidor rodando, utilizado esta janela do terminal para monitorar após este código, apenas); \
  - "mosquitto_sub -h localhost -p 1883 -t '/msgs'" ("sub" para tratar dos receiver clients; "-h" para setar de que máquina(IP) desejamos esse acesso; "-p" para setar porta; '-t' para setar tópico); \
  - "mosquitto_pub -h localhost -p 1883 -t '/msgs' -m 'Ola Mundo!'" ("pub" para publicar); \
  - "cd "fileaddress"" para configurar o diretório da pasta em que está o arquivo a ser rodado; \
  - "python3 run.py" para rodar o script com nome do arquivo "run.py" escrito na linguagem python3; \
  - "mosquitto_sub --help"; \
  - "ctrl+c" para exit sub/pub topic; \

## supp links:

- https://aws.amazon.com/pt/what-is/mqtt/ \
- http://www.steves-internet-guide.com/install-mosquitto-linux/ \
- https://www.youtube.com/watch?v=6zwRG7FQX1k&t=16s (playlist) \
- https://github.com/programadorLhama/mqtt_python/tree/master/application \
- https://github.com/fcaon/mqtt-example-web-js \

- Arquivos **init**.py para conseguir importar e exportar as coisas com facilidade. Arquivos **init**.py são úteis porque facilitam a organização, o controle e a importação de módulos e pacotes em projetos Python, tornando o código mais limpo, modular e fácil de entender e manter; \
- Pasta configs para explicitar sobre o host, sobre o port e tópico; \
- /messages > /msgs; \
