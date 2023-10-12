# Cytotoxic_nanoparticles
Project for "Programming of Chemical Tasks" from Team 2 (Шатковский Денис, Чечуева Дарья, Уразманова Карина)

Full project's name: "Discovery of selectively cytotoxic inorganic nanoparticles using machine learning reinforced genetic algorithm"       
About project: Nanoparticles have different properties and are used in different fields. For the most part, they are non-toxic and are used in drug delivery. We want to make nanoparticles selectively toxic to cancer cells based on the data that cancer and normal cells have different physiology.               
Aim: building a model that predicts whether a nanoparticle has selective toxicity or not.
      
Results: 
1) Obtained molecular descriptors from the rd kit library;

2) Then the dataset was cleaned (duplicates, omissions were removed);

3) Found correlations, removed unnecessary information. Combined possible features.

4) Engaged in the selection of the optimal predictive model and its improvement subsequently.We made 3 models, R2 with a satisfied setup - about 0.7-0.8.

5) Visualized the data from the dataset with different graphs, found a correlation

6) The result of the model was visualized by the scatterplot R2 graph.

7) Found the parameter with the greatest impact on the prediction result (feature importance)

How to install: pip install -r requirements.txt
Also you need to have 3 datasets (cell_line_descriptors.csv, Cytotoxicity.csv, Incomplete_material_descriptors.xlsx)
