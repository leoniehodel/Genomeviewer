from django import forms

from .models import Genome


class GenomeForm(forms.ModelForm):

    class Meta:
        model = Genome
        fields = ['speciesName', 'taxon', 'auth', 'version', 'ucscName', 'twoBitURI', 'chainSet',
                  'genes', 'genesDescription', 'genesURI', 'stylesheetURI', 'trixURI', 'collapseSuperGroups']
