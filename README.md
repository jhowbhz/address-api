### Geolocation FreeAPI
Is a simple API develop in PYTHON and Flask, to integration in LocationIQ for free user :)

### How to teste API

Endpoint demo Request GET:

```
https://address.contrateumdev.com.br/autocomplete?search=ana%20alvarenga%20campos,%20belo%20horizonte
```

Response SUCCESS:

```json
{
    "address": {
        "city": "Contagem",
        "country": "Brazil",
        "country_code": "br",
        "county": "Microrregião Belo Horizonte",
        "postcode": "32072330",
        "road": "Rua Gaforina",
        "state": "Minas Gerais",
        "state_district": "Região Geográfica Intermediária de Belo Horizonte",
        "suburb": "Petrolândia"
    },
    "boundingbox": [
        "-19.9188292",
        "-19.9179392",
        "-44.1064442",
        "-44.0996876"
    ],
    "display_name": "Região Metropolitana de Belo Horizonte, Região Geográfica Intermediária de Belo Horizonte, Minas Gerais, Southeast Region, 32072330, Brazil",
    "lat": "-19.9183173",
    "licence": "https://locationiq.com/attribution",
    "lon": "-44.1001843",
    "osm_id": "224298752",
    "osm_type": "way",
    "place_id": "141466939"
}
```
### How to consume API in $.POST Jquery

```javascript
function getData()
{
    $.post({
        method: 'GET',
        url: 'https://address.contrateumdev.com.br/autocomplete?search=ana%20alvarenga%20campos,%20belo%20horizonte',
        success: function(data, status, xhr) {
            resultado = JSON.parse(data);
            if (resultado) {
                console.log(resultado?.data)
            }else{
                error = JSON.parse(data);
                console.log(resultado?.data)
            }
        },
        error: function(data) {
            console.log(data.error)
        }
    })
}
```
