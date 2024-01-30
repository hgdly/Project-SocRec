# Mini-Projet – Systèmes de recommandation sociale

Github du projet : [Github](https://github.com/hgdly/Project-SocRec)

## Téléchargements

```git
git clone https://github.com/hgdly/Project-SocRec
git submodule update --init --recursive
```

## Éxecution

```bash
# Pour utiliser le dataset Delicious ou Epinions
# Ce programme va créer les fichiers au bon format 
# dans les dossiers epinions et delicious
python3 loader_sampler.py

# Récupérer les données (ep_ratings.txt, ep_trust.txt, 
# dl_ratings, dl_trust.txt) et les placer dans le dossier 
# data de RSAlgorithms

# Configurer configx.py
# Pour utiliser delicious changer dataset_name par dl
# Pour utiliser epinions changer dataset_name par ep

# Lancer dans un premier temps cross_validation.py
cd RSAlgorithms/utility
python3 cross_validation.py

# Puis lancer le model que vous voulez
cd RSAlgorithms/model
# Ici on lance le modèle SocialReg dans lequel on a ajouté nos fonctions de similarité
python3 <model_name>.py
```

## Modèles créés

On a créé deux modèles :

- `social_reg_ADD_jaccard.py` : modèle SocialReg avec la fonction de similarité Jaccard
- `social_reg_ADD_n2v.py` : modèle SocialReg qui implémente Node2Vec

## Données

- [Delicious](https://grouplens.org/datasets/hetrec-2011/)
- [Epinions](https://www.cse.msu.edu/~tangjili/datasetcode/truststudy.htm)

## Références

[1]H. Ma, D. Zhou, C. Liu, M. R. Lyu, and I. King, “Recommender systems with social regularization,” in Proceedings of the fourth ACM international conference on Web search and data mining, Feb. 2011, pp. 287–296. doi: 10.1145/1935826.1935877.

[2]H. Zhang, G. Liu, and J. Wu, “Social Collaborative Filtering Ensemble,” in PRICAI 2018: Trends in Artificial Intelligence, vol. 11012, X. Geng and B.-H. Kang, Eds. Cham: Springer International Publishing, 2018, pp. 1005–1017. doi: 10.1007/978-3-319-97304-3_77.

[3]A. Grover and J. Leskovec, “node2vec: Scalable Feature Learning for Networks,” in Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2016, pp. 855–864. doi: 10.1145/2939672.2939754.