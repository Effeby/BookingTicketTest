BookingTicket est un projet django qui permet de réserver des ticket de film.
vous pouvez consulter tous les films disponibles et en choisir un pour la réservation. une fois choisi vous pouvez consulter les détails du film Côme le réalisateur, la langue, la durée, l'heure de début de la séance, le lieu de la séance...

Ce projet comporte deux applications majeur:
-l'application d'authentification;
-l'application de billetterie.

I- APPLICATION D'AUTHENTIFICATION 

   Cette appli vas permettre d'authentification les utilisateurs, de les enregistrer dans notre base de données et de leur permettre de mettre à jour leur mot de passe.
En gros, l'utilisateur peut soit se connecter s'il a déjà un compte ou dans le cas contraire s'inscrire, il a aussi la possibilité se remettre son password.
-pour la connexion il doit se connecter avec son mail et son mot de passe, s'il est inscrit dans la base de données alors il est redirigé vers la page Acceuil sinon un message d'erreur s'affiche pour lui dire que le mail ou le password est incorrecte;
-pour l'inscription il doit renseigner son email, son username, nom et prénom et mot de passe, si le mail ou le username existe déjà dans la base de données alors un message d'erreur s'affiche lui disant que le mail ou le username son déjà utilisé donc il doit changer d'identifiant.Une fois son compte créé l'utilisateur reçoit sur son solde 5000 f pourquoi cela ? étant donné que c'est un projet académique et que j'ai pas encore trouvé le moyen d'incorporer des payement par carte ou par mobile money, nous donnerons au utilisateurs une somme de base afin de pouvoir réserver des films.
-pour la reinitialisation du mot de passe il doit renseigner son mail d'inscription afin qu'on lui envoie un mail de reinitialisation, s'il le mail n'existe mas dans la base de données alors un message d'erreur s'affiche disant que le mail n'existe pas, si le mail est correct alors on lz félicite et on lui envoie un message sur le mail renseigné afin qu'il puisse modifier son mot de passe.



II- APPLICATIONS DE BILLETERIE

   Cette application permet de consulter les détails de films, et de réserver des ticket pour la séance. Lors de la réservation, l'utilisateur doit d'abord se connecter sinon la réservation est impossible, une fois connecté, il pourra réserver autant de ticket qu'il veux à condition que son solde soit supérieur ou égale au montant total des tickets. si son solde est suffisant alors il pourra réserver et on lui enverrai un mail pour lui dire quel film il a réservé et aussi le nombr3 de ticket qu'il a réservé.
pour un film le nombre de ticket est limité donc s'il ce nombre arrive à 0 alors un message d'erreur s'affiche pour dire "Sold out", si le montant de votre solde est insuffisant alors un message d'erreur s'affiche en disant : solde insuffisant.