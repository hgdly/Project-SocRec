# Mini-Projet – Systèmes de recommandation sociale

Dépôt Github du projet : [Github](https://github.com/hgdly/Project-SocRec)

## Téléchargements

```git
git clone https://github.com/hgdly/Project-SocRec
cd Project-SocRec
git submodule update --init --recursive
```

## Installation

```bash
pip3 install -r requirements.txt
```

## Exécution

#### Pour obtenir les analyses des datasets

```
descriptive_analysis.ipynb
```

#### Pour utiliser le dataset Delicious ou Epinions

Lancer le programme `loader_sampler`. Il va créer les fichiers au bon format dans les dossiers epinions et delicious

```bash
python3 loader_sampler.py
```

Récupérer les données (`dl_ratings`, `dl_trust`, `ep_ratings`, `ep_trust`) qui sont dans les dossiers `delicious` et `epinions` et les placer dans le dossier `data` de RSAlgorithms

### Configurer configx.py

Pour utiliser delicious changer `dataset_name` par `dl`

Pour utiliser epinions changer `dataset_name` par `ep`

Lancer dans un premier temps `cross_validation.py`

```bash
cd RSAlgorithms/utility
python3 cross_validation.py
```

Puis lancer le modèle que vous voulez

```bash
cd RSAlgorithms/model
python3 <nom_du_modele>.py
```

## Modèles

- `social_reg_ADD_jaccard.py` : SocialReg avec la similarité calculée avec le coefficient de Jaccard.
- `social_reg_ADD_n2v.py` : SocialReg avec l'algorithme node2vec.

## Données

- [Delicious](https://grouplens.org/datasets/hetrec-2011/)
- [Epinions](https://www.cse.msu.edu/~tangjili/datasetcode/truststudy.htm)

## Références

[1]H. Ma, D. Zhou, C. Liu, M. R. Lyu, and I. King, “Recommender systems with social regularization,” in Proceedings of the fourth ACM international conference on Web search and data mining, Feb. 2011, pp. 287–296. doi: 10.1145/1935826.1935877.

[2]H. Zhang, G. Liu, and J. Wu, “Social Collaborative Filtering Ensemble,” in PRICAI 2018: Trends in Artificial Intelligence, vol. 11012, X. Geng and B.-H. Kang, Eds. Cham: Springer International Publishing, 2018, pp. 1005–1017. doi: 10.1007/978-3-319-97304-3_77.

[3]A. Grover and J. Leskovec, “node2vec: Scalable Feature Learning for Networks,” in Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2016, pp. 855–864. doi: 10.1145/2939672.2939754.
