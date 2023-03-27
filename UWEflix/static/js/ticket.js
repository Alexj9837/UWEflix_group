const toastElement = document.querySelector('.toast-container');

try {


    const student_num = document.getElementById("student_num")
    const children_num = document.getElementById("children_num")
    const adult_num = document.getElementById("adult_num")
    const price = document.getElementById("price")

    const adult_minus = document.getElementById("adult_minus")
    const adult_plus = document.getElementById("adult_plus")

    const children_minus = document.getElementById("children_minus")
    const children_plus = document.getElementById("children_plus")

    const student_minus = document.getElementById("student_minus")
    const student_plus = document.getElementById("student_plus")
    const count = document.getElementById("count").dataset.capacity




    let adultCount = 0;
    let studentCount = 0;
    let childrenCount = 0;


    let adultTotal = 0;
    let studentTotal = 0;
    let childrenTotal = 0;

    let total = 0;

    let adult = 10;
    let children = 8;
    let student = 7;



    adult_minus.addEventListener('click', function (e) {
        if (adultCount > 0) {
            adultCount--;
        }
        adultTotal = adult * adultCount
    })
    student_minus.addEventListener('click', function (e) {
        if (studentCount > 0) {
            studentCount--;
        }
        studentTotal = student * studentCount
    })
    children_minus.addEventListener('click', function (e) {
        if (childrenCount > 0) {
            childrenCount--;
        }
        childrenTotal = children * childrenCount
    })

    adult_plus.addEventListener('click', function (e) {
        if (adultCount + studentCount + childrenCount < count) {
            adultCount++;
        }
        adultTotal = adult * adultCount
    })
    student_plus.addEventListener('click', function (e) {
        if (adultCount + studentCount + childrenCount < count) {
            studentCount++;
        }
        studentTotal = student * studentCount
    })
    children_plus.addEventListener('click', function (e) {
        if (adultCount + studentCount + childrenCount < count) {
            childrenCount++;
        }
        childrenTotal = children * childrenCount
    })


    function increment() {
        adult_num.value = adultCount;
        student_num.value = studentCount;
        children_num.value = childrenCount;
        total = adultTotal + studentTotal + childrenTotal
        price.innerHTML = total
        if (adultCount + studentCount + childrenCount === parseInt(count)) {
            toastElement.classList.add('show');
            setTimeout(() => {
                toastElement.classList.remove('show');
            }, 3000);
        }
    }

    function decrement() {
        adult_num.value = adultCount;
        student_num.value = studentCount;
        children_num.value = childrenCount;
        total = adultTotal + studentTotal + childrenTotal
        price.innerHTML = total
    }
} catch (e) {
    console.log(e)
}


try {
    const houseFull = document.getElementById("house");

    if (houseFull.dataset.dis === "True") {
        houseFull.disabled = true

        setInterval(() => {
            toastElement.classList.add('show');
        }, 1000);
    }


} catch (error) {
    console.log(error)
}

try {

    const btn = document.getElementsByClassName("dis")

    for (let index = 0; index < btn.length; index++) {
        console.log(typeof btn[index].dataset.dis, btn[index].dataset.dis, typeof true)
        if (btn[index].dataset.dis === "True") {
            btn[index].disabled = true
        }
    }

} catch (error) {
    console.log(error)
}