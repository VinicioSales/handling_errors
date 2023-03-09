import logging

# Configuração básica do registro de mensagens
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Criação do manipulador para escrever as mensagens em um arquivo
handler = logging.FileHandler('log.log')
handler.setLevel(logging.DEBUG)

# Formatação das mensagens que serão registradas no arquivo
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Adição do manipulador à configuração do logging
logger = logging.getLogger()
logger.addHandler(handler)

# Registro de mensagens de exemplo
logger.debug('Mensagem de debug')
logger.info('Mensagem de informação')
logger.warning('Mensagem de aviso')
logger.error('Mensagem de erro')
logger.critical('Mensagem crítica')

#NOTE - Exemplo Prático
try:
    resposta = 1 / 0
except Exception as error:
    logger.debug(error)