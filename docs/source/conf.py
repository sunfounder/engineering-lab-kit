# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
import sphinx_rtd_theme
import time  ###

project = 'SunFounder Beginners Lab Kit'
copyright = f'{time.localtime().tm_year}, SunFounder'  ###
author = 'www.sunfounder.com'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autosectionlabel'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# SunFounder logo

html_js_files = [
    'https://ezblock.cc/readDocFile/custom.js', 
    './lang.js', # new
]
html_css_files = [
    'https://ezblock.cc/readDocFile/custom.css',
]

#### RTD+

# html_js_files = [
#     'https://ezblock.cc/readDocFile/custom.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/ace.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/ext-language_tools.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/theme-chrome.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-python.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-sh.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/monokai.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/xterm.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/FitAddon.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/readTheDocIndex.js',

# ]
# html_css_files = [
#     'https://ezblock.cc/readDocFile/custom.css',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/css/index.css',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/css/xterm.css',
# ]



# Multi-language

language = 'en' # Before running make html, set the language.
locale_dirs = ['locale/'] # .po files for other languages are placed in the locale/ folder.

gettext_compact = False # Support for generating the contents of the folders inside source/ into other languages.



# open link in a new window

rst_epilog = """

.. |link_processing_get_started| raw:: html

    <a href="https://processing.org/tutorials/gettingstarted" target="_blank">Getting Started</a>


.. |link_processing_reference| raw:: html

    <a href="https://processing.org/reference/" target="_blank">Processing Reference</a>

.. |link_processing_download| raw:: html

    <a href="https://processing.org/download" target="_blank">Download Processing </a>

.. |link_arduino_lib_page| raw:: html

    <a href="https://www.arduino.cc/reference/en/libraries/" target="_blank">Libraries</a>

.. |link_sf_facebook| raw:: html

    <a href="https://bit.ly/raphaelkit" target="_blank">here</a>


.. |link_wiki_avometer| raw:: html

    <a href="https://en.wikipedia.org/wiki/Avometer" target="_blank">Wikipedia - Avometer</a>


.. |link_docs_ide| raw:: html

    <a href="https://docs.arduino.cc/software/ide-v2/tutorials/getting-started-ide-v2/" target="_blank">Getting Started with Arduino IDE 2</a>


.. |link_arduino_forum| raw:: html

    <a href="https://forum.arduino.cc/" target="_blank">Arduino Forum</a>

.. |link_arduino_project_hub| raw:: html

    <a href="https://projecthub.arduino.cc/" target="_blank">Arduino Project Hub</a>

.. |link_arduino_docs| raw:: html

    <a href="https://docs.arduino.cc/" target="_blank">Official Arduino Documentation</a>

.. |link_download_arduino| raw:: html

    <a href="https://www.arduino.cc/en/software#future-version-of-the-arduino-ide" target="_blank">Arduino Software Page</a>

.. |link_ascii| raw:: html

    <a href="https://www.asciitable.com/" target="_blank">ASCII table of characters</a>

.. |link_arduino_reference| raw:: html

    <a href="https://www.arduino.cc/reference/en/" target="_blank">Language Reference</a>


"""


# language links

rst_epilog += """

.. |link_german_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/3in1-kit-r4/de/latest/" target="_blank">Deutsch Online-Kurs</a>

.. |link_jp_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/3in1-kit-r4/ja/latest/" target="_blank">日本語オンライン教材</a>

.. |link_en_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/3in1-kit-r4/en/latest/" target="_blank">English Online-tutorials</a>

"""

# component pic
rst_epilog += """

.. |components_green_led| image:: /img/list_cpn/lab_list-2.png 
.. |components_red_led| image:: /img/list_cpn/lab_list-3.png 
.. |components_blue_led| image:: /img/list_cpn/lab_list-4.png 
.. |components_yellow_led| image:: /img/list_cpn/lab_list-5.png 
.. |components_white_led| image:: /img/list_cpn/lab_list-6.png 
.. |components_rgb_led| image:: /img/list_cpn/lab_list-7.png 
.. |components_10ohm| image:: /img/list_cpn/lab_list-8.png 
.. |components_100ohm| image:: /img/list_cpn/lab_list-9.png 
.. |components_220ohm| image:: /img/list_cpn/lab_list-10.png 
.. |components_330ohm| image:: /img/list_cpn/lab_list-11.png 
.. |components_1kohm| image:: /img/list_cpn/lab_list-12.png 
.. |components_2kohm| image:: /img/list_cpn/lab_list-13.png 
.. |components_5_1ohm| image:: /img/list_cpn/lab_list-14.png 
.. |components_10kohm| image:: /img/list_cpn/lab_list-15.png 
.. |components_100kohm| image:: /img/list_cpn/lab_list-16.png 
.. |components_1mohm| image:: /img/list_cpn/lab_list-17.png 
.. |components_active_buzzer| image:: /img/list_cpn/lab_list-18.png 
.. |components_passive_buzzer| image:: /img/list_cpn/lab_list-19.png 
.. |components_button| image:: /img/list_cpn/lab_list-20.png 
.. |components_photoresistor| image:: /img/list_cpn/lab_list-21.png 
.. |components_thermistor| image:: /img/list_cpn/lab_list-22.png 
.. |components_potentiometer| image:: /img/list_cpn/lab_list-23.png 
.. |components_7segment| image:: /img/list_cpn/lab_list-24.png 
.. |components_74hc595| image:: /img/list_cpn/lab_list-25.png 
.. |components_ultrasonic| image:: /img/list_cpn/lab_list-26.png 
.. |components_meter| image:: /img/list_cpn/lab_list-27.png 
.. |components_wire| image:: /img/list_cpn/lab_list-28.png
.. |components_breadboard| image:: /img/list_cpn/lab_list-29.png 
.. |components_usb_cable| image:: /img/list_cpn/lab_list-30.png
.. |components_uno_r3| image:: /img/list_cpn/lab_list-31.png 

"""
