import time
from plyer import notification

INTERVALO_SEGUNDOS = 3600
print("Água! iniciado com sucesso. Você receberá uma notificação a cada hora para se lembrar de beber água.")

while True:
    time.sleep(INTERVALO_SEGUNDOS)

    notification.notify(
        title='Pausa para alguns goles!',
        message='De gole em gole a pele fica hidratada!',
        app_name='Água!',
        timeout=10  # Duration in seconds
    )
