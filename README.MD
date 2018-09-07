## Run locally

### Conda
To create the conda env run

``` conda env create -f environment.yml ```

Conda package manager can be downloaded [here](https://conda.io/miniconda.html)

To activate:
*widows* ``` activate mic-loader ```

*nix*  ``` source activate mic-loader ```

To run:
``` python main.py```

### Virtualenv

pip(3) install -r requirements.txt

### Test

To run:
```  cd tests  ```
```  nosetests .  ```

## Deploy

First build the docker images

``` docker build . --tag mic-loader```

Then to deploy

``` docker run mic-loader --env BUCKET={BUCKET} --env LAMBDA={LAMBDA} ```









