console.log("Hello, you");

let nod = document.querySelector("#nod");

fetch("https://api.math.tools/numbers/nod")
    .then((response) => response.json())
    .then((data) => {
        let newEl = document.createElement("p");
        newEl.innerText = data.contents.nod.numbers.number;
        nod.appendChild(newEl);
    });
