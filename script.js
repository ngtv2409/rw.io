const cards = document.querySelectorAll(".word-container");
const buttons = document.querySelectorAll(".pagebtn");
const progr = document.querySelector("progress");
const prolab = document.getElementById("prolab")

let current_card = 0; 
let total = cards.length

function showCard() {
    cards.forEach((item, i) => {
        item.style.display = ((i == current_card)? "block" : "none");
    });
    progr.value = (current_card + 1)/total
    prolab.textContent = (current_card + 1) + "/" + total
}

function prevPage() {
    if (current_card > 0) {
        current_card--;
        showCard();
    }
}
function nextPage() {
    if (current_card < total - 1) {
        current_card++;
        showCard();
    }
}

showCard(current_card);
