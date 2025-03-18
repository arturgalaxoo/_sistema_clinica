from django.utils import timezone
from django.db import models



# Aqui fica o model do paciente
class Paciente(models.Model):
      nome = models.CharField(max_length=50)
      sobrenome = models.CharField(max_length=50)
      email = models.EmailField()
      telefone = models.CharField(max_length=20)
      ativo = models.BooleanField(default=False)
      imagem = models.ImageField(upload_to='img/%Y/%m/', blank=True)

      def __str__(self):
       return f'{self.nome} {self.sobrenome}'
      
# Aqui fica o model da especialidade
class Especialidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Medico(models.Model):
      nome = models.CharField(max_length=50)
      sobrenome = models.CharField(max_length=50)
      crm = models.CharField(max_length=6)
      email = models.EmailField()
      data_criacao = models.DateTimeField(default=timezone.now)
      telefone = models.CharField(max_length=20)
      ativo = models.BooleanField(default=True)
      imagem = models.ImageField(upload_to='img/%Y/%m/', blank=True)
      mensagem = models.TextField(blank=True)
    
      def __str__(self):
       return f'{self.nome} {self.sobrenome}'
