import pickle
import os

# Créer un tokenizer basique pour MIDLPred
amino_acids = 'ACDEFGHIKLMNPQRSTVWY'

tokenizer = {
    'word_index': {aa: i+1 for i, aa in enumerate(amino_acids)},
    'index_word': {i+1: aa for i, aa in enumerate(amino_acids)},
    'num_words': len(amino_acids) + 1,
    'filters': '',
    'lower': False,
    'char_level': True,
    'document_count': 0,
    'word_docs': {},
    'word_counts': {},
    'index_docs': {}
}

# Créer le dossier models s'il n'existe pas
os.makedirs('models', exist_ok=True)

# Sauvegarder
with open('models/tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)

print("✅ Tokenizer créé avec succès!")
print(f"Acides aminés: {amino_acids}")
print(f"Taille du vocabulaire: {len(amino_acids)}")
print(f"Fichier: models/tokenizer.pkl")

# Tester le tokenizer
test_sequence = "MKWVTFISLL"
encoded = [tokenizer['word_index'].get(aa, 0) for aa in test_sequence]
print(f"\nTest d'encodage pour '{test_sequence}': {encoded}")