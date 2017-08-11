const ks = require('knapsack-js')

const config = [
  { id: 1, capacity: 5 },
  { id: 1, capacity: 10 },
  { id: 2, capacity: 3 },
  { id: 2, capacity: 6 },
  { id: 2, capacity: 9 },
  { id: 3, capacity: 3 },
  { id: 3, capacity: 5 },
  { id: 3, capacity: 9 }
]

const orders = [
  { id: 1, qty: 10 },
  { id: 2, qty: 15 },
  { id: 3, qty: 13 }
]

// orders.map((order, i) => {
//   const selectedConfig = config.filter(item => {
//     return item.id === order.id;
//   });
//   console.log('Order: ' + order.id);
//   console.log(ks.resolve(order.qty, selectedConfig));
// })


const config_2 = [
  { capacity: 3, value: 5 },
  { capacity: 5, value: 10 },
  { capacity: 9, value: 15 }
]

function nextFit(weight, maxBin) {
  let res = 0;
  let listRest = [];
  let bin_rem = maxBin;

  weight.forEach(function(element) {
    if (element.capacity > bin_rem) {
      res += 1;
      bin_rem = maxBin - element.capacity;
    } else {
      bin_rem -= element.capacity
    }
  }, this);

  return res;
}


function bestFit(weight, maxBin) {
  let res = 1;

  let bin_rem = [];

  weight.sort((a, b) => {
    return b.capacity - a.capacity;
  });


  const maxCapacity = weight.reduce((preval, item) => {
    return preval + item.capacity;
  }, 0);

  const minBin = Math.ceil(maxCapacity / maxBin);
  const max = maxBin + 1;
  
  weight.forEach((val, i) => {
    for(let j = 0; j < res; j++) {
      if (!bin_rem[j]) {
        bin_rem.push({ left: maxBin, item: [] });
      }
      
      while (bin_rem[j].left >= val.capacity) {
        bin_rem[j].left -= val.capacity;
        bin_rem[j].item.push(val);
      }
    }
    res += 1;
  });
  
  bin_rem.sort((a, b) => {
    return a.left - b.left;
  })

  return bin_rem[0];
}

let finalRes = [];

orders.forEach((order) => {
  const selectedConfig = config.filter((val) => {
    return val.id === order.id;
  });

  finalRes.push(bestFit(selectedConfig, order.qty));
})

console.log(finalRes);
