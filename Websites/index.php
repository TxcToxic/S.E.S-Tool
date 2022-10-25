<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S.E.S Tool</title>
    <link rel="icon" type="image/x-icon" href="https://gtav-online-community.com/ses/img/ses.ico">
    <style>
        body {
            background-color:#131313;
            color:#003ac2;
            font-family:Consolas;
        }
        h1 {
            text-decoration: underline;
        }
        a {
            color:#ff0000;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .main {
            background-color:#131313;
            color:#003ac2;
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #101010;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1><a href="https://discord.gg/6MTF772zpu" class="main">S.E.S Tool</a></h1>
    <p>S.E.S Tool is a little tool for Garry's Mod created from <a href="/toxic" target="_blank">-TOXIC-#1835</a> for <a href="https://discord.gg/6MTF772zpu" target="_blank">Source Engine Shitter</a></p>

    <p>You can download S.E.S Tool <a href="dl">here</a></p>
    <p><a href="how">How does it work?</a>
    <p><a href="steam://rungameid/4000">Run Garry's Mod</a>
    <p>----------- Information -----------</p>
    <?php
        $eVersion = file_get_contents('https://gtav-online-community.com/ses/index.json');
        $version = json_decode($eVersion, true)["version"];
        $available = json_decode($eVersion, true)["available"];
        $hwidlock = json_decode($eVersion, true)["hwidlock"];
        echo '<p>Current Version: ' . $version . '</p>';
        if ("$available" == "1") {
            echo '<p>Availability: Available</p>';
        } else {
            echo '<p>Availability: Unavailable</p>';
        }
        if ("$hwidlock" == "1") {
            echo '<p>Hwid Lock: Enabled</p>';
        } else {
            echo '<p>Hwid Lock: Disabled</p>';
        }
    ?>
    <div class="footer">
        <p><a href="changelog">changelog</a> | <a href="how">help page</a> | <a href="dl">download page</a></p>
    </div>
</body>
</html>