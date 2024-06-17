'''
Computes top-of-atmosphere (TOA) radiation from a series of MERRA-2
M2SDNXSLV files, then writes an output netCDF file. TOA radiation is
calculated according to the FAO formula for extraterrestrial radiation:

    https://www.fao.org/4/X0490E/x0490e07.htm#radiation
'''

import numpy as np
import xarray as xr

# NOTE: This will be different on your computer system and you should
#   use an absolute path, not a relative path
MERRA2_DATA_DIR = './data_raw/MERRA2'
DATA_YEAR = 2023
OUTPUT_FILE = f'./data/YYYYMMDD_MERRA2_{DATA_YEAR}_with_TOA-radiation.nc'

def main():
    ds = xr.open_mfdataset(f'{MERRA2_DATA_DIR}/*{DATA_YEAR}*.nc4', chunks = 'auto')
    lats = ds['lat'].values.reshape((361, 1, 1))\
        .repeat(ds.lon.size, axis = 1)\
        .repeat(ds.time.size, axis = 2)
    ds['lat_grid'] = (('lat', 'lon', 'time'), lats)

    # Compute TOA radiation
    template = ds['T2MMEAN']
    template.name = 'toa_radiation'
    result = xr.map_blocks(toa_radiation_wrapper, ds, template = template)
    toa_result = result.compute()
    # Converting TOA Radiation from [MJ m-2 day-1] to [mm H2O day-1]
    ds['toa_radiation'] = toa_result * 0.408

    # Write the file to disk, just the important variables
    ds = ds[['T2MMAX', 'T2MMEAN', 'T2MMIN', 'toa_radiation']]
    comp = dict(zlib = True, complevel = 5)
    encoding = {var: comp for var in ds.data_vars}
    ds.to_netcdf(OUTPUT_FILE, format = 'NETCDF4', encoding = encoding)


def toa_radiation(latitude, doy):
    '''
    Top-of-atmosphere (TOA) radiation for a given latitude (L) and day of year
    (DOY) can be calculated as:

    R = ((24 * 60) / pi) * G * d * (w * sin(L) * sin(D) + cos(L) * cos(D) * sin(w))

    Where G is the solar constant, 0.0820 [MJ m-2 day-1]; d is the earth-sun
    distance; w is the sunset hour angle; and D is the solar declination angle.

    For more information, consult the FAO documentation:

        https://www.fao.org/4/X0490E/x0490e07.htm#radiation

    Parameters
    ----------
    latitude : float
        The latitude on earth, in degrees
    doy : int
        The day of the year (DOY), an integer on [1,366]

    Returns
    -------
    Number
        Top-of-atmosphere (TOA) radiation, in [MJ m-2 day-1]
    '''
    solar_constant = 0.0820 # [MJ m-2 day-1]
    pi = 3.14159

    # Convert latitude from degrees to radians
    lat_radians = np.deg2rad(latitude)
    # Earth-Sun distance, as a function of day-of-year (DOY)
    earth_sun_dist = 1 + 0.0033 * np.cos(doy * ((2 * pi) / 365))
    # Solar declination, as a function of DOY
    declination = 0.409 * np.sin(doy * ((2 * pi) / 365) - 1.39)

    # Sunset hour angle; we use np.where() below to guard against
    #   warnings where arccos() would return invalid values, which
    #   happens when the argument is outside [-1, 1]
    _hour_angle = -np.tan(lat_radians) * np.tan(declination)
    _hour_angle = np.where(np.abs(_hour_angle) > 1, np.nan, _hour_angle)
    sunset_hour_angle = np.arccos(_hour_angle)

    return ((24 * 60) / pi) * solar_constant * earth_sun_dist *\
        (sunset_hour_angle * np.sin(lat_radians) * np.sin(declination) +
            np.cos(lat_radians) * np.cos(declination) * np.sin(sunset_hour_angle))


def toa_radiation_wrapper(dataset):
    'Wraps toa_radiation to work with an xarray.Dataset'
    return toa_radiation(dataset['lat_grid'], dataset['time.dayofyear'])


# If the file is run as a script, run the main() function
if __name__ == '__main__':
    main()
