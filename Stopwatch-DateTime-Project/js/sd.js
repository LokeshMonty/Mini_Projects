'use strict';
let datetime = new Date();
console.log(datetime);
document.getElementById("time").textContent = datetime.toLocaleString();
