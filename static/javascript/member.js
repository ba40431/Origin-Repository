let login_display=document.querySelector(".login-display");
let signout_display=document.querySelector(".signout-display");
let reserve_display=document.querySelector(".reserve-display");
let member_display=document.querySelector(".member-display");
let name_text=document.querySelector("#name-text");
let email_text=document.querySelector("#email-text");
let member_photo=document.querySelector("#member-photo");
let member_password=document.querySelector(".member-password");
let new_password=document.querySelector("#member-password");
let password_button=document.querySelector(".password-button");
let member_false=document.querySelector(".member-false");
let user_data=null;
let orders_data=null;
let update_data=null;
let order_items=document.querySelector(".order-items");
const member_api="/api/member"
init()

function init(){
    document.body.style.display = "none";
    get_login(user_api).then(function(data){
        user_data=data;
        if(user_data.data){
            login_display.style.display="none";
            signout_display.style.display="block";
            reserve_display.style.display="block";
            member_display.style.display="block";
            member_photo.textContent=user_data.data.name[0].toUpperCase();  //英文轉大寫
            name_text.textContent=user_data.data.name;
            email_text.textContent=user_data.data.email;
            fetch(member_api).then((response)=>{
                return response.json()
            }).then((data)=>{
                orders_data=data
                if(orders_data.data==null){
                    let order_false=document.querySelector(".order-false");
                    order_false.style.display="block";
                    document.body.style.display = "block";
                }else{
                    for(let i=0; i<orders_data.data.length; i++){
                        render(i,orders_data)
                        document.body.style.display = "block";
                    }
                }
            })
        }else if(user_data.data==null){
            location.href="/"
            login_display.style.display="block";
            signout_display.style.display="none";
            reserve_display.style.display="block";
            member_display.style.display="none";
            document.body.style.display = "block";
        }
    })
}

function get_login(url){
	return fetch(url)
	.then(function(response){
	return response.json()
	});
}

function render(i,data){
    let a=document.createElement("a");
    let number_div=document.createElement("div");
    let date_div=document.createElement("div");
    let attractioname_div=document.createElement("div");
    let hr=document.createElement("hr");
    let attraction_name=data.data[i].attractionName;
    let number=data.data[i].number;
    let date=data.data[i].date;
    order_items.appendChild(a);
    a.setAttribute("class","order-item");
    a.setAttribute("id","order-item"+i);
    a.href="/thankyou?number="+number;
    let order_box=document.getElementById("order-item"+i);
    number_div.textContent=number;
    attractioname_div.textContent=attraction_name;
    date_div.textContent=date;
    order_box.appendChild(number_div);
    order_box.appendChild(attractioname_div);
    order_box.appendChild(date_div);
    order_items.appendChild(hr);
}
function update_password(){
    if(password_button.textContent=="修改密碼"){
        member_password.style.display="block";
        password_button.textContent="確定更改";
    }else if(new_password.value==""){
        member_false.textContent="請輸入密碼"
    }else if(!new_password.value.match(/^[0-9a-zA-Z_]+$/)){
        member_false.textContent="請勿輸入特殊符號"
    }else{
        member_false.textContent=""
		let headers={"Content-Type": "application/json"}
		let body={
			"email":user_data.data.email,
			"password":new_password.value
		}
        fetch(member_api,{
			method: "PATCH",
			headers: headers,
			body: JSON.stringify(body)
		}).then((response)=>{
            return response.json()
        }).then((data)=>{
            update_data=data
            if(update_data.ok){
                password_button.textContent="修改密碼";
                member_password.style.display="none";
                // window.location.replace(location.href) 
            }else{
                member_false.textContent=update_data.message
            }
        })
    }

}