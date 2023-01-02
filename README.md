
# Survey goals
- Providing reference source of information about all available Polish ASR speech datasets up-to-date.
- Creating taxonomy and catalog enabling identification of datasets, which are freely available for R&D communities.
<br>

# TLDR 
- The total size of documented Polish ASR speech datasets amounts to over 20000 hours of audio and nearly 2500 hours of transcribed speech.
- One thousand hours worth speech datasets are available online free of charge and over 600 hours of datasets through commercial providers.
- For details about survey please refert to publication: 
- Polish ASR datasets catalog is available as:
  - [Google Sheets](https://docs.google.com/spreadsheets/d/181EDfwZNtHgHFOMaKNtgKssrYDX4tXTJ9POMzBsCRlI/edit?usp=sharing)   - [TSV](https://github.com/goodmike31/pl-asr-datasets-survey/blob/main/pl-asr-datasets-catalog-latest.tsv)

# Survey design

## Information sources

## Taxonomy
|Dataset descriptor                 |Purpose                                                                             |Allowed values                                                                    |
|-----------------------------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
|Dataset name                       |Full name of the speech corpus                                                      |[a-z A-Z\-\_0-9]                                                                  |
|Codename                           |Codename used for reporting                                                         |[a-z\-]                                                                           |
|Access link                        |Link to resource providing access to dataset                                        |url                                                                               |
|Publisher                          |Creator and/or publisher of dataset                                                 |[a-z A-Z]                                                                         |
|Repository                         |Data repository where dataset is listed and/or hosted                               |                                                                                  |
|Languages                          |Language and country code.                                                          |pl-PL, multi                                                                      |
|Creation year                      |Year dataset was created or published.                                              |\d{4}                                                                             |
|License                            |License of dataset                                                                  |Apache, CC-BY, CC-0, Proprietary                                                  |
|ISLRN                              |International Standard Language Resource Number                                     |ISRLN format                                                                      |
|ISBN                               |International Standard Book Number                                                  |ISBN                                                                              |
|LR catalogue ID/URI                |Language data repository specific ID                                                |URL,  [a-z A-Z\-\_0-9]                                                            |
|Reference publication              |Link to relevant publication where dataset is described                             |URL                                                                               |
|Contact point                      |Contact point                                                                       |[a-z A-Z\-\_0-9\@]                                                                |
|Latest version                     |The latest version of released dataset                                              |[0-9\.]                                                                           |
|Last update year                   |Last update year                                                                    |\d{4}                                                                             |
|Available                          |Is dataset available online                                                         |yes, no                                                                           |
|Funding                            |Institution which funded the creation of dataset                                    |[a-z A-Z\-\_0-9]                                                                  |
|usage cost                         |Availability for non-commercial usage                                               |free, paid, no-info                                                               |
|Price - non commercial usage       |Price for non-commercial usage                                                      |[free&#124;\d+]                                                                        |
|Price - Commercial usage           |Price for commercial usage                                                          |[free&#124;\d+]                                                                        |
|Purpose and split                  |Target usage and data split                                                         |train, valid, test, none                                                          |
|Size audio total [hours]           |Audio material                                                                      |[\d+\.]                                                                           |
|Size audio transcribed [hours]     |Transcribed speech material                                                         |[\d+\.]                                                                           |
|Size [GB]                          |Size of dataset in gigabytes.                                                       |[\d+\.]                                                                           |
|Speakers                           |Number of speakers recordings orignate from                                         |[\d+]                                                                             |
|Audio recordings                   |Number of voice recordings in the corpus                                            |\d+                                                                               |
|Audio segmentation                 |Are audio recordings segmented                                                      |yes, no                                                                           |
|Tokens                             |Number of tokens in the corpus                                                      |[\d+]                                                                             |
|Unique tokens                      |Number of unique tokens                                                             |[\d+]                                                                             |
|Automatic QA                       |Type of automatic quality assurance process applied                                 |yes, no                                                                           |
|Manual QA                          |Type of manual quality assurance process applied                                    |yes, no                                                                           |
|Manual QA scope                    |Scope of manual QA applied                                                          |[a-zA-Z \d+]                                                                      |
|Transcription coverage             |Percent of recordings having corresponsing transcription                            |percent                                                                           |
|Transcription protocol             |Is a transcription protocol availble as reference?                                  |yes, no, description                                                              |
|Normalized transcriptions          |Are there available transcriptions without abbreviations, numerals, punctuation etc.|yes, no                                                                           |
|Transcription and annotation format|Format of transcription files                                                       |                                                                                  |
|Domain                             |Domain of utterances                                                                |                                                                                  |
|Speech type                        |Type of speech                                                                      |read, conversional, commands, isolated words, synthetic, multi-type               |
|Audio collection process           |Audio collection process                                                            |controlled, corpus                                                                |
|Speech recordings providers        |Who provided speech recordings                                                      |volunteers, university employees, crowd, public speakers, paid contributors       |
|Acoustic environment               |Acoustic conditions audio was collected in                                          |quiet, various, home, office, tv show, car, public places, entertainment, children|
|Audio device                       |Device audio was recorded with                                                      |various, condenser mic, headset, phone, mobile phone                              |
|Device model                       |Mode of recording device                                                            |[a-zA-Z\- ]                                                                       |
|Audio format                       |Audio encoding format                                                               |wav, flac, raw, mp3, riff                                                         |
|Audio codec                        |                                                                                    |mp3, ogg, vorbis, opus,                                                           |
|Channels                           |                                                                                    |                                                                                  |
|Sampling rate [Hz]                 |Sampling rate of recorded audio                                                     |                                                                                  |
|Bits per sample                    |Number of bits used for encoding each audio sample                                  |                                                                                  |
|Age coverage                       |Is meta-data about speaker age present?                                             |Percent                                                                           |
|Age balanced                       |                                                                                    |description                                                                       |


# Survey results
