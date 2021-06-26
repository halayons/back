# routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"^ws/$", consumers.PedidoConsumer.as_asgi()),
	re_path(r"^postWS/$", consumers.PostConsumer.as_asgi()),
	re_path(r"^postUser/$", consumers.PedidoUserConsumer.as_asgi())
]