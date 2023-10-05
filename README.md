# Autenticacao
Projeto exemplo para disciplina Software para Serviço
Engenharia de Software - UniEvangélica


## Construa a Imagem Docker:

Abra um terminal e navegue até o diretório NoteSync que contém o Dockerfile e aplicação Flask. Execute o seguinte comando para construir a imagem Docker:

```bash
docker build -t flask-app .
```

Este comando construirá uma imagem chamada "flask-app" com base nas instruções do Dockerfile.

## Execute o Contêiner Docker:

Após construir a imagem, execute o contêiner a partir dela usando o seguinte comando:

```bash
docker run -p 5001:5001 flask-app
```

Este comando mapeia a porta 5001 do contêiner para a porta 5001 em sua máquina host. Você pode ajustar o mapeamento de portas conforme necessário.

## Acesse a Aplicação:

Uma vez que o contêiner esteja em execução, você pode acessar sua aplicação Flask abrindo um navegador da web e navegando até [http://localhost:5001](http://localhost:5001) se estiver executando localmente.


