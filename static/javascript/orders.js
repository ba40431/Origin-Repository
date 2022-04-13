TPDirect.setupSDK(123873, 'app_XAHYCabbRgwfTjFeevHjkiGtHbGcKyavCgVFj2B33yC9KYd0msTsLz4HnVL6', 'sandbox')
let user_phone=document.getElementById("user-phone");
let pay_false=document.getElementById("pay-false");
let checkbox=document.getElementById("checkbox");
user_phone.addEventListener("input",input)


set_card()

function input (e) {
	if(e.target.value.match(/^09[0-9]{8}$/)){
		e.target.classList.remove("invalid");
		e.target.classList.add("valid");
        checkbox.style.display="block";
	}else{
		e.target.classList.add("invalid");
        checkbox.style.display="none";
	}
}

function set_card(){
    let fields = {
        number: {
            // css selector
            element:"#credit-number",
            placeholder:"**** **** **** ****"
        },
        expirationDate: {
            // DOM object
            element:"#credit-date",
            placeholder:"MM / YY"
        },
        ccv: {
            element:"#credit-password",
            placeholder:"CCV"
        }
    };
    TPDirect.card.setup({
        fields: fields,
        styles: {
            "input": {
                "color":"#666666"
            },
            "input.ccv": {
                "font-size":"16px"
            },
            "input.expiration-date": {
                "font-size":"16px"
            },
            "input.card-number": {
                "font-size":"16px"
            },
            ":focus": {
                "color": "black"
            },
            ".valid": {
                "color": "#448899"
            },
            ".invalid": {
                "color": "#E64217"
            },
        }
    });
};
function orders(){
    console.log(user_data)
    console.log(booking_data)
    // 取得 TapPay Fields 的 status
    const tappayStatus = TPDirect.card.getTappayFieldsStatus()
    // 確認是否可以 getPrime
    if(user_phone.value==""){
        pay_false.textContent="請填寫手機號碼"
    }else if(! user_phone.value.match(/^09[0-9]{8}$/)){
        pay_false.textContent="請填寫正確的手機號碼格式"
    }else{
        if(tappayStatus.canGetPrime === false){
            pay_false.textContent="請填寫正確的付款資訊"
        }else{
            // Get prime
            TPDirect.card.getPrime((result) => {
                if(result.status !== 0){
                    pay_false.textContent="付款發生錯誤"
                }else{
                    let headers={
                        "Content-Type": "application/json",
                        "Accept": "application/json"
                    }
                    let body={
                        "prime":result.card.prime,
                        "order": {
                            "price":booking_data.data.price,
                            "trip": {
                            "attraction": {
                                "id":booking_data.data.attraction.id,
                                "name":booking_data.data.attraction.name,
                                "address":booking_data.data.attraction.address,
                                "image":booking_data.data.attraction.image
                            },
                            "date":booking_data.data.date,
                            "time":booking_data.data.time
                            },
                            "contact": {
                                "name":user_data.data.name,
                                "email":user_data.data.email,
                                "phone":user_phone.value
                            }
                        }
                    }
                    fetch(order_api,{
                        method:"POST",
                        headers:headers,
                        body:JSON.stringify(body)
                    }).then(function(response){
                        return response.json()
                    }).then(function(data){
                        result=data;
                        if(result.data.payment.status==1){
                            location.href=thankyou_url+"?number="+result.data.number;
                        }else{
                            pay_false.textContent="付款發生錯誤，請再確認付款資訊"
                        }
                        
                    })
                }
            })
        }
    };
}