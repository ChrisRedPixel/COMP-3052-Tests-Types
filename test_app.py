from app import autenticar_usuario

#CP-01: Login exitoso
def test_login_exitoso():
 resultado = autenticar_usuario("admin", "1234")
 assert resultado["success"] == True
 assert resultado["message"] == "Acceso concedido"
 assert resultado["response_time_ms"] > 0

#CP-02: Usuario Vacio
def test_usuario_vacio():
 resultado = autenticar_usuario("", "1234")
 assert resultado["success"] == False
 assert resultado["message"] == "Usuario y contraseña son requeridos"

#CP-03: Contraseña Vacía
def test_contrasena_vacia():
 resultado = autenticar_usuario("admin", "")
 assert resultado["success"] == False
 assert resultado["message"] == "Usuario y contraseña son requeridos"

#CP-04: Usuario Inexistente
def test_usuario_inexistente():
 resultado = autenticar_usuario("pedro", "1234")
 assert resultado["success"] == False
 assert resultado["message"] == "Usuario no existe"

#CP-05: Contraseña Incorrecta
def test_contrasena_incorrecta():
 resultado = autenticar_usuario("admin", "9999")
 assert resultado["success"] == False
 assert resultado["message"] == "Contraseña incorrecta"

#CP-06: Tiempo de Respuesta
def test_tiempo_respuesta():
 resultado = autenticar_usuario("admin", "1234")
 assert resultado["response_time_ms"] > 0

#CP-07: Estructura de Salida
def test_estructura_salida():
 resultado = autenticar_usuario("admin", "1234")
 assert "success" in resultado
 assert "message" in resultado
 assert "response_time_ms" in resultado