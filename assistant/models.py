from django.db import models

class Assistente(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Documento(models.Model):
    assistente = models.ForeignKey(Assistente, on_delete=models.CASCADE, related_name="documentos")
    arquivo = models.FileField(upload_to='documentos/')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Documento para {self.assistente.nome}'
