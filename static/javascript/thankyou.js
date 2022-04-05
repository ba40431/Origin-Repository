let login_display=document.querySelector(".login-display");
let signout_display=document.querySelector(".signout-display");
let reserve_display=document.querySelector(".reserve-display");
const url=new URL(window.location.href)
let string=url.search;
let order_number_string=string.slice(8,) //取得部份字串
let order_number=document.getElementById("order-number")

init()

function init(){
    get_login(user_api).then(function(data){
        if(data.data){
            login_display.style.display="none";
            signout_display.style.display="block";
            reserve_display.style.display="block";
            order_number.textContent=order_number_string
        }else if(data.data==null){
            location.href="/"
            login_display.style.display="block";
            signout_display.style.display="none";
            reserve_display.style.display="block";
        }
    })
}

function get_login(url){
	return fetch(url)
	.then(function(response){
	return response.json()
	});
}