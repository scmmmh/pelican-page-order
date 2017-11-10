==================
Pelican Page Order
==================

Simple Pelican plugin to enable explicit page ordering.

Configuration
#############

Load the plugin in your ``pelicanconf.py``

.. code:: python

  PLUGINS = ['pelican_page_order']

and then add explicit order meta-data to the individual pages

.. code:: text

  :order: 1

Pages with no explict order will be placed after pages with an explicit order.
Pages with the same order number or with no explicit order will be ordered
alphabetically.

Theming
#######

For theming purposes each page has the following additional attribute:

* ``order`` - The absolute order index
