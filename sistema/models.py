from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

# class Estabelecimento(models.Model):
# 	nome = models.CharField(max_length=100, unique=True)
# 	slug = models.SlugField(max_length=100)
#
# 	def get_absolute_url(self):
# 		return reverse('estabelecimento-detail',  kwargs={'slug': self.slug, 'id':self.id})
#
# 	def __str__(self):
# 		return self.nome
#
# 	def save(self, *args, **kwargs):
# 		self.slug = slugify(self.nome)
# 		super(Estabelecimento, self).save(*args, **kwargs)

class Predio(models.Model):
	# estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
	nome = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100)

	# class Meta:
	# 	unique_together = ("estabelecimento", "nome")

	def save(self, *args, **kwargs):
		self.slug = slugify("%s" % (self.nome))
		super(Predio, self).save(*args, **kwargs)

	def __str__(self):
		return ("%s" %(self.nome))

class Sala(models.Model):
	predio = models.ForeignKey(Predio, on_delete=models.CASCADE)
	nome = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100)

	class Meta:
		unique_together = (("predio", "nome"),)

	def save(self, *args, **kwargs):
		self.slug = slugify("%s %s" %(self.predio, self.nome))
		super(Sala, self).save(*args, **kwargs)

	def __str__(self):
		return self.nome

class Consumo(models.Model):
	predio = models.ForeignKey(Predio, on_delete=models.CASCADE, null=True)
	sala = models.ForeignKey(Sala, on_delete=models.CASCADE, null=True)
	slug = models.SlugField(max_length=100)
	kwh = models.FloatField()
	data = models.DateField()

	def save(self, *args, **kwargs):
		if not predio and not sala:
			raise Exception("Você não pode deixar estes campos nulos")
		super(self, MyModel).save(*args, **kwargs)

	class Meta:
		unique_together = (("sala", "data"),)

	def save(self, *args, **kwargs):
		self.slug = slugify("%s %s %s" %(self.predio, self.sala.nome, self.data))
		super(Consumo, self).save(*args, **kwargs)

	def __str__(self):
		return ("Sala: %s | Data: %s" %(self.sala.nome, self.data))

	class Meta:
		unique_together = (('sala', 'data'),)