#!/usr/local/bin/python3
import csv
import functools

import click
import tabulate


def _handler(item, f):
    if isinstance(f, tuple):
        return f[0](f[1], item)
    else:
        return f(item)


@click.command()
def main():
    items = click.get_text_stream("stdin")
    todo = [
        (map, str.strip),
        (filter, None),
        (map, lambda x: [x]),
        (map, csv.reader),
        (map, next),
        tabulate.tabulate,
        click.echo,
    ]
    functools.reduce(_handler, todo, items)


if __name__ == "__main__":
    main()

# AUTOBIN: csv_to_tab
