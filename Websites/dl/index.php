<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S.E.S Tool: Download</title>
    <link rel="icon" type="image/x-icon" href="/ses/img/ses.ico">
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
    <?php
        $file = file_get_contents('https://gtav-online-community.com/ses/index.json');
        $json = json_decode($file, true);
        echo '<h1>S.E.S Tool v' . $json["version"] . '</h1>';
        echo '<p>The bin folder is required for the program!</p>';
        echo '<a href="S.E.S%20Tool.zip" target="_blank">Click to download v' . $json["version"] .'</a>';
    ?>
    <div class="footer">
        <p><a href="/ses">main page</a> | <a href="/ses/changelog">changelog</a> | <a href="/ses/how">help page</a></p>
    </div>
</body>
</html>