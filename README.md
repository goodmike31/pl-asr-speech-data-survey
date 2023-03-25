Polish ASR speech datasets survey and catalog.

# Survey goals
- Organization of publicly available information about Polish ASR speech datasets into the catalog.
- Providing the ASR community with a collectively maintained, up-to-date source of information about available datasets.
- Identification of ASR speech datasets for Polish, which are freely available for research and commercial purposes.
<br>

# Survey results:
- **Fifty-one datasets** intended for Polish ASR development were identified based on the information available in the public domain.
- The **total** **size** of **documented Polish ASR speech data** amounts to approx. **26400** **hours** of **audio** and **5300** **hours** of **transcribed** speech.
- **One thousand hours** worth of speech data is **available** in a public domain.
- Over **3100 hours** of speech data is available through commercial providers.
- Each dataset is described with up to 60 attributes. See [Attributes description](https://github.com/goodmike31/pl-asr-speech-data-survey#attributes) for details.
* Detailed analysis results will be available in the article soon.
* Resulting Polish ASR speech datasets catalog is available in 2 formats:
  * [Google Sheets](https://docs.google.com/spreadsheets/d/181EDfwZNtHgHFOMaKNtgKssrYDX4tXTJ9POMzBsCRlI/edit?usp=sharing)
  * [TSV](https://github.com/goodmike31/pl-asr-speech-data-survey/blob/main/snapshots/pl-asr-speech-datasets-catalog-latest.tsv)

# How to contribute to the Polish ASR speech datasets catalog 
## 1. To report a bug in the catalog:
* Open an [issue](https://github.com/goodmike31/pl-asr-speech-data-survey/issues), describe it and label it as "bug".
* (alternatively) Leave a comment in the Google Sheet.

## 2. To propose adding or modyfing catalog attributes:
* Open an [issue](https://github.com/goodmike31/pl-asr-speech-data-survey/issues), describe your proposal (attribute name, meaning and motivation) and label it as "enhancement".
* (alternatively) Leave a comment in the Google Sheet and describe your proposal.


# How to identify public domain PL ASR speech datasets
1. Open the [catalog](https://docs.google.com/spreadsheets/d/181EDfwZNtHgHFOMaKNtgKssrYDX4tXTJ9POMzBsCRlI/edit?usp=sharing)
2. Set filter on **Usage cost** column to **free**

# Addendum - Survey design  

## Dataset characteristics analysis process
- Publicly available information sources were analyzed, annotated, and standardized with 60 attributes.
- Additionally, the content of publicly available datasets was analyzed automatically.
 
## Information sources
* Language Data Repositoriesadc.upenn.edu/)
  * [ELRA Catalog](http://catalogue.elra.info/en-us/)
  * [META-SHARE repository](http://www.meta-share.org/)
  * [CLARIN ERIC - Virtual Language Observatory](https://vlo.clarin.eu/)
  * [CLARIN-PL - D-space](https://clarin-pl.eu/dspace/)
  * [Open Science Resource Atlas 2.0 (AZON)](https://zasobynauki.pl/)
  * [PELCRA](http://pelcra.pl/new/tools_and_resources)
  * [Hamburger Zentrum fur Sprach Corpora HZSK](https://corpora.uni-hamburg.de/hzsk/)
* Other
  * [PolEval 2019 competition](http://2019.poleval.pl/)
  * [Google dataset search](https://datasetsearch.research.google.com/)
  * [Kaggle](https://www.kaggle.com/)
  * [Hugging face](https://huggingface.co/)
  * [Google Scholar Search](https://scholar.google.com/) (keywords: Polish, ASR, speech corpus, dataset, etc.)
  * [Google Web Search](https://www.google.com/) (keywords: Polish, ASR, speech corpus, dataset, etc.)

## Catalog attributes
- Each dataset is described with up to 60 attributes covering:
  - authorship, creation date, funding, etc.
  - availability, licensing, pricing, etc.
  - content e.g. audio format, number of speakers recorded, meta-data distributions, etc.
- Values of attributes not reported by dataset authors, publishers, or researchers are recreated, when feasible (e.g. number of recordings)
- Full list of attributes, their purpose and allowed values is available as:
  - [Google sheet](https://docs.google.com/spreadsheets/d/181EDfwZNtHgHFOMaKNtgKssrYDX4tXTJ9POMzBsCRlI/edit?usp=sharing)
  - [TSV](https://github.com/goodmike31/pl-asr-speech-data-survey/blob/main/snapshots/pl-asr-speech-datasets-taxonomy-latest.tsv)


## Limitations
The metadata collected for the catalog and used to draw conclusions is primarily based on information available online in language repositories and scientific articles. When feasible, it was further verified through manual inspection of dataset content and discussion with dataset authors. Despite our best efforts, some important metadata values may be missing. Naturally, if the original source of metadata contained errors, the resulting values in the catalog, as well as metrics and derived observations, may be biased or inaccurate. Additionally, despite our best efforts to manually validate all collected data before publication, the catalog may contain inaccuracies resulting from curation- related errors. 
We hope that making the catalog publicly available to the community will enable collective curation of the catalog and taxonomy, particularly by ad- dressing any errors in the catalog metadata that have practical impact on the community. Engaging in discussions is also crucial for filling in missing values, establishing the availability of datasets with unknown status, and determining licensing and re-usage of existing datasets for Polish ASR benchmarking purposes. Lastly, all datasets available online are subject to automatic analysis to draw new insights from the data and verify values reported by the authors in the documentation. This process, however, may introduce additional limitations in terms of the accuracy and reliability of the resulting insights.
