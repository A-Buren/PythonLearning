USER_DATA_SCHEME = {
    "type" : "object",
    "properties": {
        "id": {"type": "number"},
        "email": {"type": "string"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "avatar": {"type": "string"}
    },
    "required": ["id","email","first_name","last_name", "avatar"]
}

RESOURCE_DATA_SCHEME = {
    "type" : "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "year": {"type": "number"},
        "color": {"type": "string"},
        "pantone_value": {"type": "string"}
    },
    "required": ["id","name","year","color", "pantone_value"]
}


CREATED_USER_SCHEME = {
    "type" : "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"}
        # "createdAt": {"type": "datetime"}     #Закомментировал, тк сначала сделал сам схему, а потом Рома в видео не стал включать это поле.
                                                #Аналогично не стал добавлять подобные поля в схему UPDATE_USER_SCHEME.
    },
    "required": ["id"]
}


UPDATED_USER_SCHEME = {
    "type" : "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"}
    },
    "required": ["name", "job"]
}


REGISTERED_USER_SCHEME = {
    "type" : "object",
    "properties": {
        "id": {"type": "number"},
        "token": {"type": "string"}
    },
    "required": ["id", "token"]
}


UNSUCCESSFUL_REGISTER_SCHEME = {
    "type" : "object",
    "properties": {
        "error": {"type": "string"}
    },
    "required": ["error"]
}

LOGIN_USER_SCHEME = {
    "type" : "object",
    "properties": {
        "token": {"type": "string"}
    },
    "required": ["token"]
}


