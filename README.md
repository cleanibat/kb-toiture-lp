# KB Toiture – Landing page Google Ads « Nettoyage de toiture »

Site statique généré par `build.py` (config en tête de fichier : `GTM_ID`, `SITE_URL`, textes). Modifier, lancer `python3 build.py`, pousser.
Aperçu : https://cleanibat.github.io/kb-toiture-lp/ (illustratif : le formulaire n'envoie rien sur GitHub Pages, il fonctionne une fois `contact.php` déployé sur un hébergement PHP).

Client : KB Toiture, Karl Burel, couvreur zingueur à Saint-Dizier (52). Site principal https://kbtoiture.fr (WordPress chez Hostinger, DNS OVH).

## Checklist de lancement
1. Déployer sur l'hébergement PHP du client (Hostinger, sous-domaine), remettre le workflow `deploy-ssh.yml` du kit.
2. `SITE_URL` = domaine final dans `build.py` (canonical, sitemap).
3. `GTM_ID` dans `build.py`, conteneur importé et publié (`gtm_container.py`).
4. Conversions Google Ads créées et importées dans GTM.
5. Test de bout en bout du formulaire (`contact.php`, leads vers kbtoiture2@gmail.com, Aymeric en copie cachée).

## À confirmer avec le client
- Numéro principal : 06 65 42 50 03 (le site affiche aussi 06 17 76 41 25 et, sur la page nettoyage, « 06 35 42 50 03 »).
- Avis clients réels (ceux du site actuel n'ont pas été repris), ancienneté, photos avant/après de nettoyages.
