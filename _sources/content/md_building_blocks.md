# Markdown building blocks for the platform

This page is a collection of syntaxes for the different building blocks used in the jupyterbook for standard markdown, markdown Myst and Sphynx design

## Websites

https://developer.mozilla.org/en-US/docs/Web/CSS/display



## Headers

Here are the different header blocks used in the chapters

### Exercises Headers:

::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center 
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
__🔙[Back to Homepage](/content/intro.md)__
:::

+++

::::

:::{card}
:link: https://giscience.github.io/gis-training-resource-center/content/Module_2/en_qgis_module_2_exercises.html
__Click here to return to the exercise overview page for module 2__ 
:::

OR

::::{grid} auto
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/intro.html 
{octicon}`home-fill;2em;sd-text-danger`
:::
:::{grid-item-card}
:class-card: sd-text-center sd-rounded-circle
:link: https://giscience.github.io/gis-training-resource-center/content/module_2/en_qgis_module_2_exercises.html 
{octicon}`undo;2em;sd-text-danger`
:::
::::



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

