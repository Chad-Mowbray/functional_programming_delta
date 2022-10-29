const double = n => n * 2



function once(func) {

  let is_callable = true
  return function(n) {
    if (is_callable) {
      is_callable = false
      return func(n)
    } else {
      return 
    }
  }
}


const doubleOnce = once(double)
const res = doubleOnce(3)
const res2 = doubleOnce(4)

console.log(res, res2)