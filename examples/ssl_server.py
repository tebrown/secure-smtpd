import logging
import ssl
from secure_smtpd import SMTPServer, FakeCredentialValidator, LOG_NAME

class SSLSMTPServer(SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, message_data):
        print(message_data)

logger = logging.getLogger( LOG_NAME )
logger.setLevel(logging.INFO)

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.load_cert_chain(certfile='server.crt', keyfile='server.key')

server = SSLSMTPServer(
    ('0.0.0.0', 1025),
    None,
    require_authentication=True,
    ssl=True,
    context=context,
    credential_validator=FakeCredentialValidator(),
    maximum_execution_time = 1.0
    )

server.run()
