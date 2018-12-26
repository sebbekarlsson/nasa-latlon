# NASA lat-lon
> Python wrapper for NASA imagery.

## Usage
> To use it:

    from nasalatlon.camera import get_photo


    photo = get_photo(lat=25, lon=25)

    print(photo)

    {
        u'resource': {
            u'planet': u'earth', u'dataset': u'LC8_L1T_TOA'
        },
        u'service_version': u'v1',
        u'url': u'https://earthengine.googleapis.com/api/thumb?thumbid=d5c077a4aa6d9be63ea4d557a3733ddf&token=7917de4ac36fc0b82cf7fb7686d4c082',
        u'cloud_score': 0.0,
        u'date': u'2014-01-31T08:45:04',
        u'id': u'LC8_L1T_TOA/LC81790432014031LGN00'
    }
