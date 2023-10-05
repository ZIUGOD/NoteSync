# Usando uma imagem oficial do Python como imagem pai
FROM python:3.8-slim-buster

# Definindo o diretório de trabalho como /app
WORKDIR /app

# Copiando os conteúdos do diretório atual para o contêiner em /app
COPY . /app

# Instalando pacotes necessários especificados em requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Disponibilizando a porta 80 para o mundo fora deste contêiner
EXPOSE 80

# Definindo a variável de ambiente
ENV NAME World

# Executando app.py quando o contêiner for iniciado
CMD ["python", "app.py"]
