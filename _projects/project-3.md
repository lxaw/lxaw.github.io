---
title: "Comprehensive Food Database"
excerpt: "A comprehensive database of foods in America."
collection: projects
---
Studies with the primary aim of addressing eating disorders focus on assessing the nutrient content of food items with an exclusive focus on caloric intake. 

There are two primary impediments that can be noted in these studies. 

The first of these relates to the fact that caloric intake of each food item is calculated from an existing database. The second concerns the scientific significance of caloric intake used as the single measure of nutrient content. 

By requiring an existing database, researchers are forced to find some source of a comprehensive set of food items as well as their respective nutrients. This search alone is a difficult task, and if completed often leads to the requirement of a paid API service. These services are expensive and non-customizable, taking away funding that could be aimed at other parts of the study only to give an unwieldy database that can not be modified or contributed to. In this work, we introduce a new rendition of the USDA's food database that includes both foods found in grocery stores and those found in restaurants or fast food places. 

At the moment, we have accumulated roughly 1.5 million food entries consisting of approximately 18,000 brands and 100 restaurants in the United States. These foods also have an abundance of nutrient data associated with them, from the caloric amount to saturated fat levels. The data is stored in MySQL format and is spread among five major tables. We have also procured images for these food entries when available, and have included all of our data and program scripts in an open source repository that anyone can access, for free. See [here](https://github.com/lxaw/ComprehensiveFoodDatabase) for more.