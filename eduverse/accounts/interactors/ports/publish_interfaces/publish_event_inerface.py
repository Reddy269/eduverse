from abc import ABC, abstractmethod

class PublishEventInerface(ABC):
    @abstractmethod
    def send_signal(self, event):
        pass
