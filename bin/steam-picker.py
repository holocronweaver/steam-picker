#! /usr/bin/env python3
from appdirs import AppDirs
from pathlib import Path
import pkg_resources
import random

from steampicker import filters, Steam, utility

print('Pick a game from your personal Steam library!')

appdirs = AppDirs('steam-picker')
creds_path = Path(appdirs.user_config_dir).joinpath('creds.yaml')

party_time = pkg_resources.resource_string('steampicker', 'party_time.txt')
if type(party_time) is bytes:
    party_time = party_time.decode()

creds = utility.load_steam_creds(creds_path)
steam = Steam(creds['apikey'])
owned_games = steam.getOwnedGames(creds['steamid'])

active_filters = []
exit_app = False

while not exit_app:
    game = random.choice(owned_games)

    details = steam.getAppDetails(game['appid']) or {}
    details['Playtime'] = {'hours': game['playtime_forever'] // 60}
    details['Steam URL'] = 'https://store.steampowered.com/app/{}/'.format(game['appid'])

    if active_filters:
        passed = True
        for filter in active_filters:
            try:
                passed = filter.function(details)
                if not passed: break
            except KeyError:
                print("Could not apply filter '{}' on '{}'. Skipping.".format(filter.text, game['name']))
                passed = False
                break
        if not passed:
            continue

    print("\nHow about... '{}'?\n".format(game['name']))
    if details:
        for detail, value in details.items():
            print("{: <12}{}".format(*[detail + ':', value]))

    answer = input('\n[y = accept, n or q = quit, f = filter, other = continue]: ').lower()

    if 'y' in answer:
        picked_game = game['name']
        print("\nAlright, '%s' it is.\n" % picked_game)
        print(party_time)

        exit_app = True
    elif 'f' in answer:
        print('\nSee filters.py to customize quick filters and add default filters.')
        if active_filters:
            print('\nActive filters')
            print('==============')
            for i, active_filter in enumerate(active_filters):
                print("{:<12}'{}'".format("[{}]:".format(i), active_filter.text))
        print('\nQuick filters')
        print('=============')
        for alias, quick_filter in filters.quick.items():
            print("{:<12}{}".format("{}:".format(alias), quick_filter.text))

        reply = input('\n[Quick filter aliases (space separated)\n<or> Python lambda x: filter body to add\n<or> filter ID to delete]: ')
        if reply.isdigit():
            filterid = int(reply)
            try:
                del active_filters[filterid]
            except:
                print('Error: unable to delete that filter. Is the ID within range?')
        elif reply.split(' ')[0].strip() in filters.quick:
            aliases = [x.strip() for x in reply.split(' ')]
            for alias in aliases:
                try:
                    active_filters.append(filters.quick[alias])
                except:
                    print("Error: alias '{}' could not be applied.".format(alias))
        else:
            try:
                text = 'lambda x: ' + reply
                filter_lambda = eval(text)
                active_filters.append(filters.Filter(text, filter_lambda))
            except:
                print('Error: could not add filter. Please check expression.')
    elif any(x in answer for x in ['n', 'q']):
        print("\nAlrighty then, y'all come back now, ya hear?")
        exit_app = True
