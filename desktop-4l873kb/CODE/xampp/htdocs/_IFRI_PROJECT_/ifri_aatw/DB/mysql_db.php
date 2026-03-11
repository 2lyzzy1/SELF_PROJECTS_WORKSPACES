
<?php
//Inclusion des paramètres de connexion
include_once("myparam.inc.php");
//Connexion au serveur
$idcom = new mysqli(HOST, USER, PASS, "aatw_users");
//Affichage d'un message en cas d'erreurs
if(!$idcom)
{
echo "<script type=text/javascript>";
echo "alert('Connexion impossible à la base)</script>";
}

//********************************
//Requêtes SQL sur la base choisie
include_once("server_conn.php");
$idcom=connexobjet("magasin","myparam");
$requete="SELECT * FROM article ORDER BY categorie";
$result=$idcom->query($requete);
if(!$result)
{
echo "Lecture impossible";
}
else
{
// Lecture des résultats
while ($row = $result->fetch_array(MYSQLI_NUM))
{
foreach($row as $donn)
{
echo $donn,"&nbsp;";
}
echo "<hr />";
}
// Destruction de l'objet $result
$result->free();
}

//********************************
//Fermeture de la connexion
$idcom->close();
?>

<!-- query -->

