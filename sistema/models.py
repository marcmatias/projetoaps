from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class Estabelecimento(models.Model):
	nome = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100)

	def get_absolute_url(self):
		return reverse('estabelecimento-detail',  kwargs={'slug': self.slug, 'id':self.id})

	def __str__(self):
		return self.nome

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nome)
		super(Estabelecimento, self).save(*args, **kwargs)

class Predio(models.Model):
	estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
	nome = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)

	class Meta:
		unique_together = ("estabelecimento", "nome")

	def save(self, *args, **kwargs):
		self.slug = slugify("%s %s" % (self.estabelecimento, self.nome))
		super(Predio, self).save(*args, **kwargs)

	def __str__(self):
		return ("Predio: %s | Estabelecimento: %s" %(self.nome, self.estabelecimento.nome))

class Sala(models.Model):
	predio = models.ForeignKey(Predio, on_delete=models.CASCADE)
	nome = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100)

	class Meta:
		unique_together = (("predio", "nome"),)

	def save(self, *args, **kwargs):
		self.slug = slugify("%s %s %s" %(self.predio.estabelecimento, self.predio, self.nome))
		super(Sala, self).save(*args, **kwargs)

	def __str__(self):
		return self.nome

class Consumo(models.Model):
	sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
	slug = models.SlugField(max_length=100)
	kWh = models.FloatField()
	data = models.DateField()

	class Meta:
		unique_together = (("sala", "data"),)

	def save(self, *args, **kwargs):
		self.slug = slugify("%s %s %s" % (self.sala.predio.estabelecimento, self.sala.predio, self.sala))
		super(Consumo, self).save(*args, **kwargs)

	def __str__(self):
		return ("Sala: %s | Data: %s" %(self.sala.nome, self.data))

	class Meta:
		unique_together = (('sala', 'data'),)
