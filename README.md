Equipe Data DiscoveryOne
==============================

Projeto realizado na formação do Instituto Atlântico - Atlântico Academy Future

## Análise de Compras da Olist

A Olist é uma startup brasileira que atua no segmento de vendas pela internet (e-commerce). Através da sua plataforma de serviços, ela é um mediador e possibilita que outras empresas se inscrevem e vendam seus produtos. Em e-commerce, isso é conhecido como marketplace, ou seja, trata-se de uma loja virtual (a Olist) em que o cliente acessa a um site e compra produtos de diversos varejistas, pagando tudo junto, em um único lugar. Sendo assim, a Olist oferta diversas vitrines, como e fosse um shopping, vendendo os mais diversos itens.

## Objetivos e resultados chave

O dataset da Olist, conjunto de dados, concentra diversas informações relacionadas as compras e vendas realizadas por meio da sua plataforma de serviços.
Através dos reviews, análise crítica de dados, do dataset da Olist em relação as compras e vendas realizadas, este trabalho tem os seguintes objetivos:
Obter os reviews das compras e vendas realizadas;
Identificar variáveis e suas influências nos resultados;
Classificar os reviews por análise de sentidos por meio da técnica de processamento de linguagem natural (PLN);
Por meio da análise dos resultados gerados, buscar compreender como é a experiência da compra/uso dos serviços da Olist.
O resultado pretendido por esse trabalho busca conhecer/compreender a experiência dos usuários após utilizarem os serviços da Olist considerando:
Satisfação de uso dos serviços disponibilizados na plataforma (boa, ruim);
Quantitativo e percentual de grupos de respostas;
Orientação para tomada de com base nos resultados gerados.

## Conteúdo

O repositório está organizado seguindo a ideia básica do git-flow, sendo assim, algumas branchs estão disponíveis, sendo elas: a main, onde estão as versões estáveis do código, a develop, que é a linha do tempo principal de desenvolvimento, ou seja, as novas features deverão ser incluídas nela. Por fim, todas as features/atividades são realizadas em uma branch separada e assim que for finalizada é mesclada na develop.  
Neste sentido, no diretório notebook na branch main, está o arquivo referente a primeira entrega, com a exploração de dados inicial, que contem uma avaliação primaria, sobre a quantidade de dados disponíveis e as condições iniciais, está incluído também uma versão inicial da classificação, usando Gaussian Naive Bayes e transformação dos dados usando bag of words.

## Desenvolvedores

Arildo Alves<br>
Nator Júnior<br>
Germano Fenner<br>
Maurício Moura<br>
Rodolfo Ricardo

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
# datadiscoveryone
