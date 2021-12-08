<?php

$myfile = fopen("inputwork.txt", "r") or die("Unable to open file!");
$input = fread($myfile, filesize("inputwork.txt"));
fclose($myfile);

$data = explode("\n\r", $input);

#declare global variables
$numbers = $data[0];


print($data[1]);