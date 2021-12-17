<?php
//ini_set('memory_limit', '-1');
$raw_input = file("inputwork.txt", FILE_IGNORE_NEW_LINES); // Input is a single entry array
$input = explode(",", $raw_input[0]); //Splits all into a workable array
$test = array(3, 4, 3, 1, 2);

// Function declaration for use later 
function pipe(mixed $arg, callable ...$fns): mixed{
    foreach($fns as $fn){
        $arg = $fn($arg);
    }
    return $arg;
}


// This is fine for part 1, but part 2 is MUCH more taxing on the machine. Must find a more efficient way to handle. 
function Part1($data, $days){
    $daycounter = 1;
    while($daycounter <= $days){
        $newFishCounter = 0;
        for($i = 0; $i < count($data); $i += 1){
            if($data[$i] == 0){
                $data[$i] = 6;
                $newFishCounter += 1;
            } else {
                $data[$i] -= 1;
            }
        }
        for($i = 0; $i < $newFishCounter; $i += 1){
            array_push($data, 8);
        }
        $daycounter += 1;
    }
    return(count($data));
}

$part1_answer = Part1($input, 80);
print("Answer to Part 1 is: {$part1_answer}");

function Part2($data, $days){

}
