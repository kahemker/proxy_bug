Installation instructions
-----
This demo requires
1. Pandas
2. requests
3. pvlib (kahemker fork)
4. siphon (kahemker fork)
5. netCDF4
6. cftime == 1.0.4 (there is a bug in pvlib with the newest version of cftime)

You can install most of these packages with Anaconda using the `environment.yml` file

    conda env create -f environment.yml

Activate your new environment: `conda activate daedalus`

Verify the environment was installed correctly:  `conda env list`

Custom forks of two packages after you install the above first

    pip install -e git+https://github.com/kahemker/siphon.git@ssl-catalog#egg=siphon
    pip install -e git+https://github.com/kahemker/pvlib-python.git@dev#egg=pvlib
    
These forks allow you to pass additional arguments into the pvlib-forecast 
models that allow your HTTP GET requests to the meteorological servers to pass through 
my company's proxy.

Run the `proxy_test.py` file.  You should see one user warning because the PVLIB forecast module is under development
and insecure SSL warnings.  The process should finish successfully with exit code 0.




