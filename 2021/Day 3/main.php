<?php

# Read in file, ignore new line characters
$input = file("inputpersonal.txt", FILE_IGNORE_NEW_LINES);

# Part 1 - Epsilon (least common for each bit) multiplied by Gamma (most common for each bit)
function Part1($data){
    #establish counter dictionary
    $counter = array();
    for($i = 0; $i < 12; $i++){
        $counter[$i] = array();
        $counter[$i]['0'] = 0;
        $counter[$i]['1'] = 0;
    }

    #increment dictionary items as they appear 
    foreach($data as $line){
        for($i = 0; $i < 12; $i++){
            $c = substr($line, $i, 1); 
            $counter[$i][$c] += 1;
        }
    }

    $gamma = '';
    $epsilon = '';
    $power_consumption = 0;

    for($i = 0; $i < 12; $i++){
        $least = $counter[$i]['0'] < $counter[$i]['1'] ? '0' : '1';
        $most = $counter[$i]['0'] > $counter[$i]['1'] ? '0' : '1';

        $gamma .= $most;
        $epsilon .= $least;
    }

    $power_consumption = base_convert($gamma, 2, 10) * base_convert($epsilon, 2, 10);
    return($power_consumption);
}

$p1_answer = Part1($input);

print("Answer to part 1 is: {$p1_answer}\n");

# Part 2 - Life Support Rating = Oxygen Generator Rating * C02 Scrubber Rating
function FindValue($num_list, $weight = 0){
    $offset = 0;
    $continue = true;
    $sum = array();

    while($continue){
        $sum['0'] = 0;
        $sum['1'] = 0;
        $output = array();
        foreach($num_list as $number){
            $bit = substr($number, $offset, 1);
            $sum[$bit] += 1;
        }
        $keep = '0';
        switch($weight){
            case 0: # CO2 - least common, keep 0 if tie
                if($sum['0'] > $sum['1']) $keep = '1';
                if($sum['0'] <= $sum['1']) $keep = '0';
                break;
            case 1: # Oxygen - most common, keep 1 if tie
                if($sum['0'] <= $sum['1']) $keep = '1';
                if($sum['0'] > $sum['1']) $keep = '0';
                break;
            default:
                break;
        }
        foreach($num_list as $number){
            $bit = substr($number, $offset, 1);
            if ($bit == $keep) array_push($output, $number);
        }
        $num_list = $output;
        $offset += 1;
        if($offset == 12) $continue = false;
        if(count($output) == 1) $continue = false;
    }
    return $num_list[0];
}
function Part2($data){
    $oxygen = FindValue($data, 1);
    $co2 = FindValue($data, 0);

    $survival_rating = base_convert($oxygen, 2, 10) * base_convert($co2, 2 ,10);
    return($survival_rating);
}

$p2_answer = Part2($input);
print("Answer to part 2 is: {$p2_answer}");