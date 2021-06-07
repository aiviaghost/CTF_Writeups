<?php
    $source = show_source("index.php", true);
    echo("<div>");
    print $source;
    echo("</div>");

    if (isset($_GET['shell']) && isset($_GET['pwn'])) {
        if ($_GET['shell'] !== $_GET['pwn'] && hash("sha256", $_GET['shell']) === hash("sha256", $_GET['pwn'])) {
            include("flag.php");
            echo("<h1>$flag</h1>");
        }
        else {
            echo("<h1>Try harder!</h1>");
        }
    }
    else {
        echo("<h1>Collisions are fun to see</h1>");
    }
?>
