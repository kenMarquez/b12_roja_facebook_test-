import requests
import json


class Usuario:
    nombre = ""

    def __init__(self):
        self.url = "https://graph.facebook.com/v2.8/me"
        self.access_token = "EAACEdEose0cBAPZAO8boT8vxgcj0qFpZAZC5IHuVZAJYa6h514357FyZB4akyIruKH1Se9ZBGtAcIqSjOQQXN647vsw4badlDi8frbbdqlAFzXuvlmKZBrgLFiZCyJRnqAcFRD01xDJKPYYafqZBtOMTZA5kAJjZBxlCiA13fhYnW3ZB8AZDZD"

    def get_info(self):
        params = {"access_token": self.access_token}
        resultado = requests.get(self.url, params=params).json()
        print(resultado)
        print("Hola")
        self.nombre = resultado["name"]
        return resultado



