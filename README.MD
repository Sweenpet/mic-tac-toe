##AWS
Firstly go to the AWS console/cli, create a lambda and give it write permissions to an s3 bucket.

## Run locally

When running locally, one needs to have aws cli, i.e a .aws folder in the HOME directory

### Conda
To create the conda env run

``` conda env create -f environment.yml ```

Conda package manager can be downloaded [here](https://conda.io/miniconda.html)

To activate:
``` (source) activate mic-loader ```

To run:
``` python(3) main.py```

### Virtualenv

pip(3) install -r requirements.txt

### Test

To run:
```  cd tests  ```
```  nosetests .  ```

## Deploy

First build the docker image

``` docker build . --tag mic-loader```

Then to upload to AWS

``` docker run mic-loader --env BUCKET={BUCKET} --env LAMBDA={LAMBDA} ```

I think it makes more sense to push it to AWS when the container is built.
Currently the parameters are limited to the lambda and the bucket, but
ideally one could pass the sheer parser type.

## Modeling assumptions

I didn't really change the shape of the data. I did some sanitization on it however,
all the whitespace was removed from the keys, replaced with hypens and made lowercase.
When strings were empty or floats were nans I omitted theres values from the json object
as empty strings and nans provide no information, plus it saves space.

The current implementation is limited but generic across excel sheets. The code can handle tabular data, creating
an object per row, user is also able to specify resource location, url currently and sheet names. If it was desired to more radically transform the data all one has to do it inherit from sheet_reader and set this as the default type in the settings.json.


Changes I could make to how the data is stored:

* Store it hierarchally by country, then city
* Replace the string format for operating/market segment with binary value or enum
* It might be benefitial to store the dates in a more conventional format dd/mm/yyyy
* Can lose the www and http prefixes on the websites but keep whether its using ssl or not.

Ultimately I would need more information on how the data is consumed to make these decisions.





