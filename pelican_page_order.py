'''
###########################################
Pelican plugin to generate a page hierarchy
###########################################
'''
import os

from itertools import chain
from pelican import signals, contents


def update_order(generator):
    """Adds ``order``, ``parents``, and ``children`` attributes to all
    pages.
    """
    generator.pages.sort(key=lambda p: (int(p.order), p.slug) if hasattr(p, 'order') else (float('inf'), p.slug))
    for idx, page in enumerate(generator.pages):
        page.order = idx


def register():
    """Registers the processing callbacks."""
    signals.page_generator_finalized.connect(update_order)
