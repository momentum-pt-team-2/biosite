//Quotes from https://github.com/LukePeavey/quotable#get-random-quote
//We are using 'fetch' https://developer.mozilla.org/en-US/Web/API/Fetch_API/Using_Fetch

console.log('linked')
let quote = document.querySelector('#quote-of-the-day')
console.log(quote)

fetch('https://api.quotable.io/random')
.then(response => response.json())
.then(data => {
    let newEl = document.createElement('p')
    newEl.innerText = data.content
    quote.appendChild(newEl)
})
