from pathlib import Path

from django.contrib.gis.utils import LayerMapping

from .models import Hospital

hospital_mapping = {
    "name": "Hospital",
    "lon": "Long",
    "lat": "Lat",
    "fid": "FID",
    "beds": "beds",
    "province_name": "ADM1_EN",
    "province_code": "ADM1_PCODE",
    "geom": "POINT",
}

hospital_shp = Path(__file__).resolve().parent / "data" / "Hospitals.shp"


def run(verbose=True):
    lm = LayerMapping(Hospital, str(hospital_shp), hospital_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
