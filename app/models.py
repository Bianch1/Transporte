from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

class Tipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo de transporte")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Transporte"
        verbose_name_plural = "Tipos de Transporte"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    pai = models.CharField(max_length=100, verbose_name="Nome do pai")
    mae = models.CharField(max_length=100, verbose_name="Nome da mãe")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    nascimento = models.DateField(verbose_name="Data de nascimento")
    email = models.EmailField(verbose_name="Email")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class Instituicao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da instituição")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"

class Veiculo(models.Model):
    marca = models.CharField(max_length=50, verbose_name="Marca")
    modelo = models.CharField(max_length=50, verbose_name="Modelo")
    placa = models.CharField(max_length=10, unique=True, verbose_name="Placa")
    ano = models.IntegerField(verbose_name="Ano")

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"

class Rota(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, verbose_name='Tipo de transporte')
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituição")
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name="Veículo")
    pessoas = models.ManyToManyField(Pessoa, verbose_name="Pessoas")

    def __str__(self):
        return f"{self.bairro} - {self.instituicao.nome}"

    class Meta:
        verbose_name = "Rota"
        verbose_name_plural = "Rotas"

class Frequencia(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name="Veículo")
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE, verbose_name="Rota")
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituição")
    faltas = models.IntegerField(verbose_name="Quantidade de faltas")

    def __str__(self):
        return f"{self.pessoa} - {self.faltas} faltas"

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"

class Horario(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituição")
    ida = models.TimeField(verbose_name="Horário de ida")
    volta = models.TimeField(verbose_name="Horário de volta")

    def __str__(self):
        return f"{self.instituicao.nome} - Ida: {self.ida} / Volta: {self.volta}"

    class Meta:
        verbose_name = "Horário"
        verbose_name_plural = "Horários"

class Ocorrencia(models.Model):
    descricao = models.TextField(verbose_name="Descrição")
    data = models.DateField(verbose_name="Data")
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name="Veículo")
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE, verbose_name="Rota")

    def __str__(self):
        return f"{self.data} - {self.veiculo.placa}"

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"

class Gasto(models.Model):
    combustivel = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Gasto com combustível")
    reparo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Gasto com reparos")
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name="Veículo")

    def __str__(self):
        return f"{self.veiculo.placa} - Combustível: R${self.combustivel} / Reparo: R${self.reparo}"

    class Meta:
        verbose_name = "Gasto"
        verbose_name_plural = "Gastos"

class Relatorio(models.Model):
    data = models.DateField(verbose_name="Data do relatório")
    frequencia = models.ForeignKey(Frequencia, on_delete=models.CASCADE, verbose_name="Frequência")
    ocorrencia = models.ForeignKey(Ocorrencia, on_delete=models.CASCADE, verbose_name="Ocorrência")
    gasto = models.ForeignKey(Gasto, on_delete=models.CASCADE, verbose_name="Gasto")

    def __str__(self):
        return f"Relatório de {self.data}"

    class Meta:
        verbose_name = "Relatório"
        verbose_name_plural = "Relatórios"
