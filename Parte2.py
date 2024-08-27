import sentry_sdk

# Inicializa Sentry con tu DSN
sentry_sdk.init(
    dsn="https://3699533e6e2074468190a2bb3cbf9c5b@o4507846538035200.ingest.us.sentry.io/4507846577225728",
    # Configura la tasa de muestreo de los eventos
    traces_sample_rate=1.0,
    # Activa el envio de informacion de rendimiento
    send_default_pii=True
)

def funcion_que_falla():
    return 1 / 0  # Esta linea generara un error de division por cero

try:
    funcion_que_falla()
except Exception as e:
    # Captura y envia el error a Sentry
    sentry_sdk.capture_exception(e)
    print("El error ha sido reportado a Sentry.")

