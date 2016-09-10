function StringMatch(text, pattern) {
  var textArr = text.split('');
  var patternArr = pattern.split('');
  var success = 0;
  var unsuccess = 0;

  for (var i = 0; i < textArr.length; i++){
    var j = 0;
    while (j < patternArr.length && patternArr[j] === textArr[i + j]){
      j++;
      success++;
    }
    if (j === patternArr.length){
      console.log('success: ' + success);
      console.log('unsuccess: ' + unsuccess);
      return i;
    }
    unsuccess++;
  }
  console.log('success: ' + success);
  console.log('unsuccess: ' + unsuccess);
  return -1;
}


console.log(StringMatch("hello world","o wo"));
