from accounts.interactors.ports.publish_interfaces import PublishEventInerface
from django.dispatch import Signal
from accounts.interactors.ports.publish_interfaces import StudentRegistredDTO

class SendSignalAdapter(PublishEventInerface):
    def send_signal(self, event: StudentRegistredDTO) -> None:
        Signal().send(sender=type(event), event=event)
        return
