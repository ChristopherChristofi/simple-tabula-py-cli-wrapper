# Tabula-py-cli-wrapper

## Description:

I had to group together an assortment of business documents; with invoices originating from more than one source, of which one persisted of tabular sales data in PDF format: making it difficult to collate such data with all the other sales data. [tabula-py](https://tabula-py.readthedocs.io/en/latest/) proved most useful and made it easy to convert the tabular PDF into a spreadsheet. In this repo I have put together a simple command-line wrapper for the tabula-py library functionality, of which I used to make my work process a bit simpler.

## Usage:

```sh
tabulapycliwrapper --pdf-data INPUT_DATA_FILE.pdf --output-path OUTPUT_DATA.csv --page 2
```

## Dependencies:

- tabula-py
- click
