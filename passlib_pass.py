from passlib.context import CryptContext

contexto = CryptContext(
    schemes = ["pbkdf2_sha256"],
    default = "pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=3000
)

def encry(password):
    texto_encriptado = contexto.hash(password)
    return texto_encriptado

def verify_encry(password,texto_encriptado):
    verify_text = contexto.verify(password, texto_encriptado)
    return verify_text