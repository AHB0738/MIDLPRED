from django import forms
from .models import ProteinSequence

class ProteinSequenceForm(forms.ModelForm):
    class Meta:
        model = ProteinSequence
        fields = ['sequence_id', 'sequence']
        widgets = {
            'sequence': forms.Textarea(attrs={
                'rows': 8,
                'cols': 80,
                'placeholder': 'Enter your protein sequence (ex: MKWVTFISLL...)',
                'id': 'sequence-input',
                'class': 'form-control sequence-input',
                'oninput': "this.value = this.value.toUpperCase().replace(/[^A-Z\\n]/g, '');",
                'style': 'font-family: monospace; font-size: 14px;'
            }),
            'sequence_id': forms.TextInput(attrs={
                'placeholder': 'ID optionnel (ex: PATIENT_001, GENE_XYZ)',
                'class': 'form-control',
                'style': 'max-width: 300px;'
            }),
        }
        labels = {
            'sequence': 'Protein sequence',
            'sequence_id': 'Identifier (optional)',
        }
    
    def clean_sequence(self):
        """Nettoyer et valider la séquence"""
        sequence = self.cleaned_data['sequence'].strip().upper()
        if len(sequence) < 10:
            raise forms.ValidationError("The sequence must contain at least 10 amino acids.")
        # Filtrer uniquement les caractères valides
        sequence = ''.join(c for c in sequence if c in 'ACDEFGHIKLMNPQRSTVWY')
        if len(sequence) < 10:
            raise forms.ValidationError("The sequence must contain at least 10 valid amino acids.")
        return sequence