import os
import sys

# Ajouter le répertoire parent au chemin
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'midlpred_project2026_V1.settings')
import django
django.setup()

from midlpred.midlpred_predictor import MIDLPredPredictor

def check_models():
    """Vérifier que tous les modèles sont présents"""
    models_dir = os.path.join(os.path.dirname(__file__), 'models')
    
    print(f"Vérification des modèles dans: {models_dir}")
    print("=" * 60)
    
    # Vérifier l'existence des fichiers
    missing_models = []
    existing_models = []
    
    for i in range(20):
        model_file = f"ensemble_model_{i}.h5"
        model_path = os.path.join(models_dir, model_file)
        
        if os.path.exists(model_path):
            existing_models.append(model_file)
            print(f"✓ {model_file}")
        else:
            missing_models.append(model_file)
            print(f"✗ {model_file} - MANQUANT")
    
    print("=" * 60)
    print(f"Modèles trouvés: {len(existing_models)}/20")
    
    if missing_models:
        print(f"Modèles manquants: {len(missing_models)}")
        for model in missing_models:
            print(f"  - {model}")
    
    # Tester le chargement du prédicteur
    print("\nTest du chargement du prédicteur...")
    print("=" * 60)
    
    predictor = MIDLPredPredictor(models_dir=models_dir)
    success = predictor.load()
    
    print(f"\nStatut: {predictor.status}")
    print(f"Modèles chargés: {len(predictor.models)}")
    
    if success and predictor.models:
        print(f"\nClasses: {predictor.classes}")
        print(f"Max longueur: {predictor.MAX_LENGTH}")
        
        # Tester une prédiction
        test_sequence = "MKWVTFISLLFLFSSAYSRGVFRRDAHKSEVAHRFKDLGEENFKALVLIAFAQYLQQCPF"
        print(f"\nTest de prédiction sur séquence de {len(test_sequence)} AA...")
        
        result = predictor.predict(test_sequence)
        print(f"Classe prédite: {result['predicted_class']}")
        print(f"Confiance: {result['confidence']:.2%}")
        print(f"Modèle utilisé: {result['model_used']}")

if __name__ == "__main__":
    check_models()