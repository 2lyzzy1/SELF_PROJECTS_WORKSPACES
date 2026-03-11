<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title> PHP </title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="#">upgrade your browser</a> to improve your experience.</p>
        <!-- -->
        <?php
        // $ ;
            $a = 5;
            echo $a. "\n";
            //$users = ["Stacy", 27, "married"];
            //phpinfo();*/
            // $
        ?>
        <button name="butt" onclick=<?php $a++; ?>> <?php echo $a; ?> </button><!-- value="$a" -->

        <?php
            /*
            echo $_SERVER;

            $z = "Trans";
            echo $z[1];
            $ar = [];
            $bod;
            echo var_dump($z)."\n";
            echo var_dump($ar)."\n";
            echo isset($bod)."\n";*/

            //echo "-" * 100;

            /*
            $servers = ["My", "SQL"];
            //echo $servers[0];
            for ($i=0; $i<$servers.count();$i++) {
                echo $servers[$i];
            }
            /*
            $i = 0;
            $server = [""];
            foreach ($server as $servers) {
                echo " Server {$i} :". $servers[$i];
                $i++;
            }*/
            /*
            class user {
                public string $name = "Yan";
            }
            $enterprises = new user;
            echo $enterprises.$name;*/
        ?>
        
        <!-- <script src="" async defer></script> -->
    </body>
</html>