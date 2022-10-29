const double = n => n * 2
const sq = n => n * n
const inc = n => n + 1


let starting = 10

const final1 = inc(sq(double(starting)))
// const final2 = sq(inc(double(starting)))

function pipeline(listFuncs, startingVal) {
  return listFuncs.reduce( (acc, f) => f(acc), startingVal)
}

console.log(final1)
console.log(pipeline([double, sq, inc, sq, inc, inc, double], starting))


