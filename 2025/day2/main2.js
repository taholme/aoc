const patternRepeats = (str) => {
  const halfLength = Math.floor(str.length / 2);
  for (let i = 1; i <= halfLength; i++) {
    if (str.length % i != 0) continue;
    let substrings = splitStringIntoEqualParts(str, i);
    let pattern = substrings[0];

    if (substrings.length >= 2 && substrings.every((part) => part == pattern)) return true;

  }
  return false;
}

const splitStringIntoEqualParts = (str, partLength) => {
  const numParts = Math.ceil(str.length / partLength);
  return Array.from({ length: numParts }, (_, i) =>
    str.slice(i * partLength, (i + 1) * partLength)
  );
}

function range(start, end, step = 1) {
  const result = [];
  for (let i = start; i <= end; i += step) {
    result.push(i);
  }
  return result;
}

``.split(',').map(e => range(...e.trim().split('-').map(Number)).map(e => '' + e).filter(patternRepeats)).flat().map(Number).reduce((a, b) => a + b, 0) 
