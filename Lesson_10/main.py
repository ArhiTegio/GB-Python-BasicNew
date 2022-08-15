import logging
import random

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


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

choice_program = ''
g1 = ''
g1_list = []
with open (Config.read()['db_data']) as file:
    for line in file:
        g1_list.append(line.split('. ')[-1].replace('\n', ''))
g2_pos = 0
g2_pos_max = 0
g2_field = []
player = []
comp = []
state = {}

START, \
CHOICE, \
__MAIN__, \
ACTION, \
CONFIRMATION = range(5)


def start(update, context):
    reply_keyboard = [['Конфеты', 'Быки и коровы', ]]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(f'Выберите.', reply_markup=markup_key, )
    return __MAIN__


def choice(update, context):
    global choice_program
    choice_program = update.message.text

    reply_keyboard = [['Да', 'Нет', ]]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(f'Подтверждаите.', reply_markup=markup_key, )
    return __MAIN__


def main(update, context):
    global choice_program, g1, g1_list, g2_pos, g2_pos_max, player, comp, state
    if choice_program == '':
        choice_program = update.message.text

    if choice_program == 'Быки и коровы':
        if g1 == '':
            g1 = random.choice(g1_list)
        else:
            word = update.message.text
            if g1 == word:
                update.message.reply_text(f'Поздравляю. Вы отгадали слово {g1}.', )
                return ConversationHandler.END
            else:
                bulls = 0
                cows = 0
                dic = {}
                dic_word = {}
                for idx in range(len(word)):
                    ch = word[idx]
                    if ch in dic_word.keys():
                        dic_word[ch] += 1
                    else:
                        dic_word[ch] = 1

                for idx in range(len(g1)):
                    ch = g1[idx]
                    if ch in dic.keys():
                        dic[ch] += 1
                    else:
                        dic[ch] = 1

                    if len(word) > idx and ch == word[idx]:
                        bulls += 1
                    elif len(word) > idx and ch in dic_word.keys() and dic[ch] <= dic_word[ch]:
                        cows += 1

                update.message.reply_text(f'Найдено быков {bulls} и коров {cows}.', )
                update.message.reply_text(f'Отгадайте слово {"".join(["*" for _ in g1])}.', )
                return __MAIN__

        update.message.reply_text(f'Отгадайте слово {"".join(["*" for _ in g1])}.', )
        return __MAIN__
    elif choice_program == 'Конфеты':
        if g2_pos == 0:
            g2_pos = random.randint(30, 300)
            g2_pos_max = g2_pos
            with open(Config.read()['db_state']) as file:
                for line in file:
                    sp = line.split(':')
                    state[int(sp[0])] = float(sp[1])

        update.message.reply_text(f'{g2_pos}/{g2_pos_max}: ', )

        step = update.message.text
        digits = ''.join([e for e in step if str.isdigit(e)])
        if 28 >= len(digits) > 0:
            digits = int(digits)
            g2_pos -= digits
            update.message.reply_text(f'{g2_pos}/{g2_pos_max}: ', )
            player.append(g2_pos)
            if g2_pos <= 0:
                for e in player:
                    if e in state.keys():
                        state[e] += 100
                    else:
                        state[e] = 100

                for e in comp:
                    if e in state.keys():
                        state[e] -= 20
                    else:
                        state[e] = -20
                save_state(state)
                update.message.reply_text(f'Вы выйграли ', )
                return ConversationHandler.END
            update.message.reply_text(f'Ход аппанента: ', )
            pos = g2_pos - 28
            steps = [e for e in range(0 if pos == 0 else pos,  g2_pos)]
            st = [state[e] if e in state.keys() else 0 for e in range(0 if pos == 0 else pos,  g2_pos)]
            step = random.choices(population=steps, k=1, weights=st)
            comp.append(step[0])
            g2_pos = step[0]
            update.message.reply_text(f'{g2_pos}/{g2_pos_max}: ', )
            if g2_pos <= 0:
                for e in comp:
                    if e in state.keys():
                        state[e] += 20
                    else:
                        state[e] = 20
                for e in player:
                    if e in state.keys():
                        state[e] -= 20
                    else:
                        state[e] = -20
                save_state(state)
                update.message.reply_text(f'Опонент выйграл ', )
                return ConversationHandler.END

            update.message.reply_text(f'Ход игрока: ', )
            update.message.reply_text(f'Введите количество конфет (не более 28): ', )
            return __MAIN__
            pass
        else:
            update.message.reply_text(f'Ход игрока: ', )
            update.message.reply_text(f'Введите количество конфет (не более 28): ', )
            return __MAIN__


def save_state(state):
    with open(Config.read()['db_state'], 'w') as fp:
        fp.write('\n'.join([f'{k}:{v}' for k,v in state.items()]))

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
            START: [MessageHandler(Filters.regex(''), start)],
            CHOICE: [MessageHandler(Filters.regex('^(Конфеты|Быки и коровы)$'), choice)],
            __MAIN__: [MessageHandler(Filters.regex(''), main)],
            #ACTION: [MessageHandler(Filters.regex(''), action)],
            #CONFIRMATION: [MessageHandler(Filters.regex(''), confirmation)]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()
