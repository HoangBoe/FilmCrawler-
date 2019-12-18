# Search Engine
## Requirements
1. [python](https://www.python.org/) and [pip](https://pypi.org/project/pip/)
2. [scrapy](https://scrapy.org/)
3. [java](https://www.java.com/en/) Java 8 or greater
4. [apache solr](https://lucene.apache.org/solr/)


## How to run our spider and store data in file json 
```
1. scrapy crawl filmCrawler -o film.json
```
## How to import data to Solr 

1. Start solr 
```
cd solr...
bin/solr start
```
2. Create solr core filmCrawler:
```
bin/solr create -c filmCrawler
```
3. Post data:
```
bin/post -c filmCrawler <dir>film.json 
```

## Known Issues:


