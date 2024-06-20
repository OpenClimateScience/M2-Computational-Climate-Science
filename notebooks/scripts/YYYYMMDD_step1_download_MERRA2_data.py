'''
Downloads MERRA-2 M2SDNXSLV data, for the first 5 months of a year.
Read more about MERRA-2 here:

    https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/

Data are downloaded to this folder:

    data_raw/MERRA2
'''

import earthaccess

DATA_YEAR = 2023

auth = earthaccess.login()

results = earthaccess.search_data(
    short_name = 'M2SDNXSLV',
    temporal = (f"{DATA_YEAR}-01-01", f"{DATA_YEAR}-05-31"))

# Could take about 1 minute on a broadband connection
earthaccess.download(results, 'data_raw/MERRA2')
