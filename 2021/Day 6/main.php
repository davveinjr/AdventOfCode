<?php
//ini_set('memory_limit', '-1');
$raw_input = file("inputpersonal.txt", FILE_IGNORE_NEW_LINES); // Input is a single entry array
$input = explode(",", $raw_input[0]); //Splits all into a workable array
$test = array(3, 4, 3, 1, 2);

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
print("Answer to Part 1 is: {$part1_answer}\n");

function Part2($data, $days){
    $fishies = array( #This dictionary is to count the amount in each phase
        "8" => 0,
        "7" => 0,
        "6" => 0,
        "5" => 0,
        "4" => 0,
        "3" => 0,
        "2" => 0,
        "1" => 0,
        "0" => 0
    );

    foreach($data as $fish){ #Prepopulate the dictionary
        $fish = strval($fish);
        $fishies[$fish] += 1;
    }

    $daycounter = 1;
    while($daycounter <= $days){
        $eight = $fishies['8']; # Establish count of each value
        $seven = $fishies['7'];
        $six = $fishies['6'];
        $five = $fishies['5'];
        $four = $fishies['4'];
        $three = $fishies['3'];
        $two = $fishies['2'];
        $one = $fishies['1'];
        $zero = $fishies['0'];

        $fishies['0'] = $one; # Effectively decrease each number by one, handle "birth"
        $fishies['1'] = $two;
        $fishies['2'] = $three;
        $fishies['3'] = $four;
        $fishies['4'] = $five;
        $fishies['5'] = $six;
        $fishies['6'] = $seven + $zero;
        $fishies['7'] = $eight;
        $fishies['8'] = $zero;

        $daycounter += 1;
    }
    return(array_sum($fishies));
}

$part2_answer = Part2($input, 256);
print("The answer to part 2 is: {$part2_answer}\n");