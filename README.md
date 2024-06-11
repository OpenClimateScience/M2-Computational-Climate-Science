M2: Computational Climate Science
=================================

> How can we analyze gridded climate datasets with spatial and temporal attributes? How is climate variability measured and modeled?

The second module of our [open climate-science curriculum](https://openclimatescience.github.io/curriculum) focuses on preparing learners to work with gridded climate datasets.
**At the end of this module, you should be able to:**

- Describe the interpretation and calculation of climate normals, climate anomalies, and a climatology.
- Learn what indices are available for meteorological drought, soil moisture drought, atmospheric water demand, and canopy greenness.
- Calculate a drought index.


Contents
--------------

1. Managing Software Dependencies
2. Working with Gridded Climate Data
3. Climate and Drought Indices


Getting Started
---------------

[See our installation guide here.](https://github.com/OpenClimateScience/M1-Open-Climate-Data/blob/master/HOW_TO_INSTALL.md)

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
- Uses a package manager to install and manage software dependencies. (CC1.10)
- Knows how to navigate a file system using both a graphical user interface (GUI) and a command-line interface (CLI). (CC1.4)
- Records relationships between code, results, and metadata. (CC1.5)
- Understands machine representations of numeric data types. (CC2.1)
- Can debug a computational workflow, either by deduction, print statements, breakpoints, or an interactive debugger. (CC2.7)
