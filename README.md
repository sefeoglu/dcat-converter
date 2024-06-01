The poster paper "Converter: Enhancing Interoperability in Research Data Management" of this repository has been accepted by ESWC 2024.

# DCAT Converter
The project converts the oai_dc formatted meta data into dcat_ap format and save them in rdf format.
This converter has been integrated to harvest the data of Berlin University Alliance.
The portal of this project is available since last November: [META4BUA](https://meta4bua.fokus.fraunhofer.de/datasets?locale=en)
## Meta Data Portal
![META4BUA](https://github.com/sefeoglu/dcat-converter/blob/master/doc/bua.png)


## Project Folder Structure
````
.
├── LICENSE
├── README.md
├── config.ini
├── configs --> all the config.ini files of the repositories.
│   ├── config_fuberlin.ini
│   ├── config_huberlin.ini
│   └── config_tuberlin.ini
├── data
│   ├── fu_berlin.rdf
│   ├── hu_berlin.rdf
│   ├── sample.rdf
│   └── tu_berlin.rdf
├── dockerfile
├── requirements.txt
├── schema
├── schema_matching_experiments
└── src
    ├── converter_service.py
    ├── data_crawler.py
    ├── dcat_ap.py
    ├── matches.py
    ├── schema_matcher
    └── utils.py
````
## Run
* Create a conda environment

```
$ conda create -n dcat_env python=3.9
```

* Activate enviroment

```
$ conda activate dcat_env
```
* Install Requirements

```
pip install -r requirements.txt
```

*  ```config_reponame.ini``` has the specific data crawling parameters.
First copy the config file of the repository into ```config.ini``` for a repository that you would like to work.
Then, run the steps below for only one repository.
After finishing the steps, repeat them for other repository.

## 1. Change the config.ini
* copy the config_reponame's content into ```config.ini``` for the repository
## 2. Repository APIs


* 1.) Refubium Repository

```
https://refubium.fu-berlin.de/oai/dnb?verb=ListRecords&metadataPrefix=xMetaDissPlus
```

* 2.) Depositonce Repository

```
https://api-depositonce.tu-berlin.de/server/oai/request?verb=ListRecords&metadataPrefix=oai_dc
```
* 3.) Edoc Repository

```
https://edoc.hu-berlin.de/oai/request/?verb=ListRecords&metadataPrefix=oai_dc
```

 **Note: The data is harvested in partitions (100 records per request).  Entire data is not harvested and imported into the portal with each update.**
## 3. Data Collection and Converter
* Run the script below:
```
python src/converter_service.py
```
@author: Sefika Efeoglu: sefika.efeoglu@fu-berlin.de

