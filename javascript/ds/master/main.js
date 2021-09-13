const names = ['nemo', 'simba', 'rex']

function findNemo(array) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === 'nemo') {
      console.log('Found NEMO!')
      break
    }
  }
  console.log('Not Found!')
}

findNemo(names);