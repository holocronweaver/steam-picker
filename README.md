A Python 3 CLI for picking a random game from your Steam library!

# Features

-   customizable filters (co-op, multiplayer, VR, high Metacritic rating, and more!)
-   concise game metadata (summary, platforms, categories, playtime, Metacritic score, etc.)
-   remembers your Steam ID and API key, only have to enter once

# Installation

**Requires Python 3.9 or higher.**

## pipx [recommended]

[Install pipx](https://pipx.pypa.io/) if you haven't already, then run the following command in the app root directory:

`pipx install .`

Add the `--editable` flag if you want to hack on the source code and have your changes automatically reflected in the installed app:

`pipx install --editable .`

## pip

Run the following command in the app root directory:

`pip3 install --user .`

Feel free to omit the `--user` flag if you normally install packages
to the root directory.

# Usage

Assuming your Python package bin is in your `$PATH`, just run `steam-picker` from the command line.

    Pick a game from your personal Steam library!
    
    <enter your Steam profile URL and API key>
    
    How about... 'Zeno Clash 2'?
    
    Categories: ['Single-player', 'Co-op', 'Steam Achievements', 'Full controller support', 'Steam Trading Cards', 'Steam Cloud', 'Steam Leaderboards']
    Genres:     ['Action', 'Indie']
    Platforms:  ['windows']
    Playtime:   {'hours': 0}
    Steam URL:  https://store.steampowered.com/app/215690/
    
    [y = accept, n or q = quit, f = filter, other = continue]: f
    
    See filters.py to customize quick filters and add default filters.
    
    Quick filters
    =============
    coop:       Co-op games.
    high:       Metracritic scores > 70. (Filters out games without Metacritic scores.)
    linux:      Linux support.
    multi:      Multiplayer.
    vr:         VR support. (Steam store metadata does not categorize all VR-capable games, so this will miss some.)
    unplayed:   Played less than an hour.
    
    [Quick filter alias <or> Python lambda x: filter body to add <or> filter ID to delete]: coop
    
    How about... 'Secrets of Grindea'?
    
    Summary:    A fantasy Action RPG, playable by yourself or in co-op with up to three friends! Features an unrestricted skill system, fluid and challenging combat, and an engaging story. For additional value, there's also a fleshed out, challenging roguelike mode to truly put your ARPG skills to the test!
    Categories: ['Single-player', 'Online Multi-Player', 'Co-op', 'Steam Achievements', 'Full controller support', 'Steam Cloud', 'Steam Leaderboards']
    Genres:     ['Action', 'Adventure', 'Indie', 'RPG', 'Early Access']
    Platforms:  ['windows']
    Playtime:   {'hours': 1}
    Steam URL:  https://store.steampowered.com/app/269770/
    
    [y = accept, n or q = quit, f = filter, other = continue]: y
    
    Alright, 'Secrets of Grindea' it is.
    
    ░▐█▀█ ▄▀▄ █▀▀▄ ▀█▀ ▀▄─▄▀──░█▀█▀█ ▀ █▄─▄█ █▀▀░█░█░█
    ░▐█▄█ █▀█ █▐█▀ ─█─ ──█──────░█── █ █─█─█ █▀▀─▀─▀─▀
    ░▐█── ▀─▀ ▀─▀▀ ─▀─ ──▀─────░▄█▄─ ▀ ▀───▀ ▀▀▀░▄░▄░▄

# Development

To develop this package or run it without installing:

1. Install [uv](https://docs.astral.sh/uv/).
1. Run the app: `uv run steam-picker`
1. Build the app for distribution (see `dist` directory for wheel and archive): `uv build`

