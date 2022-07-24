from enum import Enum
from typing import List, Union
import json
import random


class TypePlayer(Enum):
    human = 0
    robot = 1



class Player:
    def __init__(self, type_player:TypePlayer, name:str):
        self.type_player = type_player
        self.name = name
        self.is_win = False
        self.statistics = {}



class CandyStrategy:
    def __init__(self, players: List[Player]):
        self.players = players
        self.change_players = {0 if idx + 1 > len(self.players) - 1 else idx + 1: e for idx, e in
                               enumerate(list(range(len(self.players))))}

        self.params = {
            'candys': 2021,
            'get_max_candys': 28,
            'candys_prestep': 2021,
            'path_matrix': 'decision_matrix.json',
        }
        self.type_player_names = {TypePlayer.robot:"робот", TypePlayer.human:"человек"}
        self.matrix_greedy = self.load_matrix_greedy(self.params['path_matrix'])
        self.steps_matrix_greedy = list(self.matrix_greedy.keys())
        self.steps_matrix_greedy.sort()
        self.player_choise = random.randint(0, 1)
        self.player_start = self.player_choise


    def Start(self):
        print('Участвуют следующие учатники:')
        print('\n'.join([f'{idx} - {self.type_player_names[e.type_player]} - {e.name}' for idx, e in enumerate(self.players)]))
        step = 1
        while True:
            print(f'Шаг {step}, остаток {self.params["candys_prestep"]}')
            get_candys = self.get_candys(self.player_choise)
            self.write_statistic(step=step, get_candys=get_candys, player=self.players[self.player_choise])
            print(f'Игрок {self.player_choise} - {self.players[self.player_choise].name} - {self.type_player_names[self.players[self.player_choise].type_player]} - взял {get_candys}')

            self.params['candys_prestep'] -= get_candys

            if self.params['candys_prestep'] == 0:
                self.players[self.player_choise].is_win = True
                print(f'Выйграл {self.player_choise} {self.players[self.player_choise].name} за {step} шагов')
                self.save_matrix_greedy(self.params['path_matrix'], self.players[self.player_choise], [e for idx, e in  enumerate(self.players) if idx != self.player_choise])
                break

            step = self.change_player(step)


    def write_statistic(self, step:int, get_candys:int, player:Player):
        stat = {'step': step, 'candys_prestep': self.params["candys_prestep"], 'get_candys':get_candys, 'is_win': True if self.params["candys_prestep"] - get_candys <= 0 else False }
        player.statistics[int(self.params["candys_prestep"])] = stat


    def change_player(self, step:int) -> int:
        self.player_choise = self.change_players[self.player_choise]
        return step + 1


    def get_candys(self, player:int):
        get_candys = 0
        if self.players[player].type_player == TypePlayer.robot:
            get_candys = self.get_pos_robot()
        elif self.players[player].type_player == TypePlayer.human:
            get_candys = self.get_pos_humen()

        return get_candys


    def get_pos_robot(self):
        pos = 0
        if self.params["candys_prestep"] not in self.matrix_greedy.keys():
            pos = random.randint(1,
                                        self.params['get_max_candys'] if self.params['get_max_candys'] <= self.params[
                                            'candys_prestep'] else self.params['candys_prestep'])
        else:
            while True:
                pos = random.choices([e for e in range(self.params['get_max_candys'] + 1)],
                                            weights=self.matrix_greedy[self.params["candys_prestep"]]['coefficients'])[
                    0]
                if pos <= self.params['candys_prestep'] and pos != 0:
                    break
        return pos


    def get_pos_humen(self):
        pos = 0
        while True:
            val = input(f'Введите количество взятых конфет, но не более {self.params["get_max_candys"]}?')
            val = ''.join([c for c in val if str.isdigit(c)])
            if len(val) > 0:
                val = int(val)
                if 1 <= val <= self.params['get_max_candys']:
                    pos = val
                    break
        return pos


    def save_matrix_greedy(self, path:str, player_win:Player, players_lose:List[Player]):
        statistic_win_steps = list(player_win.statistics.keys())
        statistic_win_steps.sort()
        steps_not_in_greedy = [step for step in statistic_win_steps if step not in self.steps_matrix_greedy and step != 0]
        steps_not_in_greedy.sort()
        steps_in_greedy = [step for step in statistic_win_steps if step in self.steps_matrix_greedy and step != 0]
        steps_in_greedy.sort()

        if len(steps_not_in_greedy) > 0:
            min_step = player_win.statistics[min(steps_not_in_greedy)]
            self.matrix_greedy[int(min_step['candys_prestep'])] = {
                'coefficients': [100.0 for _ in range(self.params['get_max_candys'] + 1)]}
            self.matrix_greedy[int(min_step['candys_prestep'])]['coefficients'] = [
                e * 0.85 if idx != min_step['get_candys'] else e * (1.15 if player_win.type_player == TypePlayer.robot else 1.5)
                for idx, e in
                enumerate(self.matrix_greedy[int(min_step['candys_prestep'])]['coefficients'])]

        if len(steps_in_greedy) > 0:
            for candys_prestep in steps_in_greedy:
                min_step = player_win.statistics[candys_prestep]
                self.matrix_greedy[int(candys_prestep)]['coefficients'] = [
                    e * (0.85 if player_win.type_player == TypePlayer.robot else 0.75) if idx != min_step['get_candys'] else e * (1.25 if player_win.type_player == TypePlayer.robot else 1.5)
                    for idx, e in
                    enumerate(self.matrix_greedy[int(min_step['candys_prestep'])]['coefficients'])]
                self.matrix_greedy[int(candys_prestep)]['coefficients'] = [e*10 if e < 0.0001 else e for e in
                                                                           self.matrix_greedy[int(candys_prestep)][
                                                                               'coefficients']]
                self.matrix_greedy[int(candys_prestep)]['coefficients'] = [1000.0 if e > 1000.0 else e for e in self.matrix_greedy[int(candys_prestep)]['coefficients']]

        for player_lose in players_lose:
            for step in list(player_lose.statistics.keys()):
                if step in self.steps_matrix_greedy:
                    self.matrix_greedy[int(step)]['coefficients'][player_lose.statistics[int(step)]['get_candys']] *= .85


        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.matrix_greedy, f, ensure_ascii=False)


    def load_matrix_greedy(self, path:str):
        matrix_greedy = {1: {'coefficients': [100.0 for _ in range(self.params['get_max_candys'] + 1)]}}
        with open(path) as f:
            matrix_greedy = json.load(f)
        matrix_greedy = {int(k): v for k, v in matrix_greedy.items()}
        return matrix_greedy




