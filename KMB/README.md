# KMB (LWB)
If you want to use KMB (LWB), you need to import it firstly.
```python
import KMB
```

## Route
> - [`get()`](#routeget)
> - [`all()`](#routeall)

### Route.get()
**Get a bus route**
- `route: str` The bus route number.
- `serverType: str | int` The service type of the bus route: '1' | 1
- `direction: str` The direction of the bus route: 'inbound' | 'outbound'

#### Return:
> [abcRoute](#abcroute)

### Route.all()
**List all of the bus route**

#### Return
> [list](https://docs.python.org/3/glossary.html#term-list)[[abcRoute](#abcroute)]

## abcRoute
> - `json: dict` The data of the route packed by JSON.
> - `route: str` The bus route number.
> - `direction: str` The direction of the bus route.
> - `serviceType: str` The service type of the bus route.
> - `origin: dict[str, str]` The origin of a bus route. There were Traditional Chinese, English and Simplified Chinese.
> - `destination: dict[str, str]` The destination of a bus route. There were Traditional Chinese, English and Simplified Chinese.
> - `stops: list[abcStop]` The stops of a bus route.

## Stop
> - [`get()`](#stopget)
> - [`all()`](#stopall)

### Stop.get()
**Get a bus stop**
- `id: str` The ID of a bus stop. (If you want to get by stop id, please enter this)
- `name: dict[str, str]` The name of a nus stop. (If you want to get by stop name, please enter this)
- `language: str` The language of the name. There were Traditional Chinese, English and Simplified Chinese. (Use to get by stop name)

#### Return
> [abcStop]()

### Stop.all()
**List all of the bus stop**

#### Return
> [list](https://docs.python.org/3/glossary.html#term-list)[[abcStop](#abcstop)]

## abcStop
> - `json: dict` The data of the stop packed by JSON.
> - `id: str` The ID of a bus stop.
> - `name: dict[str, str]` The name of a bus stop. There were Traditional Chinese, English and Simplified Chinese.
> - `coordinate: dict[str, float]` The Latitude and Longitude in decimal degree in WGS84 standard.

## ETA
> - [`getRoute()`](#etagetroute)
> - [`getStop()`](#etagetstop)
> - [`getRouteStop()`](#etagetroutestop)

### ETA.getRoute()
**Get all of the route's ETA**
- 'route: abcRoute' The bus route.

#### Return
> [list](https://docs.python.org/3/glossary.html#term-list)[[abcETA](#abceta)]

### ETA.getStop()
**Get all of the stop's ETA**
- `stop: abcStop` The bus stop.

#### Return
> [list](https://docs.python.org/3/glossary.html#term-list)[[abcETA](#abceta)]

### ETA.getRouteStop()
**Get all of the stop of the route's ETA**
- `route: abcRoute` The bus route.
- `stop: abcStop` The bus stop.

#### Return
> [list](https://docs.python.org/3/glossary.html#term-list)[[abcETA](#abceta)]

## abcETA
> - `json: dict` The data of the ETA packed by JSON.
> - `route: abcRoute` The bus route.
> - `stop: abcStop` The bus stop.
> - `ETA: datetime` The bus arrival's time
> - `remark: dict[str, str]` The remark of the ETA. There were Traditional Chinese, English and Simplified Chinese.
> - `destination: dict[str, str]` The destination of the bus route.