# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'test'
copyright = '2025, Ashley'
author = 'Ashley'
release = '1.0'

# 定义主文档文件
master_doc = 'index'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    'sphinxemoji.sphinxemoji',
    'rst2pdf.pdfbuilder',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.inheritance_diagram', 
    'sphinx_markdown_tables' 
    ]

source_suffix = {
 '.rst': 'restructuredtext',
 '.txt': 'restructuredtext',
 '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

sphinxemoji_style = 'twemoji'

numfig = True



# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    
    'papersize': 'a4paper',
    
    'pointsize': '10pt',

    'latex_engine': 'xelatex',
    
    'preamble': r'''
        \usepackage{ctex}  
        \usepackage{graphicx}
        \setCJKmainfont{SimSun}
    ''',
    
    'classoptions': ',openany,oneside',

}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'MyProject-Documentation.tex', 'test Hardware User Manual',
     'Ashley', 'manual'), 
]
 
 
# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'rst', 'rst-test',
     ['Ashley'], 1) 
]

