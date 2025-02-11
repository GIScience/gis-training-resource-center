# Markdown building blocks for the platform

This page is a collection of syntaxes for the different building blocks used in the jupyterbook for standard markdown, markdown Myst and Sphynx design

## Websites

https://developer.mozilla.org/en-US/docs/Web/CSS/display



## Headers

Here are the different header blocks used in the chapters

### Exercises Headers:

### Module Chapter Headers:

__[Article info:](https://sphinx-design.readthedocs.io/en/pydata-theme/additional.html)__

- block displaying some characteristics of the page

::::{dropdown} Syntax
````
```{article-info}
:avatar: images/ebp-logo.png
:avatar-link: https://executablebooks.org/
:avatar-outline: muted
:author: Executable Books
:date: Jul 24, 2021
:read-time: 5 min read
:class-container: sd-p-2 sd-outline-muted sd-rounded-1
```
````
::::




  - caption: Module 1
    chapters:
      - file: content/Module_1/en_module_1_overview.md
        sections: 
          - file: content/Module_1/en_qgis_theory.md
          - file: content/Module_1/en_qgis_installation.md
          - file: content/Module_1/en_qgis_start.md
          - file: content/Module_1/en_qgis_module_1_exercises.md      
  - caption: Module 2
    chapters:
      - file: content/Module_2/en_module_2_overview.md
        sections:
          - file: content/Module_2/en_qgis_geodata_concept.md
          - file: content/Module_2/en_qgis_projections.md
          - file: content/Module_2/en_qgis_geodata_management.md
          - file: content/Module_2/en_qgis_attribute_table.md
          - file: content/Module_2/en_data_sources.md
          - file: content/Module_2/en_qgis_basemap.md
          - file: content/Module_2/en_qgis_module_2_exercises.md