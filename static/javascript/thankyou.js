let login_display=document.querySelector(".login-display");
let signout_display=document.querySelector(".signout-display");
let reserve_display=document.querySelector(".reserve-display");
let member_display=document.querySelector(".member-display");
const url=new URL(window.location.href);
let string=url.search;
let order_number_string=string.slice(8,) //取得部份字串
const order_api="/api/order/"+order_number_string
let user_data=null;
let order_data=null;

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
            fetch(order_api).then((response)=>{
                return response.json()
            }).then((data)=>{
                order_data=data
                render(order_data)
                document.body.style.display = "block";
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

function render(data){
    let title_text=document.querySelector("#title-text");
    let order_name=document.querySelector("#order-name");
    let order_number=document.getElementById("order-number")
    let spot_photo=document.querySelector(".spot-photo");
    let date_text=document.querySelector(".date-text");
    let time_text=document.querySelector(".time-text");
    let cost_dollar=document.querySelector("#cost-dollar");
    let address_text=document.querySelector(".address-text");
    let user_name=document.querySelector("#user-name");
    let user_email=document.querySelector("#user-email");
    let user_phone=document.querySelector("#user-phone");
    title_text.textContent=data.data.trip.attraction.name;
    order_name.textContent=data.data.contact.name;
    order_number.textContent=order_number_string;
    spot_photo.src=data.data.trip.attraction.image;
    date_text.textContent=data.data.trip.date;
    cost_dollar.textContent=data.data.price;
    address_text.textContent=data.data.trip.attraction.address;
    user_name.textContent=data.data.contact.name;
    user_email.textContent=data.data.contact.email;
    user_phone.textContent=data.data.contact.phone;
    if(data.data.trip.time=="morning"){
        time_text.textContent="早上 9 點到下午 4 點";
    }else{
        time_text.textContent="下午 2 點到晚上 9 點";
    }
}