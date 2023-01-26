//Because I'm lazy, I will be manually loading the stacks for this problem
//Vertical parsing is a pain in the ass

#region Stack init
Stack<string> stackOne = new Stack<string>();
Stack<string> stackTwo = new Stack<string>();
Stack<string> stackThree = new Stack<string>();
Stack<string> stackFour = new Stack<string>();
Stack<string> stackFive = new Stack<string>();
Stack<string> stackSix = new Stack<string>();
Stack<string> stackSeven = new Stack<string>();
Stack<string> stackEight = new Stack<string>();
Stack<string> stackNine = new Stack<string>();
#endregion
#region Populate Stack 1
stackOne.Push("W");
stackOne.Push("D");
stackOne.Push("G");
stackOne.Push("B");
stackOne.Push("H");
stackOne.Push("R");
stackOne.Push("V");
#endregion
#region Populate Stack 2
stackTwo.Push("J");
stackTwo.Push("N");
stackTwo.Push("G");
stackTwo.Push("C");
stackTwo.Push("R");
stackTwo.Push("F");
#endregion
#region Populate Stack 3
stackThree.Push("L");
stackThree.Push("S");
stackThree.Push("F");
stackThree.Push("H");
stackThree.Push("D");
stackThree.Push("N");
stackThree.Push("J");
#endregion
#region Populate Stack 4
stackFour.Push("J");
stackFour.Push("D");
stackFour.Push("S");
stackFour.Push("V");
#endregion
#region Populate Stack 5
stackFive.Push("S");
stackFive.Push("H");
stackFive.Push("D");
stackFive.Push("R");
stackFive.Push("Q");
stackFive.Push("W");
stackFive.Push("N");
stackFive.Push("V");
#endregion
#region Populate Stack 6
stackSix.Push("P");
stackSix.Push("G");
stackSix.Push("H");
stackSix.Push("C");
stackSix.Push("M");
#endregion
#region Populate Stack 7
stackSeven.Push("F");
stackSeven.Push("J");
stackSeven.Push("B");
stackSeven.Push("G");
stackSeven.Push("L");
stackSeven.Push("Z");
stackSeven.Push("H");
stackSeven.Push("C");
#endregion
#region Populate Stack 8
stackEight.Push("S");
stackEight.Push("J");
stackEight.Push("R");
#endregion
#region Populate Stack 9
stackNine.Push("L");
stackNine.Push("G");
stackNine.Push("S");
stackNine.Push("R");
stackNine.Push("B");
stackNine.Push("N");
stackNine.Push("V");
stackNine.Push("M");
#endregion

List<Stack<string>> stacks = new List<Stack<string>>(){
    stackOne, stackTwo, stackThree, stackFour, stackFive, stackSix, stackSeven, stackEight, stackNine
};


//This is where the real problem begins!

string contents = File.ReadAllText(@"input.txt");

string[] splitContents = contents.Split(new string[] {"\r\n\r\n"}, StringSplitOptions.None);
string commands = splitContents[1];

// foreach(string line in commands.Split("\n")){
//     //each of these strings need to be split by spaces
//     //items of interest are at [1], [3], [5] in the string arrays

//     string[] instructions = line.Split(" ");

//     int amount = int.Parse(instructions[1]);
//     int from = int.Parse(instructions[3]);
//     int to = int.Parse(instructions[5]);

//     for (int i = 1; i <= amount; i++){
//         stacks[to - 1].Push(stacks[from - 1].Pop());
//     }
// }

// for (int i = 0; i < stacks.Count; i++) {
//     Console.Write(stacks[i].Peek());
// }

List<Stack<string>> stacksTwo = new List<Stack<string>>(){
    stackOne, stackTwo, stackThree, stackFour, stackFive, stackSix, stackSeven, stackEight, stackNine
};

foreach(string lineTwo in commands.Split("\n")){
    string[] instructionsTwo = lineTwo.Split(" ");

    int amount = int.Parse(instructionsTwo[1]);
    int from = int.Parse(instructionsTwo[3]);
    int to = int.Parse(instructionsTwo[5]);
    Stack<string> tempStack = new Stack<string>();

    for (int i = 1; i <= amount && stacksTwo[from - 1].Count != 0; i++){
        tempStack.Push(stacksTwo[from - 1].Pop());
    }

    while(tempStack.Count > 0) {
        stacksTwo[to - 1].Push(tempStack.Pop());
    }
}

Console.WriteLine();
for (int i = 0; i < stacksTwo.Count; i++){
    Console.Write(stacksTwo[i].Peek());
}