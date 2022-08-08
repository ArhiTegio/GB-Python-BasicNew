import logging

from Config.config import Config
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from Models.model import Model
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

AUTH, \
__MAIN__, \
ACTION, \
CONFIRMATION = range(4)

pas = ''
act = ''

def start(update, context):
    global pas
    pas = ''
    update.message.reply_text(
        'Добрый день. Список задач.\n Введите пароль: ',)
    return AUTH


def auth(update, _):
    global pas
    global act
    user = update.message.from_user
    logger.info("Пользователь %s рассказал: %s", user.first_name, update.message.text)
    if update.message.text == Model.read(Config.read()['db_identity'])[0]['pas'] or pas == Model.read(Config.read()['db_identity'])[0]['pas']:
        if len(pas) == 0:
            pas = update.message.text
        data = Model.read(Config.read()['db_data'])
        if act == 'Создать':
            data.insert(0, {'title': update.message.text, 'state': 'Новое',})
        elif act == 'Удалить':
            ipt = update.message.text
            ipt = ''.join([e for e in ipt if str.isdigit(e)])
            if len(ipt) > 0:
                idx = int(ipt)
                if idx < len(data):
                    data[idx]['state'] = 'Удалено'
        elif act == 'Выполнено':
            ipt = update.message.text
            ipt = ''.join([e for e in ipt if str.isdigit(e)])
            if len(ipt) > 0:
                idx = int(ipt)
                if idx < len(data) and data[idx]['state'] != 'Удалено':
                    data[idx]['state'] = 'Выполнено'
        elif act == 'Приоритет':
            ipt = update.message.text
            ipt = ipt.split(' ')
            ipt = [''.join([e for e in i if str.isdigit(e)]) for i in ipt]
            if len(ipt) == 2 and len(ipt[0]) > 0 and len(ipt[1]) > 0:
                idx_start = int(ipt[0])
                idx_end = int(ipt[1])
                if idx_start < len(data) and idx_end < len(data):
                    val = data[idx_start]
                    del data[idx_start]
                    data.insert(idx_end, val)
        elif act == 'Изменить':
            ipt = update.message.text
            ipt = ipt.split(' ')
            if len(ipt) > 1:
                val = ' '.join(ipt[1:])
                idx = ''.join([e for e in ipt[0] if str.isdigit(e)])
                if len(idx) > 0 and len(val) > 0:
                    idx = int(idx)
                    if idx < len(data):
                        data[idx]['title'] = val
        Model.write(data, Config.read()['db_data'])
        reply_keyboard = [['Создать', 'Изменить', 'Выполнено', 'Удалить', 'Приоритет', 'Выйти']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

        data = '\n'.join([f'{idx}. {e["title"]} - {e["state"]}' for idx, e in enumerate(data) if e['state'] != 'Удалено'])
        msg = 'Нет списка дел.' if len(data) == 0 else 'Список дел:'
        update.message.reply_text(f'Добро пожаловать.\n{msg}\n{data}', reply_markup=markup_key,)
        # Заканчиваем разговор.
        return ACTION
    else:
        update.message.reply_text('Соединение завершино.')
        return ConversationHandler.END


def main(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал биографию или рассказ пользователя
    logger.info("Пользователь %s рассказал: %s", user.first_name, update.message.text)
    # Отвечаем на то что пользователь рассказал.
    return ConversationHandler.END


def action(update, _):
    global act
    act = update.message.text
    if update.message.text == 'Выйти':
        reply_keyboard = [['Да', 'Нет',]]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text(f'Подтверждаите.', reply_markup=markup_key, )
        return CONFIRMATION
    elif update.message.text == 'Создать':
        update.message.reply_text('Введите название: ', )
        return AUTH
    elif update.message.text == 'Удалить':
        update.message.reply_text('Введите позицию: ')
        return AUTH
    elif update.message.text == 'Выполнено':
        update.message.reply_text('Введите позицию: ')
        return AUTH
    elif update.message.text == 'Приоритет':
        update.message.reply_text('Введите начальную и конечную позиции через пробел: ')
        return AUTH
    elif update.message.text == 'Изменить':
        update.message.reply_text('Введите номер позиции и начио необходимо изменить через пробел: ')
        return AUTH
    else:
        return AUTH


def confirmation(update, _):
    if act == 'Выйти':
        if update.message.text == 'Да':
            update.message.reply_text('Досвидание. ', )
            return ConversationHandler.END
        else:
            update.message.reply_text('Нажмите любую клавишу. ', )
            return AUTH
    return AUTH


def cancel(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(Config.read()['TOKEN'])
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            AUTH: [MessageHandler(Filters.regex(''), auth)],
            __MAIN__: [MessageHandler(Filters.regex('^(Создать|Изменить|Выполнено|Удалить|Изменить приоритет|Выйти)$'), main)],
            ACTION: [MessageHandler(Filters.regex(''), action)],
            CONFIRMATION: [MessageHandler(Filters.regex(''), confirmation)]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()
