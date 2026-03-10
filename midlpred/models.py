from django.db import models

class ProteinSequence(models.Model):
    sequence = models.TextField(verbose_name="Protein sequence")
    sequence_id = models.CharField(max_length=100, verbose_name="Sequence ID", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    prediction = models.JSONField(verbose_name="Prediction result", null=True, blank=True)
    
    class Meta:
        verbose_name = "Protein sequence"
        verbose_name_plural = "Proteins sequences"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.sequence_id or 'Sequence'} - {self.created_at.strftime('%d/%m/%Y %H:%M')}"
    
    def get_predicted_class(self):
        """Retourne la classe prédite depuis les résultats JSON"""
        if self.prediction and 'predicted_class' in self.prediction:
            return self.prediction['predicted_class']
        return "N/A"
    
    def get_confidence(self):
        """Retourne la confiance de prédiction"""
        if self.prediction and 'confidence' in self.prediction:
            return f"{self.prediction['confidence']:.2%}"
        return "N/A"