import click, tabula, logging
from log import logger

@click.option('--pdf-data',
        type=click.Path(()),
        help='Provide the filename and filepath to the PDF data source.'
)
@click.option(
        '--output-path',
        default='output.csv',
        type=click.Path(()),
        help='Provide a filepath for the csv output. Default is output.csv'
)
@click.option(
        '--output-format',
        default='csv',
        type=click.Choice(['csv','JSON','tsv']),
        help='Select an applicable output format. Default is csv'
)
@click.option(
        '--pages',
        type=click.INT,
        help='Provide a page number that holds your selected table. Default is all pages.'
)
@click.option(
        '--log',
        default='tabulapycliwrapper.log',
        type=click.Path(()),
        help='Provide a filepath for a logging file. Default is tabulapycliwrapper.log'
)
@click.command()
def cli(pdf_data, output_path, output_format, pages, log):

    '''Responsible for initiating tabula-py functionality; the conversion of PDF data tables to another format, such as: csv'''


    logger(log)

    if not pages:
        pages = 'all'

    logging.info('converting file: {input}. Page number: {page}'.format(
            input=pdf_data,
            page=pages
            ))

    tabula.convert_into(pdf_data, output_path, output_format=output_format, pages=str(pages))

    logging.info('completed converting file: {input} to {output}. Page number: {page}'.format(
            input=pdf_data,
            output=output_path,
            page=pages
            ))
