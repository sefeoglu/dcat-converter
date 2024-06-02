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
├── configs                                   ---> all the config.ini files of the repositories.
│   ├── config_fuberlin.ini
│   ├── config_huberlin.ini
│   └── config_tuberlin.ini
├── data                                      ---> RDFs will be in this folder.
│   ├── fu_berlin.rdf
│   ├── hu_berlin.rdf
│   ├── sample.rdf
│   └── tu_berlin.rdf
├── dockerfile
├── requirements.txt                           ---> Libraries
├── schema                                     ---> dcat elements, terms, and dcat_ap, oai_dc
├── schema_matching_experiments                ---> Prompting and similarity calculation to find correspondences between dcat elements and terms according to [1]
└── src
    ├── converter_service.py                   ---> The converter will run from this script.
    ├── data_crawler.py
    ├── dcat_ap.py
    ├── matches.py
    ├── schema_matcher
    └── utils.py
````
## How to run on a conda environment
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
$ pip install -r requirements.txt
```

*  ```config_reponame.ini``` under configs folder has the specific data crawling parameters.

## 1. Repository APIs


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
 
## 2. Data Collection and Converter
* Run the script below:
```
$ python src/converter_service.py
```
## 3. Pipeline
![Pipeline](https://github.com/sefeoglu/dcat-converter/blob/master/doc/bua_converter.png)

* BOP Docker Compose
  ```bash
  https://github.com/sefeoglu/bop-docker-compose
  ```
* BOP UI, which is based on piveau UI .
  ```bash
  https://github.com/sefeoglu/bua-bop-ui
  ```
* BOP RDF Importer, which was modified from piveau rdf importer
  ```bash
  https://github.com/sefeoglu/bop-consus-importing-rdf
  ```
Note: UI and RDF importer's images below are registered on fokus servers, so please register their images on your own server.


------------------------------------------------------------------
### References
[1] Conversational Ontology Alignment with ChatGPT.
````bash
@misc{norouzi2023conversational,
      title={Conversational Ontology Alignment with ChatGPT}, 
      author={Sanaz Saki Norouzi and Mohammad Saeid Mahdavinejad and Pascal Hitzler},
      year={2023},
      eprint={2308.09217},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
````
### Citation
```bash
@misc{efeoglu2024converter,
      title={Converter: Enhancing Interoperability in Research Data Management}, 
      author={Sefika Efeoglu and Zongxiong Chen and Sonja Schimmler and Bianca Wentzel},
      year={2024},
      eprint={2404.13406},
      archivePrefix={arXiv},
      primaryClass={cs.DL}
}
```

