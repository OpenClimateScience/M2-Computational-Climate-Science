'''
Creates a single netCDF dataset for the CHIRPS monthly data for Africa.
Original CHIRPS data was downloaded from:

    https://data.chc.ucsb.edu/products/CHIRPS-2.0/africa_monthly/tifs/

It is assumed the filenames look something like:

    chirps-v2.0.1981.01.tif.gz
'''

import os
import glob
import gzip
import numpy as np
import rioxarray
import xarray as xr
import pandas as pd
from tqdm import tqdm
from tempfile import NamedTemporaryFile

DATA_DIRECTORY = '/home/user/Downloads/CHIRPS'
OUTPUT_FILE = 'CHIRPS-v2_Africa_monthly_2014-2023.nc'

file_list = glob.glob(f'{DATA_DIRECTORY}/chirps-v2.0.*.gz')
file_list.sort()
datasets = []
for i, file_path in tqdm(enumerate(file_list)):
    # Get the date of the current file as a YYYY-MM-DD string
    filename = os.path.basename(file_path)
    date = '-'.join(filename.split('.')[-4:-2]) + '-01'

    # Create an output filename (drop the "*.gz" extension)
    output_filename = filename.replace('.gz', '')

    # Open the compressed file
    with gzip.open(file_path, 'rb') as input_file:
        # Create a new temporary file (in memory); it's necessary to use
        #   delete = False because we will be trying to merge the file
        #   data for multiple files outside of the context of this file
        #   being open
        with NamedTemporaryFile(delete = False) as dummy_file:
            # Write the decompressed data into the file in memory
            dummy_file.write(input_file.read())
            # Then open the file in memory using rioxarray (file is a GeoTIFF)
            ds0 = rioxarray.open_rasterio(dummy_file.name)\
                .to_dataset(name = 'precip')
            # Assign the current date as a new "time" coordinate
            ds0 = ds0.assign_coords(band = ('band', [pd.to_datetime(date)]))
            datasets.append(ds0)

# Combine all the datasets together on the "time" axis
ds = xr.concat(datasets, dim = 'band', data_vars = ['precip'])\
    .rename_vars({'band': 'time'})\
    .swap_dims({'band': 'time'})\
    .sortby('time')
ds.reindex(time = ds.coords['time'])\
    .to_netcdf( # About 500 MB
        OUTPUT_FILE, format = 'NETCDF4',
        encoding = {'precip': {'compression': 'zlib', 'complevel': 5}})
