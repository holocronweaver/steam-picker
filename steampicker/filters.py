'''
Pre-made app filters for easy filtering.

Feel free to customize!
'''
class Filter:
    def __init__(self, text, lambda_filter):
        self.text = text
        self.function = lambda_filter

# A list of quick filter aliases to apply by default.
default = []

# The available quick filters.
quick = {
    #TODO: 'aaa' and proper 'indie'. Doesn't seem possible with current metadata.
    'coop': Filter(
        'Co-op games.',
        lambda x: any('Co-op' in category for category in x['Categories'])
    ),
    'indie': Filter(
        'Indie games. (Some indie games are not tagged, so expect false negatives.)',
        lambda x: 'Indie' in x['Genres']
    ),
    'linux': Filter(
        'Linux support.',
        lambda x: 'linux' in x['Platforms']
    ),
    'mac': Filter(
        'MacOS support.',
        lambda x: 'mac' in x['Platforms']
    ),
    'multi': Filter(
        'Multi-player.',
        lambda x: 'Multi-player' in x['Categories']
    ),
    'score': Filter(
        'Metracritic scores >= 70. (Filters out games lacking Metacritic scores.)',
        lambda x: x['Metacritic']['score'] >= 70
    ),
    'score80': Filter(
        'Metracritic scores >= 80. (Filters out games lacking Metacritic scores.)',
        lambda x: x['Metacritic']['score'] >= 80
    ),
    'score90': Filter(
        'Metracritic scores >= 90. (Filters out games lacking Metacritic scores.)',
        lambda x: x['Metacritic']['score'] >= 90
    ),
    'single': Filter(
        'Single-player.',
        lambda x: 'Single-player' in x['Categories']
    ),
    'vr': Filter(
        'VR support. (Steam store metadata does not categorize all VR-capable games, so this will miss some.)',
        lambda x: 'VR Support' in x['Categories']
    ),
    'unplayed': Filter(
        'Played less than an hour.',
        lambda x: x['Playtime']['hours'] == 0
    ),
}
