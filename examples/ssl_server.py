import logging
import ssl
from secure_smtpd import SMTPServer, FakeCredentialValidator, LOG_NAME

class SSLSMTPServer(SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, message_data):
        print(message_data)

logger = logging.getLogger( LOG_NAME )
logger.setLevel(logging.INFO)



server = SSLSMTPServer(
    ('0.0.0.0', 1026),
    None,
    require_authentication=False,
    ssl=True,
    keyfile='server.key',
    certfile='server.crt',
    credential_validator=FakeCredentialValidator(),
    maximum_execution_time = 1.0
    )

server.run()
