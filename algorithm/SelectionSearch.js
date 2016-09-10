function SelectionSearch(elementArray, searchKey) {
  var len = elementArray.length;
  elementArray[len] = searchKey;
  var i = 0;
  while (elementArray[i] !== searchKey) {
    i++;
  }

  if (i < len){
    return i;
  }else{
    return -1;
  }
}

var array = [1,2,3,4,5,6,7,8,12];
console.log(SelectionSearch(array,12));
