# MakeTitlesGreatAgain
Helper file to fix wrong capitalisation in latex references

How often have you compiled your latex document after downloading bibtex entries from different sources and observed errors like this:

* JAMI: fast computation of conditional mutual information for ceRNA network analysis

becomes:

* Jami: fast computation of conditional mutual information for cerna network analysis

because the title line in the corresponding bibtex entry looks like this:

**title = {JAMI: fast computation of conditional mutual information for ceRNA network analysis}**

and not like this

**title = {{JAMI: fast computation of conditional mutual information for ceRNA network analysis}}**

The simple script here can fix this.

### Usage (Python 2.7)

python FixBibTexTitles.py file.bib > newFile.bib
