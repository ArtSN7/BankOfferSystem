from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup
import asyncio



# ------------------------------------------

# starting function

hello_text = """Вы зарегистрировались в системе «Экспобонус»! Теперь вам доступны бонусы, скидки и привилегии всех компаний партнеров Экспобанка!)
Для старта просим вас подтвердить согласие на обработку, хранение и передачу персональных данных компаниям партнерам Экспобанка! """

reply_keyboard = [['/yes'], ['/no']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

async def start(update, context):
    user = update.effective_user

    await update.message.reply_html(rf"Привет {user.mention_html()}! {hello_text}", reply_markup=markup)



async def confirm(update, context):
    user = update.effective_user

    await update.message.reply_html(rf"Привет {user.mention_html()}! Скиньте, пожалуйста, номер телефона, который Вам привязан к Вашей учетной записи - благодаря нему мы сможем Вас индифицировать.",)

    return 1



first_stuff_text = """Мы предлагаем вам выгодно подобрать новый автомобиль у нашего партнера EXPOCAR, с комплектом страховок КАСКО+ОСАГО от Д2 страхование со скидкой 30%!"""

reply_keyboard_two = [["/ACCEPT", "/REJECT"]]
markup_two=ReplyKeyboardMarkup(reply_keyboard_two, one_time_keyboard=True)

async def first_response(update, context):
    code = update.message.text

    await update.message.reply_text(f"Спасибо! Вы успешно были подключены, теперь мы готовы Вам помогать.")

    await update.message.reply_text(first_stuff_text, reply_markup=markup_two)

    return ConversationHandler.END




second_stuff_text = """Катайтесь с выгодой!
Заезжайте с мая по август в шинный сервис Лизинг 2 ( операционный лизинг) и возвращайте до 10% Экспобонусами. 
РЕКЛАМА: Рекламодатель ООО «Лизинг 2 ( операционный лизинг)» (18+) ОГРН.."""


async def first_accept(update, context):
    await update.message.reply_text("Хороший выбор! Менеджер с Вами свяжется в скором времени",)

    await asyncio.sleep(60)

    await update.message.reply_text(second_stuff_text, reply_markup=markup_two)





async def offer_reject(update, context):
    await update.message.reply_text("Мы постараемся предлагать более релевантные предложения!",)

# ------------------------------------------



# ------------------------------------------
async def stop(update, context):
    await update.message.reply_text(":)")
    return ConversationHandler.END


async def refuse(update, context):
    await update.message.reply_text("Жаль, тогда до свидания!")


async def response(update, context):
    await update.message.reply_text("К сожалению, я не могу Вам ответить. Я был создан лишь для того, чтобы отправлять Вам достойные Вас предложения от Экспобанк и наших партнеров.")

# ------------------------------------------



def main():
    application = Application.builder().token("7423830416:AAFnYZUP3yg-UBD8dYWsenrWawAGPaK94zY").build()

    application.add_handler(CommandHandler("start", start)) 
    application.add_handler(CommandHandler("no", refuse))


    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("yes", confirm)],

        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, first_response)],
        },

        fallbacks=[CommandHandler('stop', stop)]

    )


    application.add_handler(CommandHandler("ACCEPT", first_accept))
    application.add_handler(CommandHandler("REJECT", offer_reject))


    application.add_handler(conv_handler)


    text_handler = MessageHandler(filters.TEXT, response)

    application.add_handler(text_handler)

    # Запускаем приложение.
    application.run_polling()





# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()