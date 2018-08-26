def load_steam_creds(path):
    '''
    Load Steam credentials from a YAML file, or create the file if none exists.

    Args:
        path: pathlib.Path to yaml file containing creds.

    Returns:
        A dict of Steam credentials.
    '''
    import yaml
    from Steam import Steam

    creds = None
    if path.exists():
        with open(path, 'r') as f:
            creds = yaml.load(f)
    else:
        creds = {}
        creds['profile_url'] = input('Please enter your Steam profile URL [e.g., https://steamcommunity.com/id/MyUserName/home/]: ')
        creds['steamid'] = Steam.getSteamIdFromURL(creds['profile_url'])
        creds['apikey'] = input('Please enter your Steam API access key (see https://steamcommunity.com/dev/apikey): ')
        Steam.validateWebApiKey(creds['apikey'])
        with open(path, 'w') as f:
            yaml.dump(creds, f, default_flow_style=False)
    return creds


def remove_html_tags(text):
    '''Remove HTML tags from a string.'''
    import re
    return re.sub('<[^<]+?>', '', text)
