from django.db import models

# Create your models here.
def getSampleData():
    ans = [{'City'       : 'Dublin',
            'Province'   : 'Leinster',
            'Population' : 1110627},
           {'City'       : 'Cork',
            'Province'   : 'Munster',
            'Population' : 198582},
           {'City'       : 'Limerick',
            'Province'   : 'Munster',
            'Population' : 91454},
           {'City'       : 'Galway',
            'Province'   : 'Connacht',
            'Population' : 76778},
           {'City'       : 'Waterford',
            'Province'   : 'Munster',
            'Population' : 51519}
          ]
    return ans

