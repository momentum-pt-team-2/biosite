
let quote = document.querySelector('#random-quote')


fetch('https://api.quotable.io/random')
  .then(response => response.json())
  .then(data => {
    let newEl = document.createElement('p')
    newEl.innerText = (`"${data.content}" ~${data.author}`)
    quote.appendChild(newEl)

  })



// quote.addEventListener('click', function(){
//   fetch('https://api.quotable.io/random')
//   .then(response => response.json())
//   .then(data => {
//     let newEl = document.getElementById('p')
//     // newEl.empty()
//     newEl.innerText = (`"${data.content}" ~${data.author}`)
//     quote.appendChild(newEl)

//   });
// });