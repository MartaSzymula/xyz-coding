var numbers = [65, 99, 43, 34, 22, 46, 17, 6, 42, 2, 34, 81, 94, 61, 5, 68, 21, 3, 16, 53, 85, 16, 71, 46, 74, 96, 56, 85, 61, 94, 4, 43, 93, 75, 48, 13, 27, 99, 89, 58, 14, 51, 89, 54, 58, 23, 9, 9, 86, 53, 55, 43, 60, 5, 66, 17, 72, 67, 19, 56, 0, 59, 87, 79, 96, 43, 96, 17, 43, 18, 14, 70, 17, 57, 52, 55, 34, 37, 17, 42, 31, 13, 23, 2, 10, 89, 94, 54, 14, 20, 59, 54, 63, 84, 21, 46, 89, 43, 64, 23];
var evens = 0;
var odds = 0;
// var i = Math.round(k)
for(var i = 0; i < numbers.length; i++){
//   console.log(numbers[i]);
  if(numbers[i] % 2 == 0){
    evens++;

	}
  else{
    odds++;

  }
	}
console.log("Even:", evens);
console.log("Odds", odds);