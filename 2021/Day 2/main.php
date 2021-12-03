<?php

$input = file("input.txt", FILE_IGNORE_NEW_LINES);

# Part 1 - Use the directions in the input file to determine your depth and horizontal position

function Part1($data){
    $horizontal = 0;
    $depth = 0;

    foreach($data as $line) {
        list($direction, $value) = explode(" ", $line);
        switch($direction) {
            case "forward":
                $horizontal += (int)$value;
                break;
            case "down":
                $depth += (int)$value;
                break;
            case "up":
                $depth -= (int)$value;
                break;
        }
    }
    return ($horizontal*$depth);
}

$p1_solution = Part1($input);
print("Solution to part 1 is: {$p1_solution}");

function Part2($data){
    $horizontal = 0;
    $depth = 0;
    $aim = 0;

    foreach($data as $line) {
        list($direction, $value) = explode(" ", $line);
        switch($direction) {
            case "forward":
                $horizontal += (int)$value;
                $depth += ($aim * (int)$value);
                break;
            case "down":
                $aim += (int)$value;
                break;
            case "up":
                $aim -= (int)$value;
                break;
        }
    }
    return ($horizontal*$depth);
}

$p2_solution = Part2($input);
print("\nSolution to Part 2 is: {$p2_solution}");