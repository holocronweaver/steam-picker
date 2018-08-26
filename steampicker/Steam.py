import requests
import steam as steamapi
import steampicker.utility as utility

class Steam:
    def __init__(self, apikey):
        self.api = steamapi.WebAPI(apikey)
        # self.client = steamapi.SteamClient()

    def validateWebApiKey(apikey):
        steamapi.WebAPI(apikey)

    def getSteamIdFromURL(profile_url):
        return steamapi.steamid.from_url(profile_url)

    def getOwnedGames(self, steamid):
        response = self.api.IPlayerService.GetOwnedGames(
            steamid                   = steamid,
            include_appinfo           = True,
            include_played_free_games = True,
            appids_filter             = None
        )
        return response['response']['games']

    def getRawAppDetails(self, appid):
        response = requests.get('http://store.steampowered.com/api/appdetails', params={'appids': appid})
        apps = response.json()
        app = apps[str(appid)]
        return app['data'] if 'data' in app else None

    def getAppDetails(self, appid):
        raw_details = self.getRawAppDetails(appid)
        if not raw_details:
            return None

        details = {}
        if 'short_description' in raw_details and raw_details['short_description']:
            details['Summary'] = utility.remove_html_tags(raw_details['short_description'])
        if 'categories' in raw_details:
            details['Categories'] = [category['description'] for category in raw_details['categories']]
        if 'genres' in raw_details:
            details['Genres'] = [genre['description'] for genre in raw_details['genres']]
        if 'platforms' in raw_details:
            platforms = raw_details['platforms']
            details['Platforms'] = [platform  for platform in platforms if platforms[platform]]
        if 'metacritic' in raw_details:
            details['Metacritic'] = raw_details['metacritic']
        return details
