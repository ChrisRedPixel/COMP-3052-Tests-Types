def autenticar_usuario(username, password):
    usuarios = {
        "admin": "1234",
        "javier": "python123",
        "estudiante": "abc123"
    }

    # Validar campos vacíos
    if username == "" or password == "":
        return {
            "success": False,
            "message": "Usuario y contraseña son requeridos",
            "response_time_ms": 50
        }

    # Validar usuario existente
    if username not in usuarios:
        return {
            "success": False,
            "message": "Usuario no existe",
            "response_time_ms": 70
        }

    # Validar contraseña
    if usuarios[username] != password:
        return {
            "success": False,
            "message": "Contraseña incorrecta",
            "response_time_ms": 80
        }

    # Caso exitoso
    return {
        "success": True,
        "message": "Acceso concedido",
        "response_time_ms": 60
    }