import click, tabula


@click.option(
        '--pdf-data',
        type=click.Path(())
        )
@click.option(
        '--ouput-path',
        default='output.csv',
        type=click.Path(())
        )
@click.option(
        '--output-format',
        default='csv',
        type=click.Choice(['csv','JSON','tsv'])
        )
@click.option(
        '--pages',
        type=click.INT
        )
@click.command()
def cli(pdf_data, output_path, output_format, pages):

    if not pages: pages = 'all'

    tabula.convert_into(pdf_data, output_path, output_format, pages)

