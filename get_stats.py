import os
import json
import tabulate


# PATH_TO_FILE = r'files/output_log.txt'
PATH_TO_FILE = os.path.join(os.environ['USERPROFILE'], r'AppData\LocalLow\1CGS\Caliber\output_log.txt')

# LINE_TO_FIND = r'Request https://ru-login.caliber.ru/v1/account/change_card complete:'
LINE_TO_FIND = r'Request https://ru-login.caliber.ru/v1/account/unmark_entity complete:'


if not os.path.exists(PATH_TO_FILE):
    print('Не найден файл с данными.')
else:
    with open(PATH_TO_FILE, 'r') as file:
        body = file.readlines()

    good = list()
    for line in body:
        if LINE_TO_FIND in line:
            good.append(line)
    last_good = good[-1]
    # print(last_good[69:])
    good_json = json.loads(last_good[len(LINE_TO_FIND) + 1:])

    print('\tИнформация об аккаунте:')
    nickname = good_json['nickname']
    credit = good_json['money']['values']['sc']
    gold = good_json['money']['values']['hc']
    level = good_json['level']
    free_exp = good_json['freeXp']

    table_acc = tabulate.tabulate([
        ['Ник', nickname], ['Уровень', level], ['Кредитов', credit], ['Золотишка', gold], ['Свободный опыт', free_exp]
    ], tablefmt='pipe')
    print(table_acc)

    print('\n\tИнформация о проведенных сражениях:')
    training = good_json['matchCount']['polygon']
    pve = good_json['matchCount']['pve']
    pve_hard = good_json['matchCount']['pvehard']
    pvp = good_json['matchCount']['pvp']
    hack_net = good_json['matchCount']['hacking']
    pvp_pve = good_json['matchCount']['pvpve']

    win_pve = good_json['matchesWon']['pve']
    win_pve_hard = good_json['matchesWon']['pvehard']
    win_pvp = good_json['matchesWon']['pvp']
    win_hack_net = good_json['matchesWon']['hacking']
    win_pvp_pve = good_json['matchesWon']['pvpve']

    percent_pve = round(win_pve / pve * 100, 2)
    percent_pve_hard = round(win_pve_hard / pve_hard * 100, 2)
    percent_pvp = round(win_pvp / pvp * 100, 2)
    percent_hack_net = round(win_hack_net / hack_net * 100, 2)
    percent_pvp_pve = round(win_pvp_pve / pvp_pve * 100, 2)

    table_batles = tabulate.tabulate([
        ['Всего игр', training, pve, pve_hard, pvp, hack_net, pvp_pve],
        ['Побед', training, win_pve, win_pve_hard, win_pvp, win_hack_net, win_pvp_pve],
        ['% побед', '100.00', percent_pve, percent_pve_hard, percent_pvp, percent_hack_net, percent_pvp_pve]
    ], headers=['', 'Тренировка', 'PvE', 'Спецоперация', 'PvP', 'Взлом', 'Фронт'], tablefmt='pipe')

    print(table_batles)

    print('\nСпасибо за использование программы!')


