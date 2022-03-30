const reserve_api="/api/booking";
const reserve_url="/booking";
let user_url="/api/user";
let login_display=document.querySelector(".login-display");
let signout_display=document.querySelector(".signout-display");
let reserve_display=document.querySelector(".reserve-display");


init()

function init(){
    get_login(user_url).then(function(data){
        if(data.data){
          login_display.style.display="none";
          signout_display.style.display="block";
          reserve_display.style.display="block";
          let user_name=document.getElementById("user-name");
          user_name.textContent=data.data.name
          fetch_booking(reserve_api).then(function(data){
            if(data.data){
                render(data)
            }else if(data.data==null){
                hidding_info()
            }else{
                hidding_info()
            }
        })
        }else if(data.data==null){
            document.body.innerHTML="";
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
function render(data){
    let spot_photo=document.querySelector(".spot-photo");
    let title_text=document.getElementById("title-text");
    let date_text=document.querySelector(".date-text");
    let time_text=document.querySelector(".time-text");
    let cost_dollar=document.getElementById("cost-dollar");
    let address_text=document.querySelector(".address-text");
    let pay_dollar=document.getElementById("pay-dollar");
    spot_photo.src=data.data.attraction.image;
    title_text.textContent=data.data.attraction.name;
    date_text.textContent=data.data.date;
    cost_dollar.textContent=data.data.price;
    address_text.textContent=data.data.attraction.address;
    pay_dollar.textContent=data.data.price;
    if(data.data.time=="morning"){
        time_text.textContent="早上 9 點到下午 4 點";
    }else{
        time_text.textContent="下午 2 點到下午 9 點";
    }
}
function fetch_booking(url){
    return fetch(url)
    .then(function(response){
      return response.json()
    });
}
function delete_booking(){
    fetch(reserve_api,{
        method: "DELETE",
      }).then(function(response){
        return response.json();
      }).then(function(result){
        data=result
        document.body.innerHTML="";
        window.location.replace(location.href)
      })
}
function hidding_info(){
    let reserve_false=document.querySelector(".reserve-false");
    let reserve_container=document.querySelector(".reserve-container");
    let footer=document.querySelector(".footer");
    let user_wrapper=document.querySelector(".user-wrapper");
    let footer_text=document.querySelector(".footer-text");
    reserve_false.style.display="block";
    reserve_container.style.display="none";
    user_wrapper.style.display="none";
    footer.style.position="fixed";
    footer.style.marginTop="40px";
    footer.style.width="100%";
    footer.style.height="100%" //將剩餘頁面畫面填滿
    footer.style.alignItems="flex-start";
    footer_text.style.marginTop="45px";
}