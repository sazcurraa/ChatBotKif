Bot de Telegram para Gestión de Eventos 
Este proyecto es un bot de Telegram que permite a los usuarios crear y consultar eventos en su Google Calendar mediante comandos. Utiliza la API de Google Calendar y la API de Gmail para la autenticación y el envío de correos.

Características
Crear eventos: Permite programar eventos en el Google Calendar especificando resumen, ubicación, descripción, y horarios de inicio y fin.
Leer eventos: Consulta y muestra los próximos eventos en el calendario del usuario.
Comando de inicio: Presenta las opciones y funcionalidades disponibles para el usuario.
Tecnologías utilizadas
Python: Lenguaje de programación.
Telegram Bot API: Para la interacción de usuarios a través de Telegram.
Google APIs (Calendar & Gmail): Para la gestión de eventos y autenticación.
Google OAuth2: Para el manejo de credenciales de acceso.
Requisitos previos
Python 3.7 o superior.
Instalación de librerías de Python:
google-auth
google-auth-oauthlib
google-auth-httplib2
google-api-python-client
python-telegram-bot
Puedes instalar todas las dependencias usando pip:

bash
Copiar código
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client python-telegram-bot
Configuración
1. Obtención de credenciales de Google
Dirígete a la Google Cloud Console.
Crea un proyecto y habilita la API de Google Calendar.
Genera un archivo de credenciales (credentials.json) y descárgalo en tu máquina.
2. Configuración del bot de Telegram
Crea un bot en Telegram mediante el BotFather y obtén el token de acceso.
Sustituye el token en la variable TELEGRAM_TOKEN del script.
3. Configuración del archivo de credenciales
Asegúrate de que la ruta del archivo de credenciales (SERVICE_ACCOUNT_FILE) sea correcta y accesible desde tu entorno.

Uso
Ejecuta el script:

bash
Copiar código
python nombre_del_script.py
Interacción con el bot:

/start: Muestra un mensaje de bienvenida y las instrucciones de uso.
/agendar <resumen> <ubicación> <descripción> <inicio (YYYY-MM-DDTHH:MM:SS-03:00)> <fin (YYYY-MM-DDTHH:MM:SS-03:00)>: Crea un nuevo evento en el calendario.
/leer: Muestra los próximos eventos en el calendario.
Ejemplo de comandos
Para agendar un evento:

text
Copiar código
/agendar Reunión Oficina "Reunión con el equipo" "2024-12-01T14:00:00-03:00" "2024-12-01T15:00:00-03:00"
Para leer eventos:

text
Copiar código
/leer
Notas
Asegúrate de que la cuenta de Google usada tenga acceso al calendario especificado en calendar_id.
El bot solo responderá a mensajes de texto relacionados con comandos.
Contribuciones
Si deseas contribuir al proyecto, por favor, envía tus sugerencias y mejoras a través de un pull request en GitHub.

Licencia
Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo LICENSE.

Este README.md te dará una guía clara sobre cómo configurar y utilizar tu bot. Si necesitas personalizar algún detalle o agregar instrucciones adicionales, házmelo saber.
