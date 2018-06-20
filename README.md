# Projeto Integrador ADM

## API REST

#### Consulta e criação de Salas no sistema via api rest:

http://marcmatias.pythonanywhere.com/salas

#### Edição e exclusão de consumos de Salas no sistema via api rest:

http://marcmatias.pythonanywhere.com/salasdetalhe/id

id = chave priméria da sala que se quer editar ou deletar, substitua por numeral inteiro

#### Consulta e criação de Consumos Elétricos Diários no sistema via api rest:

http://marcmatias.pythonanywhere.com/consumos

#### Edição e exclusão de consumos de Consumos Eléticos Diários no sistema via api rest:

http://marcmatias.pythonanywhere.com/consumosdetalhe/id

id = chave priméria da sala que se quer editar ou deletar, substitua por numeral inteiro

## Iniciando

As instruções à seguir vão lhe ajudar a montar o projeto na sua máquina e utilizar o sistema com o banco de dados padrão de testes dbsqlite3 do Django.

### Pré-requisitos

Para rodar o sistema será necessário

```
Python 3.6.1 ou ver superior
Django==2.0.5
django-widget-tweaks==1.4.2
pytz==2018.4
```

### Instalando

Segue um passo a passo de instalação

Este são os passos para rodar o sistema na sua máquina


Crie um ambiente virtual
```
python -m venv myenv
```

Execute o ambiente virtual
```
myenv\Scripts\activate
```


Instale os requerimentos mínimos automaticamente
```
pip install -r requirements.txt
```

Crie um banco de dados
```
python manage.py makemigrations
```
```
python manage.py migrate
```
Crie um usuário no banco de dados

```
python manage.py createsuperuser
```

Execute o sistema no localhost
```
python manage.py runserver
```
<!--
## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). -->

## Autores

* **Alexandre Silva dos Santos** - *Gerente de Projeto*
* **Anibal de Medeiros Batista Filho** - *DBA*
* **Ronaldo Costa Cordeiro** - *Front-End*
* **Rodrigo Oliveira Gomes dos Santos** - *Analista*
* **Marcel Marques** - *Back-End e Front-End* - [Github](https://github.com/marcmatias)

<!-- See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project. -->

<!-- ## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc -->
