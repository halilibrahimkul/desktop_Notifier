from notifypy import Notify

notification = Notify()
notification.application_name='Desk-Notifier'
notification.title = 'Uygulamasından Selamlar.'
notification.message = "Okuduğunuz için teşekkür ederiz.İyi günler."
notification.icon='X icon application.png'
notification.send()
