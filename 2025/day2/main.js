 const splitStringInMiddle = (str) {
  const middleIndex = Math.floor(str.length / 2);
  return str.substring(0, middleIndex) === str.substring(middleIndex);
}

function range(start, end, step = 1) {
  const result = [];
  for (let i = start; i <= end; i += step) {
    result.push(i);
  }
  return result;
}

``.split(',').map(e => range(...e.trim().split('-').map(Number)).map(e => ''+e).filter(splitStringInMiddle)).flat().map(Number).reduce((a,b) => a+b, 0) 
