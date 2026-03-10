# MIDLPRED
MIDLPred

MIDLPred: Leveraging Deep Learning on Protein Sequences to Uncover Male Infertility Factors
Author: Abdelhafedh BEN DAHMANE
Affiliations:

Department of Biology, Laboratory of Microbial Engineering and Applications, University of Constantine 1, Constantine, Algeria

Department of Biology, Abbes Laghrour Khenchela University, Khenchela, Algeria
Correspondence: abdelhafedh.ben-dahmane@doc.umc.edu.dz

Motivation

MIDLPred is a deep learning (DL) and natural language processing (NLP) based classification model designed to predict male infertility factors from primary protein sequences.

Methods

Dataset: 10,678 sequences from the MIK database, annotated into four clinical classes: MOTILITY, SHAPE, PHYSIO, OTHER.

Architecture: 1D Convolutional Neural Network (1D-CNN).

Optimization: Cross-validation and an ensemble learning strategy using ten independent models.

Results

Weighted F1-score: 0.96

Accuracy: >98% for some classes

Confusion matrices and ROC curves demonstrate excellent generalization.

MIDLPred identifies relevant molecular patterns related to infertility phenotypes, consistent with current reproductive genetics knowledge.

Conclusion

MIDLPred provides a robust, scalable, and interpretable method for automatic classification of male infertility factors from protein sequences, enabling more precise and personalized diagnostics.

Online Demo

https://midlpred-amob.onrender.com/

Installation
# Clone the repository
git clone https://github.com/AHB0738/MIDLPRED.git
cd MIDLPRED

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
Usage

Prepare your protein sequences in FASTA format.

Run the main prediction script:

python MIDLPRED/predict.py --input sequences.fasta

Obtain predictions for each class (MOTILITY, SHAPE, PHYSIO, OTHER).

Contribution

Contributions are welcome via pull requests. Please follow the project’s code of conduct and coding standards.

License

This project is intended for academic and research use. For any commercial use, please contact the author: abdelhafedh.ben-dahmane@doc.umc.edu.dz
.
