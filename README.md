Polish ASR speech data survey and catalog.

# Survey goals
- Organization of publicly available information about Polish ASR speech datasets into the catalog.
- Providing the ASR community with a collectively maintained, up-to-date source of information about available datasets.
- Identification of ASR speech datasets for Polish, which are freely available for research and commercial purposes.
<br>

# Survey results
- **Fifty-one datasets** intended for Polish ASR development were identified
- The **total** **size** of **documented Polish ASR speech data** amounts to over **26400** **hours** of **audio** and nearly **5300** **hours** of **transcribed** speech.
- **One thousand hours** worth speech data is **available** in a public domain
- Over **3100 hours** of speech data available through commercial providers. See [Public domain PL ASR speech datasets]
- Each dataset is described with up to 57 attributes. See [Taxonomy](https://github.com/goodmike31/pl-asr-speech-data-survey#taxonomy) for details.
* Detailed analysis results are available at: 
* Resulting Polish ASR speech datasets catalog is available in 2 formats:
  * [Google Sheets](https://docs.google.com/spreadsheets/d/181EDfwZNtHgHFOMaKNtgKssrYDX4tXTJ9POMzBsCRlI/edit?usp=sharing)
  * [TSV](https://github.com/goodmike31/pl-asr-speech-data-survey/blob/main/snapshots/pl-asr-datasets-catalog-latest.tsv)

# How to contribute to the Polish ASR speech datasets catalog 
## 1. To report a bug in the catalog:
* Open an issue on github, describe it and label as "bug".
* (alternatively) Leave a comment in the Google Sheet.

## 2. To propose an enhancement to the catalog taxonomy:
* Open an issue on github, describe your proposal (descriptor name, meaning and motivation) and label it as "enhancement".
* (alternatively) Leave a comment in the Google Sheet and describe your proposal.


# How to identify public domain PL ASR speech datasets
1. Open [Catalog](https://docs.google.com/spreadsheets/d/181EDfwZNtHgHFOMaKNtgKssrYDX4tXTJ9POMzBsCRlI/edit?usp=sharing)
2. Filter results by column "Usage cost" by allowing only "free" values

# Addendum - Survey design  

## Dataset characteristics analysis process
- Publicly available information sources were analyzed, annotated, and standardized according to the Taxonomy
- Additionally, the content of publicly available datasets was analyzed automatically
 
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

## Taxonomy
- The dataset cards taxonomy consists of 57 attributes.
- Each dataset is described in terms of:
  - authorship, creation date, funding, etc.
  - availability, licensing, pricing, etc.
  - content e.g. audio format, number of speakers recorded, meta-data distributions, etc.
- Values of attributes not reported by dataset authors, publishers, or researchers are recreated, when feasible (e.g. number of recordings)
- Full taxonomy is available as:
  - [Google sheet](https://docs.google.com/spreadsheets/d/181EDfwZNtHgHFOMaKNtgKssrYDX4tXTJ9POMzBsCRlI/edit?usp=sharing)
  - [TSV](https://github.com/goodmike31/pl-asr-speech-data-survey/blob/main/snapshots/pl-asr-datasets-taxonomy-latest.tsv)


## Limitations
Collected meta-data organized into the catalog and used to draw findings is based on the information available online, mostly originating from datasets authors, language repositories, and scientific articles. In case any source values contain errors, resulting metrics and derived observations may be biased or not accurate as well. Additionally, despite of author’s best efforts to validate manually collected data before the publication, the catalog may contain inaccurate information resulting the curation-related error. The author hopes that making the catalog publicly available to the community will enable collective curation of the catalog and taxonomy, especially the correction of errors in the catalog meta-data. The author plans to reach out to dataset creators to discuss missing values, availability of datasets with unknown status, as well as licensing and re-usage of all existing datasets for the Polish ASR benchmarking purposes. Last but not least, all datasets available online were downloaded and are being analyzed automatically, to draw new insights data and verify values reported by the authors in the documentation.
