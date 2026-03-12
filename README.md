# MIDLPRED

# MIDLPred: Leveraging Deep Learning on Protein Sequences to Uncover Male Infertility Factors
```
Author: Abdelhafedh BEN DAHMANE
Affiliations:

Department of Biology, Laboratory of Microbial Engineering and Applications, University of Constantine 1, Constantine, Algeria

Correspondence: abdelhafedh.ben-dahmane@doc.umc.edu.dz
```
```
# Motivation

MIDLPred is a deep learning (DL) model utilizing natural language processing (NLP) techniques to predict male infertility factors directly from protein sequences. It provides a scalable and interpretable tool to support precision diagnostics in reproductive medicine.

# Methods

Dataset: 10,678 protein sequences from the MIK database, annotated into four clinical categories: MOTILITY, SHAPE, PHYSIO, OTHER.

Architecture: 1D Convolutional Neural Network (1D-CNN).

Optimization: Cross-validation and ensemble learning using ten independent models.

# Results

Weighted F1-score: 0.96

Accuracy: >98% for some classes

Confusion matrices and ROC curves show excellent generalization.

MIDLPred highlights molecular patterns consistent with known infertility phenotypes.

# Conclusion

MIDLPred offers a robust, interpretable, and automated approach for classifying male infertility factors from protein sequences, facilitating more precise and personalized diagnostics.
```

# Online Demo

https://midlpred-amob.onrender.com/

# Repository Branches
```
This repository contains two branches:

Branch	Purpose
main	Default branch – contains the manuscript, documentation, and supplementary material.
master	MIDLPred Tool – contains all scripts, models, and code to run the MIDLPred protein sequence classifier.
```
# Switch branches or clone a specific branch:
```
# Switch to master branch
git checkout master

# Or clone master directly
git clone -b master https://github.com/AHB0738/MIDLPRED.git
```
# Installation & Usage

# Clone the repository:

```
git clone https://github.com/AHB0738/MIDLPRED.git
cd MIDLPRED
```

# Create a virtual environment:
```
python3 -m venv venv
Linux/macOS
source venv/bin/activate
Windows
venv\Scripts\activate
```

# Install dependencies:
```
pip install -r requirements.txt
```
# Run predictions:
Prepare protein sequences in FASTA format, then run:

python MIDLPRED/predict.py --input sequences.fasta

On Windows, you can also launch the server using:
```
cd C:\###\path\midlpred_project2026_V1
python manage.py runserver
```
Contribution

Contributions are welcome via pull requests. Please adhere to the project’s code of conduct and coding standards.
License

This project is intended for academic and research purposes. For commercial use, contact: ``` abdelhafedh.ben-dahmane@doc.umc.edu.dz ```

## License / Copyright
``` © 2026 Abdelhafedh BEN DAHMANE. All rights reserved. ```
