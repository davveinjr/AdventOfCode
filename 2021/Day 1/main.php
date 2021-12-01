<?php

#    $data_file = fopen("input.txt", "r") or die("Can't open the file!");
    $input = file("input.txt", FILE_IGNORE_NEW_LINES);


    # Part 1 - How many depth readings are larger than the one before it?  
function Part1($data) {
    $counter = 0;
    for($i = 1; $i < count($data); $i++){
        if($data[$i] > $data[$i - 1]){
            $counter += 1;
        }
    }

    return $counter;
}

$part1_answer  = Part1($input);

print($part1_answer);

    # Part 2 - Part 1, but instead we are using sum of 3 measurements as a sliding window

function Part2($data) {
    $counter = 0;
    for($i = 1; $i < (count($data) - 1); $i++) {
        $current_sum = $data[$i] + $data[$i + 1] + $data[$i + 2];
        $prev_sum = $data[$i] + $data[$i - 1] + $data[$i + 1];

        if($current_sum > $prev_sum){
            $counter += 1;
        }
    }

    return $counter;
}

$part2_answer = Part2($input);
print($part2_answer);

?>