from helper import generate_ingredients

#RESPONSES

DUP_USER_RESPONSE = {
        "success": False,
        "message": "User already exists"
    }

MIS_FIELD_RESPONSE = {
        "success": False,
        "message": "Email, password and name are required fields"
    }
LOGIN_ERROR_RESPONSE = {
        'success': False,
        'message': 'email or password are incorrect'
    }

UNAUTHORIZED_RESPONSE = {
        "success": False,
        "message": "You should be authorised"
}

EMPTY_INGREDIENTS_RESPONSE = {
    "success": False,
    "message": "Ingredient ids must be provided"
}

INVALID_INGREDIENTS_RESPONSE = {
    "success": False,
    "message": "One or more ids provided are incorrect"
}

NO_AUTHORIZED_USER = {
    "success": False,
    "message": "You should be authorised"
}
#INGREDIENTS DATA

VALID_INGREDIENTS_PAYLOAD = {
    'ingredients': generate_ingredients()
}

EMPTY_INGREDIENTS_PAYLOAD = {
    'ingredients': []
}

INVALID_INGREDIENTS_PAYLOAD = {
    "ingredients": ["invalid_id_1", "invalid_id_2"]
}
