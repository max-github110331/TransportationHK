# import
import requests
from json import loads
from dataclasses import dataclass
from .error import MissingData


# data class
@dataclass
class abcStop:
    __slots__ = (
        'json',
        'id',
        'name',
        'coordinate'
    )

    json: dict
    id: str
    name: dict[str, str]
    coordinate: dict[str, float]

    def __init__(self, json: dict):
        if json == {}:
            raise MissingData('Please make sure your stop data is correct. API has not responsed anything to you!')
        self.json = json
        self.id = json['stop']
        self.name = {
            'zh': self.json['name_tc'],
            'tc': self.json['name_tc'],
            'en': self.json['name_en'],
            'cn': self.json['name_sc'],
            'sc': self.json['name_sc']
        }
        self.coordinate = {
            'lat': float(self.json['lat']),
            'long': float(self.json['long'])
        }


# main function
class Stop(abcStop):
    # get bus stop data
    def get(id: str = None, name: str = None, language: str = None):
        if id == None and name == None and language == None:
            raise ValueError('Please make sure you entered ')
        elif language != None and language not in ['zh', 'tc', 'en', 'cn', 'sc']:
            raise ValueError('Language needs to follow the format!')

        # get by id
        if id:
            _response = requests.get(f'https://data.etabus.gov.hk/v1/transport/kmb/stop/{id}')
            _response.raise_for_status()
            _json = loads(_response.content.decode('utf-8'))
            return abcStop(_json['data'])

        # get by name
        if name and language:
            _stops: list[abcStop] = []
            for stop in Stop.all():
                if name == stop.name[language]:
                    _stops.append(stop)
            return _stops

    # get all of the bus stop data
    def all():
        _response = requests.get('https://data.etabus.gov.hk/v1/transport/kmb/stop')
        _response.raise_for_status()
        _json: dict = loads(_response.content.decode('utf-8'))
        _stops: list[abcStop] = []
        for stopJson in _json['data']:
            _stops.append(abcStop(stopJson))
        return _stops