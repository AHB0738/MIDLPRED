from django.contrib import admin
from .models import ProteinSequence

@admin.register(ProteinSequence)
class ProteinSequenceAdmin(admin.ModelAdmin):
    list_display = ('sequence_id', 'get_predicted_class', 'get_confidence', 'sequence_preview', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('sequence_id', 'sequence', 'prediction')
    readonly_fields = ('created_at', 'prediction_display')
    fieldsets = (
        (None, {
            'fields': ('sequence_id', 'sequence', 'created_at')
        }),
        ('Prédiction', {
            'fields': ('prediction_display',),
            'classes': ('collapse',)
        }),
    )
    
    def sequence_preview(self, obj):
        return obj.sequence[:50] + '...' if len(obj.sequence) > 50 else obj.sequence
    sequence_preview.short_description = 'Séquence'
    
    def get_predicted_class(self, obj):
        return obj.get_predicted_class()
    get_predicted_class.short_description = 'Classe prédite'
    
    def get_confidence(self, obj):
        return obj.get_confidence()
    get_confidence.short_description = 'Confiance'
    
    def prediction_display(self, obj):
        if obj.prediction:
            return json.dumps(obj.prediction, indent=2, ensure_ascii=False)
        return "Aucune prédiction"
    prediction_display.short_description = 'Résultats détaillés'