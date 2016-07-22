from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Genome(models.Model):
    speciesName = models.CharField(max_length=50)
    taxon = models.CharField(max_length=50)
    auth = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    ucscName = models.CharField(max_length=50)
    twoBitURI = models.CharField(max_length=500)
    chainSet = models.CharField(max_length=500)
    genes = models.CharField(max_length=500)
    genesDescription = models.CharField(max_length=500)
    genesURI = models.CharField(max_length=500)
    stylesheetURI = models.CharField(max_length=500, default = 'www.biodalliance.org/stylesheets/gencode.xml')
    trixURI = models.CharField(max_length=500)
    collapseSuperGroups = models.BooleanField('True')


    def get_absolute_url(self):
        return reverse('genomebrowser:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.speciesName

