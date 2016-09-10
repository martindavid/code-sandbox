function main(input) {
    //Enter your code here
    var testCase = input[0];
    var maxNum = input[1].split(' ');
    for (var i = 0; i < testCase; i++){
    	for (var j = 0; j <= maxNum[i]; j++){
    		if (j % 3 === 0){
    			process.stdout.write("fizz");
    		}else if (j % 5 === 0){
    			process.stdout.write("buzz");
    		} else{
    			process.stdout.write(j);
    		}
    	}
    }
}

process.stdin.resume();
process.stdin.setEncoding("utf-8");
var stdin_input = "";

process.stdin.on("data", function (input) {
    stdin_input += input;
});

process.stdin.on("end", function () {
   main(stdin_input);
});
