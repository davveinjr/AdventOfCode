<?php

$input = file("inputwork.txt", FILE_IGNORE_NEW_LINES);

print($input[0]);

function Part1($data){
    foreach($data as $line){
        list($start, $end) = explode("->", $line);
        $start = trim($start);
        $end = trim($end);
        list($x1, $y1) = explode(",", $start);
        list($x2, $y2) = explode(",", $end);

        if($x1 == $x2){ # Vertical Line

        }
        if($y1 == $y2){ # Horizontal Line

        }
    }
}

#$p1 = Part1($input);
#print("Answer to part 1 is: {$p1}\n");

function Part2($data){

}