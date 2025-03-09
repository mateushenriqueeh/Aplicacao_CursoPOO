from abc import ABC, abstractmethod
class Entidade(ABC):
    @abstractmethod
    def exibir_info(self):
        pass
