TPDirect.setupSDK(123873, 'app_XAHYCabbRgwfTjFeevHjkiGtHbGcKyavCgVFj2B33yC9KYd0msTsLz4HnVL6', 'sandbox')
let fields = {
    number: {
        // css selector
        element:".credit-number",
        placeholder:"**** **** **** ****"
    },
    expirationDate: {
        // DOM object
        element:".credit-date",
        placeholder:"MM / YY"
    },
    ccv: {
        element:".credit-password",
        placeholder:"CCV"
    }
}
TPDirect.card.setup({
    fields: fields,
    styles: {
        // Style all elements
        "input": {
            "color":"#666666"
        },
        // Styling ccv field
        "input.ccv": {
            "font-size":"16px"
        },
        // Styling expiration-date field
        'input.expiration-date': {
            "font-size":"16px"
        },
        // Styling card-number field
        'input.card-number': {
            "font-size":"16px"
        },
        // style focus state
        ':focus': {
            // 'color': 'black'
        },
        // style valid state
        '.valid': {
            'color': '#448899'
        },
        // style invalid state
        '.invalid': {
            'color': 'red'
        },
    }
})
TPDirect.card.onUpdate(function (update) {
    // update.canGetPrime === true
    // --> you can call TPDirect.card.getPrime()
    if (update.canGetPrime) {
        // Enable submit Button to get prime.
        // submitButton.removeAttribute('disabled')
    } else {
        // Disable submit Button to get prime.
        // submitButton.setAttribute('disabled', true)
    }
                                            
    // cardTypes = ['mastercard', 'visa', 'jcb', 'amex', 'unknown']
    if (update.cardType === 'visa') {
        // Handle card type visa.
    }

    // number 欄位是錯誤的
    if (update.status.number === 2) {
        // setNumberFormGroupToError()
    } else if (update.status.number === 0) {
        // setNumberFormGroupToSuccess()
    } else {
        // setNumberFormGroupToNormal()
    }
    
    if (update.status.expiry === 2) {
        // setNumberFormGroupToError()
    } else if (update.status.expiry === 0) {
        // setNumberFormGroupToSuccess()
    } else {
        // setNumberFormGroupToNormal()
    }
    
    if (update.status.ccv === 2) {
        // setNumberFormGroupToError()
    } else if (update.status.ccv === 0) {
        // setNumberFormGroupToSuccess()
    } else {
        // setNumberFormGroupToNormal()
    }
})
function orders(event) {
    // event.preventDefault()

    // 取得 TapPay Fields 的 status
    const tappayStatus = TPDirect.card.getTappayFieldsStatus()

    // 確認是否可以 getPrime
    if (tappayStatus.canGetPrime === false) {
        alert('can not get prime')
        return
    }

    // Get prime
    TPDirect.card.getPrime((result) => {
        if (result.status !== 0) {
            alert('get prime error ' + result.msg)
            return
        }
        alert('get prime 成功，prime: ' + result.card.prime)

        // send prime to your server, to pay with Pay by Prime API .
        // Pay By Prime Docs: https://docs.tappaysdk.com/tutorial/zh/back.html#pay-by-prime-api
    })
}