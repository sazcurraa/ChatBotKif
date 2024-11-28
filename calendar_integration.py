import base64
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import datetime

# Archivo de credenciales y configuración de Google API
SERVICE_ACCOUNT_FILE = 'C:/Users/User/OneDrive/Escritorio/TPSanti/credentials.json'
SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/gmail.send'
]

# Token de Telegram
TELEGRAM_TOKEN = '7942086608:AAFvJ4paJveIhB5BihpelJwkhlPh9ebB-WM'

# Inicialización de credenciales y servicios de Google
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

calendar_service = build('calendar', 'v3', credentials=credentials)
calendar_id = 'santi.1234.azcurra@gmail.com'

# Comando para agendar un evento
async def agendar_evento(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args  # Argumentos después del comando
        if len(args) < 5:
            await update.message.reply_text(
                "Uso: /agendar <resumen> <ubicación> <descripción> <inicio (YYYY-MM-DDTHH:MM:SS-03:00)> <fin (YYYY-MM-DDTHH:MM:SS-03:00)>"
            )
            return

        summary, location, description, start_time, end_time = args

        event = {
            'summary': summary,
            'location': location,
            'description': description,
            'start': {
                'dateTime': start_time,
                'timeZone': 'America/Argentina/Buenos_Aires',
            },
            'end': {
                'dateTime': end_time,
                'timeZone': 'America/Argentina/Buenos_Aires',
            },
        }

        event = calendar_service.events().insert(calendarId=calendar_id, body=event).execute()
        await update.message.reply_text(f'Evento creado: {event.get("htmlLink")}')
    except HttpError as error:
        await update.message.reply_text(f'Error al crear el evento: {error}')

# Comando para leer eventos
async def leer_eventos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        future = (datetime.datetime.utcnow() + datetime.timedelta(days=7)).isoformat() + 'Z'

        events_result = calendar_service.events().list(
            calendarId=calendar_id,
            timeMin=now,
            timeMax=future,
            maxResults=10,
            singleEvents=True,
            orderBy='startTime'
        ).execute()

        events = events_result.get('items', [])

        if not events:
            await update.message.reply_text('No hay eventos próximos.')
        else:
            message = "Eventos encontrados:\n"
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                message += f"- {event['summary']} (Inicio: {start})\n"
            await update.message.reply_text(message)
    except HttpError as error:
        await update.message.reply_text(f'Error al leer los eventos: {error}')

# Comando para iniciar el bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! Soy tu asistente de calendario. Estos son los comandos disponibles:\n"
        "/start - Mostrar este mensaje\n"
        "/agendar - Crear un evento en tu calendario\n"
        "/leer - Ver los próximos eventos en tu calendario"
    )

# Manejador de texto para mensajes no relacionados con comandos
async def manejar_texto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("No entiendo este mensaje. Usa /start para ver los comandos disponibles.")

# Función principal del bot
def main():
    # Crear la aplicación
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Registro de comandos
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('agendar', agendar_evento))
    application.add_handler(CommandHandler('leer', leer_eventos))

    # Manejador de texto para mensajes que no sean comandos
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_texto))

    # Iniciar el bot
    application.run_polling()

if __name__ == "__main__":
    main()
