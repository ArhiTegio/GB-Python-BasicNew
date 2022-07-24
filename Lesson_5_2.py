#2- Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""
#https://music.yandex.ru/album/3874680/track/43765563


from CandyStrategyWork import TypePlayer, Player, CandyStrategy


p = 100
#for p in range(75, 100):
    #for _ in range(28):
g = CandyStrategy(players=[
                    Player(TypePlayer.human, name='1name1'),
                    Player(type_player=TypePlayer.robot, name='2name2'),
                ])
#g.params['candys'] = p
#g.params['candys_prestep'] = p
g.Start()
