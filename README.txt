This repository contains all code and images used for the 2023 ISSW paper: "AUTOMATIC IDENTIFICATION OF SNOW GRAINS USING ARTIFICIAL NEURAL NETWORKS."  The code is organized as follows: 

=== Contents ===
./
- results.txt: contains results from 100 iterations of 5-fold cross validation
- make_X.py: code to create the Xy.npy file required for training and testing
- cross_validate.py: code to run 100 random iterations of 5-fold cross validation using a multilayer perceptron classification model
- plot_results.py: code to visualize the cross validation results. 

./facets/
- images of faceted snow grains (.tiff)
- process.py: code to bootstrap the original images (rotate, flip)
- run_pca.py: code to run the principal component analysis on all .tiff image files
- pca_viz.py: code to visualize using principal component analysis for feature extraction
- original/: contains the original image files (.jpg)

./rounds/ 
- images of rounded snow grains (.tiff)
- process.py: code to bootstrap the original images (rotate, flip)
- run_pca.py: code to run the principal component analysis on all .tiff image files
- original/: contains the original image files (.jpg)

ORDER OF OPERATIONS: 
1) run facets/run_pca.py to create facets/facets.npy.
2) run rounds/run_pca.py to create rounds/rounds.npy.
3) run make_X.py to create Xy.npy (from facets/facets.npy and rounds/rounds.npy)
4) run cross_validate.py to execute 100 randomized iterations of 5-fold cross validation using a MLP classifier. (results get printed to the console).
