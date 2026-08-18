import time
from plyer import notification

notification.notify(
    title='Pausa para alguns goles!',
    message='De gole em gole a pele fica hidratada!',
    app_name='Água!',
    timeout=10  # Duration in seconds
)
