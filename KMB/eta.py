# import
import requests
from json import loads
from datetime import datetime
from dataclasses import dataclass
from .stop import abcStop, Stop
from .route import abcRoute, Route
from .error import MissingData


# data class
@dataclass
class abcETA:
    __slots__ = [
        'json',
        'route',
        'ETA',
        'remark',
        'destination'
    ]

    json: dict
    route: abcRoute | None
    ETA: datetime
    remark: dict[str, str]
    destination: dict[str, str]

    def __init__(self, json: dict):
        if (json == {}):
            raise MissingData('Please make sure your ETA data is correct. API has not responsed anything to you!')
        self.json = json
        self.route = Route.get(
            self.json['route'],
            self.json['service_type'],
            self.json['dir'].replace('O', 'outbound').replace('I', 'inbound')
        )
        self.ETA = datetime.fromisoformat(self.json['eta'])
        self.remark = {
            'zh': self.json['rmk_tc'],
            'tc': self.json['rmk_tc'],
            'en': self.json['rmk_tc'],
            'cn': self.json['rmk_sc'],
            'sc': self.json['rmk_sc']
        }
        self.destination: dict = {
            'zh': self.json['dest_tc'],
            'tc': self.json['dest_tc'],
            'en': self.json['dest_en'],
            'cn': self.json['dest_sc'],
            'sc': self.json['dest_sc']
        }


    @property
    def stop(self):
        if 'stop' in self.json:
            return Stop.get(id = self.json['stop'])
        else:
            return self.route.stops[self.json['seq'] - 1]


# main function
class ETA(abcETA):
    # get by route and stop
    def getRouteStop(route: abcRoute, stop: abcStop):
        _response = requests.get(
            f'https://data.etabus.gov.hk/v1/transport/kmb/eta/{stop.id}/{route.route}/{route.serviceType}')
        _response.raise_for_status()
        _json = loads(_response.content.decode('utf-8'))
        _eta: list[abcETA] = []
        for ETAJson in _json['data']:
            _eta.append(abcETA(ETAJson))
        return _eta

    # get by stop
    def getStop(stop: abcStop):
        _response = requests.get(f'https://data.etabus.gov.hk/v1/transport/kmb/stop-eta/{stop.id}')
        _response.raise_for_status()
        _json = loads(_response.content.decode('utf-8'))
        _eta: list[abcETA] = []
        for ETAJson in _json['data']:
            _eta.append(abcETA(ETAJson))
        return _eta

    # get by route
    def getRoute(route: abcRoute):
        _response = requests.get(
            f'https://data.etabus.gov.hk/v1/transport/kmb/route-eta/{route.route}/{route.serviceType}')
        _response.raise_for_status()
        _json = loads(_response.content.decode('utf-8'))
        _eta: list[abcETA] = []
        for ETAJson in _json['data']:
            _eta.append(abcETA(ETAJson))
        return _eta
