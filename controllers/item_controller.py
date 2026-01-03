from sanic import response
from models.item_model import get_all_items, get_item_by_id, create_item, update_item, delete_item
from sanic.log import logger
from sanic.response import json
from utils.auth_decorator import protected

async def test(request):
    return response.json({"message": "Hello, Sanicaa!"})

@protected()
async def list_items(request):
    items = get_all_items()
    logger.info(f"Datos obtenidos: {items}")
    return response.json(items)

@protected()
async def get_item(request, item_id):
    item = get_item_by_id(item_id)
    if item:
        return response.json(item)
    return response.json({"error": "Item no encontrado"}, status=404)

@protected()
async def create_new_item(request):
    data = request.json
    create_item(data["name"], data["description"], data["price"])
    return response.json({"message": "Item creado correctamente"}, status=201)

@protected()
async def update_existing_item(request, item_id):
    data = request.json
    update_item(item_id, data["name"], data["description"], data["price"])
    return response.json({"message": "Item actualizado correctamente"})

@protected()
async def delete_existing_item(request, item_id):
    delete_item(item_id)
    return response.json({"message": "Item eliminado correctamente"})