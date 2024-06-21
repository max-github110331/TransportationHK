# import
import requests


# data class
class abcRoute:
    json: dict = None
    if (json):
        route: str = json['route']
        direction: str | bool = json['bound']
        serviceType: str = json['service_type']
        origin: dict = {
            'zh': json['orig_tc'],
            'tc': json['orig_tc'],
            'en': json['orig_en'],
            'cn': json['orig_sc'],
            'sc': json['orig_sc']
        }
        destination: dict = {
            'zh': json['dest_tc'],
            'tc': json['dest_tc'],
            'en': json['dest_en'],
            'cn': json['dest_sc'],
            'sc': json['dest_sc']
        }


# main functions
class Route(abcRoute):
    # get bus route data
    def get(route: str, direction: str | bool = 'O', serviceType: str | int = '1') -> None:
        if (bool(direction)):
            if (direction == True):
                direction = 'O'
            if (direction == False):
                direction = 'I'
        if (int(serviceType)):
            serviceType = str(serviceType)
        _response = requests.get(f'https://data.etabus.gov.hk/v1/transport/kmb/route/{route}/{direction}/{serviceType}')
        _response.raise_for_status()
        _json = _response.json()
        abcRoute.json = _json
        return abcRoute


    # get all of the route data
    def all():
        _response = requests.get('https://data.etabus.gov.hk/v1/transport/kmb/route/')
        _response.raise_for_status()
        _json = _response.json()
        allRouteJson = _json['data']
        _list = []
        for routeJson in allRouteJson:
            abcRoute.json = routeJson
            _list.append(abcRoute)
        return _list