def create_pet_payload(pet_id, name, status):
    return {
        "id": pet_id,
        "category": {"id": 0, "name": "string"},
        "name": name,
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": status
    }
