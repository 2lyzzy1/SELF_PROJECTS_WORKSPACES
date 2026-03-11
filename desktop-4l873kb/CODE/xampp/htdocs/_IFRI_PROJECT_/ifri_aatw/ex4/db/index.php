<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title></title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	  <style>
	  	body {
	  		min-height: 100vh;
	  		align-content: center;
	  		background: #e1dcdcff;
	  	}
	  	form {
	  		margin: auto;
	  		padding: 7px;
	  		max-width: 421px;
	  		background: #fafafad0;
	  	}
	  	fieldset {
	  		border: solid 1px black;
	  	}
	  	legend {
	  		font: 18px bolder;
	  	}
	  	input[type=text], input[type=number] {
	  		width: 100%;
	  	}
      input[type=submit] {
        margin-left: 34px;
      }
      input[type=reset] {
        float: right;
        margin-right: 34px;
      }
	  </style>
  </head>
  <body>
    <!--  -->
    <form method="post" action="mysql_db.php">
      <fieldset>
      <legend> Integration </legend>
        <input type="text" name="nom" placeholder="nom">
        <br><br>
        <input type="text" name="nick" placeholder="prenom">
        <br><br>
        <input type="number" name="int" placeholder="age">
        <br><br>
        <input type="submit"> <input type="reset">
      </fieldset>
    </form>
  </body>
</html>
<?php
echo "aatw_users";
?>