[![DOI](https://zenodo.org/badge/742518754.svg)](https://zenodo.org/doi/10.5281/zenodo.13820296)


M2: Computational Climate Science
=================================

> How can we analyze gridded climate datasets with spatial and temporal attributes? How is climate variability measured and modeled?

The second module of our [open climate-science curriculum](https://openclimatescience.github.io/curriculum) focuses on preparing learners to work with gridded climate datasets.
**At the end of this module, you should be able to:**

- Learn what indices are available for meteorological drought, soil moisture drought, atmospheric water demand, and soil water balance.
- Efficiently load and analyze big climate datasets, including long climate data records.
- Calculate a drought index.


Contents
--------------

1. [Managing Software Dependencies](https://github.com/OpenClimateScience/M2-Computational-Climate-Science/blob/main/notebooks/01_Managing_Software_Dependencies.ipynb)
2. [Working with Gridded Climate Data](https://github.com/OpenClimateScience/M2-Computational-Climate-Science/blob/main/notebooks/02_Working_with_Gridded_Climate_Data.ipynb)
3. [Climate and Drought Indices](https://github.com/OpenClimateScience/M2-Computational-Climate-Science/blob/main/notebooks/03_Climate_and_Drought_Indices.ipynb)
4. [Processing Long Climate Data Records Concurrently](https://github.com/OpenClimateScience/M2-Computational-Climate-Science/blob/main/notebooks/04_Processing_Long_Climate_Data_Records.ipynb)
5. [Creating a Reproducible Climate Analysis](https://github.com/OpenClimateScience/M2-Computational-Climate-Science/blob/main/notebooks/05_Creating_a_Reproducible_Climate_Data_Analysis.ipynb)


Getting Started
---------------

[See our installation guide here.](https://github.com/OpenClimateScience/M1-Open-Climate-Data/blob/main/HOW_TO_INSTALL.md)

You can run the notebooks in this repository using [Github Codespaces](https://docs.github.com/en/codespaces/overview) or as [a VSCode Dev Container](https://code.visualstudio.com/docs/devcontainers/containers). Once your container is running, launch Jupyter Notebook by:

```sh
# Create your own password when prompted
jupyter server password

# Then, launch Jupyter Notebook; enter your password when prompted
jupyter notebook
```

**The Python libraries required for the exercises can be installed using the `pip` package manager:**

```sh
pip install xarray netcdf4 dask
```


Learning Outcomes
-----------------

- Uses meaningful but brief filenames and folder names. Uses one of the following strategies: Timestamps, Process hierarchy, or Filename metadata. (CC1.3)
- Knows how to navigate a file system using both a graphical user interface (GUI) and a command-line interface (CLI). (CC1.4)
- Records relationships between code, results, and metadata. (CC1.5)
- Uses a package manager to install and manage software dependencies. (CC1.10)
- Understands machine representations of numeric data types. (CC2.1)
- Understands multidimensional arrays and their use for representing datasets structured by space, time, and multiple variables. (CC2.3)
- Profiles the resource use of a computational workflow. (CC2.5)
- Understands different types of concurrency and how to scale up a computational workflow that is limited by throughput or memory. (CC2.6)
- Can debug a computational workflow, either by deduction, print statements, breakpoints, or an interactive debugger. (CC2.7)
- Familiar with the different types of structured datasets used in scientific applications, including spatial datasets (raster and vector) and hierarchical datasets (e.g., HDF5, netCDF4). (CC2.8)
- Computational workflows are documented with both in-line comments and external documentation. (CC4.3)
- Writes short, simple functions that have no side effects. (CC4.9)


Climate Datasets Used
---------------------

- [Terrestrial water storage anomalies from the NASA GRACE and GRACE-FO missions](https://podaac.jpl.nasa.gov/dataset/TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.1_V3)
- Monthly precipitation estimates for Africa from [the Climate Hazards Group InfraRed Precipitation with Station (CHIRPS) dataset](https://www.chc.ucsb.edu/data/chirps)
- Monthly potential evapotranspiration data from [TerraClimate](https://climatedataguide.ucar.edu/climate-data/terraclimate-global-high-resolution-gridded-temperature-precipitation-and-other-water)
- Daily mean, minimum, and maximum air temperatures from [the NASA Global Modeling and Assimilation Office's MERRA-2 re-analysis dataset](https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/)


Acknowledgements
----------------

This curriculum was enabled by a grant from NASA's Transition to Open Science (TOPS) Training program (80NSSC23K0864), part of [NASA's TOPS Program](https://nasa.github.io/Transform-to-Open-Science/)
