try {


    document.addEventListener('DOMContentLoaded', function () {
        const stripe = Stripe("pk_test_51N3kLqGBA8tceJAWA4aSuLMEp58epmp8tw2Pl7iFbKLxPyLtQKdcYj1DnjZbDtY6T0vfcjflBxk0YrCCuuI0h7Yz009NbbKnEh");
        const value = document.getElementsByClassName("data")[0].dataset.value

        return stripe.redirectToCheckout({ sessionId: value})

    })

} catch (e) {
    console.log("ff")
}

