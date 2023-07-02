# Introduction
Projet est basé sur la formation en ligne d'OpenClassrooms "[Utilisez Ansible pour automatiser vos tâches de configuration](https://openclassrooms.com/fr/courses/2035796-utilisez-ansible-pour-automatiser-vos-taches-de-configuration)" et a pour objectif de mettre en pratique les concepts et les compétences lié à Ansible. Projet réalisé open-premise dans mon lab.

# Pre-requis :
Vous devez avoir 3 serveurs:
- un serveur qui vous permettra ou est installé ansible pour déployer les config. (node manager)
- un serveur web qui hebergera le wiki
- un serveur de base de donnée qui hebergera la base de donnée

# Objectifs
## Les objectifs du projet :
Configurer un serveur Ubuntu et Mariadb à l'aide d'Ansible.
Configurer l'interconnexion entre les deux serveurs.
Déployer une application Web sur le serveur configuré à l'aide d'Ansible.
Utiliser les meilleures pratiques pour la structuration des fichiers de configuration Ansible.

# Utilisation
Pour utiliser ce projet, vous devez :
1. Cloner le dépôt Git sur votre machine.
2. Modifier le fichier inventory pour inclure l'adresse IP de vos different serveur cible.
3. Modifier les fichiers de configuration de chaque rôle dans le dossier roles.
4. Exécuter la commande ansible-playbook install_XXXX.yml pour lancer le déploiement de l'application.

# Architecture
<img src="https://github.com/Peewty/my_first_ansible_conf/blob/main/Architecture_mediawiki.png" width=50% height=50%>

# Conclusion
Ce projet permet de mettre en pratique les concepts et les compétences présentées dans la formation d'OpenClassrooms en utilisant Ansible pour automatiser la configuration et le déploiement d'un serveur Ubuntu, d'une application Web et d'une BDD MariaDB. Vous pouvez le réutiliser comme vous voulez 😉
