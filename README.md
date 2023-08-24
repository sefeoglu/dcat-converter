# DCAT_AP converter
The project converts the oai_dc formatted meta data into dcat_ap format and save them in rdf format.






* Project Folder Structure
````
.
├── Dockerfile
├── LICENSE
├── README.md
├── compose.yaml
├── config.ini
├── data
│   └── sample.rdf
├── requirements.txt
└── src
    ├── converter_service.py
    ├── data_crawler.py
    ├── dcat_ap.py
    └── utils.py
````
## Docker 

* ```docker build --tag dcat_converter .```

WIP!
## Data Collection
Run the scprit below:
``` 
python data_crawler.py api_url number_of_records_in_a_page total_number_of_records
```
* 1.) Refubium Repository

```
python data_crawler.py "https://refubium.fu-berlin.de/oai/dnb?verb=ListRecords&resumptionToken=xMetaDissPlus////" 100 20338
```

* 2.) Depositonce Repository

```
python data_crawler.py "https://api-depositonce.tu-berlin.de/server/oai/request?verb=ListRecords&resumptionToken=oai_dc////" 100 15424
```
* 3.) Edoc Repository

```
 python data_crawler.py "https://edoc.hu-berlin.de/oai/request/?verb=ListRecords&resumptionToken=oai_dc////" 100 25696
```

* Note:Poster paper from the project has been submitted and waiting for the review, so we will update the readme later. The project will be released, so the repository was updated.
