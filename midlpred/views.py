import numpy as np
import json
import os
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from .forms import ProteinSequenceForm
from .models import ProteinSequence
from .midlpred_predictor import MIDLPredPredictor
import hashlib

# Initialiser le prédicteur une seule fois
_predictor_instance = None

def get_predictor():
    """Singleton pour le prédicteur MIDLPred Ensemble"""
    global _predictor_instance
    if _predictor_instance is None:
        models_dir = os.path.join(settings.BASE_DIR, 'models')
        _predictor_instance = MIDLPredPredictor(models_dir=models_dir)
        _predictor_instance.load()
    return _predictor_instance

def home(request):
    """Page d'accueil avec formulaire de saisie"""
    if request.method == 'POST':
        form = ProteinSequenceForm(request.POST)
        if form.is_valid():
            # Sauvegarder la séquence
            protein_seq = form.save(commit=False)
            
            # Obtenir le prédicteur
            predictor = get_predictor()
            
            # Faire la prédiction
            result = predictor.predict(protein_seq.sequence)
            
            # Ajouter des informations supplémentaires
            result['sequence_length'] = len(protein_seq.sequence)
            result['amino_acid_composition'] = predictor.calculate_amino_acid_composition(protein_seq.sequence)
            
            # Sauvegarder la prédiction
            protein_seq.prediction = result
            protein_seq.save()
            
            # Préparer le contexte pour les résultats
            context = {
                'form': ProteinSequenceForm(),  # Nouveau formulaire vide
                'result': result,
                'sequence_id': protein_seq.sequence_id or f"SEQ_{protein_seq.id}",
                'sequence_preview': protein_seq.sequence[:100] + '...' if len(protein_seq.sequence) > 100 else protein_seq.sequence,
                'sequence_obj': protein_seq,
            }
            
            return render(request, 'midlpred/result.html', context)
    else:
        form = ProteinSequenceForm()
    
    # Obtenir les informations du modèle pour l'affichage
    predictor = get_predictor()
    
    context = {
        'form': form,
        'model_status': predictor.status,
        'model_info': predictor.get_model_info(),
        'class_descriptions': predictor.class_descriptions,
        'recent_predictions': ProteinSequence.objects.all().order_by('-created_at')[:5],
    }
    
    return render(request, 'midlpred/home.html', context)

# AJOUTEZ CETTE FONCTION MANQUANTE
def api_predict(request):
    """API pour les prédictions JSON"""
    if request.method == 'POST':
        try:
            # Charger les données JSON
            data = json.loads(request.body.decode('utf-8'))
            sequence = data.get('sequence', '').strip().upper()
            sequence_id = data.get('sequence_id', f"API_{hashlib.md5(sequence.encode()).hexdigest()[:8]}")
            
            if not sequence:
                return JsonResponse({'error': 'Sequence is required'}, status=400)
            
            # Valider la séquence
            sequence = ''.join(c for c in sequence if c in 'ACDEFGHIKLMNPQRSTVWY')
            if len(sequence) < 10:
                return JsonResponse({'error': 'Sequence must contain at least 10 valid amino acids'}, status=400)
            
            # Obtenir le prédicteur
            predictor = get_predictor()
            
            # Faire la prédiction
            result = predictor.predict(sequence)
            result['sequence_length'] = len(sequence)
            result['sequence_id'] = sequence_id
            
            # Sauvegarder dans la base de données si demandé
            if data.get('save', False):
                ProteinSequence.objects.create(
                    sequence=sequence,
                    sequence_id=sequence_id,
                    prediction=result
                )
            
            return JsonResponse(result)
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    # Si ce n'est pas une requête POST, retourner une erreur
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def clear_history(request):
    """Effacer l'historique des prédictions"""
    if request.method == 'POST':
        ProteinSequence.objects.all().delete()
        return redirect('home')
    return redirect('home')

def about(request):
    """Page À propos de MIDLPred"""
    predictor = get_predictor()
    
    return render(request, 'midlpred/about.html', {
        'model_info': predictor.get_model_info(),
        'class_descriptions': predictor.class_descriptions,
        'total_predictions': ProteinSequence.objects.count(),
    })