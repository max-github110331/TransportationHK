# import
import requests
from json import loads
from dataclasses import dataclass
from .stop import abcStop, Stop
from .error import MissingData


# data class
@dataclass
class abcRoute:
    __slots__ = (
        'json',
        'route',
        'direction',
        'serviceType',
        'origin',
        'destination'
    )
    
    json: dict
    route: str
    direction: str
    serviceType: str
    origin: dict[str]
    destination: dict[str]

    def __init__(self, json: dict):
        if (json == {}):
            raise MissingData('Please make sure your route data is correct. API has not responsed anything to you!')
        self.json: dict = json
        self.route: str = self.json['route']
        self.direction: str = self.json['bound'].replace('O', 'outbound').replace('I', 'inbound')
        self.serviceType: str = self.json['service_type']
        self.origin: dict = {
            'zh': self.json['orig_tc'],
            'tc': self.json['orig_tc'],
            'en': self.json['orig_en'],
            'cn': self.json['orig_sc'],
            'sc': self.json['orig_sc']
        }
        self.destination: dict = {
            'zh': self.json['dest_tc'],
            'tc': self.json['dest_tc'],
            'en': self.json['dest_en'],
            'cn': self.json['dest_sc'],
            'sc': self.json['dest_sc']
        }


    # get the stops of the route
    @property
    def stops(self):
        _reponse = requests.get(f'https://data.etabus.gov.hk/v1/transport/kmb/route-stop/{self.route}/{self.direction}/{self.serviceType}')
        _reponse.raise_for_status()
        _json = loads(_reponse.content.decode('utf-8'))
        _stops: list[abcStop] = []
        for stopJson in _json['data']:
            _stops.append(Stop.get(id = stopJson['stop']))
        return _stops


# main functions
class Route(abcRoute):
    # get bus route data
    def get(route: str, serviceType: str | int = '1', direction: str = 'outbound'):
        if direction not in ['inbound', 'outbound']:
            raise ValueError('Direction needs to follow the format')
        if int(serviceType):
            serviceType = str(serviceType)
        _response = requests.get(f'https://data.etabus.gov.hk/v1/transport/kmb/route/{route}/{direction}/{serviceType}')
        _response.raise_for_status()
        _json = loads(_response.content.decode("utf-8"))
        return abcRoute(_json['data'])


    # get all of the route data
    def all():
        _response = requests.get('https://data.etabus.gov.hk/v1/transport/kmb/route/')
        _response.raise_for_status()
        _json = loads(_response.content.decode("utf-8"))
        _route: list[abcRoute] = []
        for routeJson in _json['data']:
            _route.append(abcRoute(routeJson))
        return _route