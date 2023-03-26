const number = document.getElementById("num")
const price = document.getElementById("price")
const category = document.getElementById("cat")



let count = 1;
let adult = 10;
let children = 8;
let student = 7; 
let option = null;

console.log(number)

category.addEventListener("change", function (e) {
    option = e.target.value
    if (option === "Adult") return price.innerHTML = adult * count
    if (option === "Children") return price.innerHTML = children * count
    if (option === "Student") return price.innerHTML = student * count
})

// console.log(number.dataset.capacity)

function increment() {
    if (count < parseInt(number.dataset.capacity)  ){
        count++;
    }
    
    number.innerHTML = count;
    // console.log(parseInt(number.dataset.capacity))
    // console.log(count <= parseInt(number.dataset.capacity) )

    if (option === "Adult") return price.innerHTML = adult * count
    if (option === "Children") return price.innerHTML = children * count
    if (option === "Student") return price.innerHTML = student * count
}

function decrement() {
    if (count > 1) {
        count--;
        number.innerHTML = count;
        if (option === "Adult") return price.innerHTML = adult * count
        if (option === "Children") return price.innerHTML = children * count
        if (option === "Student") return price.innerHTML = student * count
    }
}

function backButton (){
    window.history.back()
}
