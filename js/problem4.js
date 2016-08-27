function strReverse(str) {
  return str.split("").reverse().join("");
}

function sortNum(a, b) {
  return a - b;
}

var n1 = 999, n2 = 999;
var res = [];

for(var i = 999; i > 1; i--){
  for(var j = 1; j < 1000; j++){
    var r = n1 * n2;
    if(r.toString() === strReverse(r.toString())) {
      if(!(r in res)){ 
		res.push(r);
      }
    }
	n1--;
  }
  n2--;
  n1 = 999;
}
res.sort(sortNum);
console.log(res[res.length - 1]);
