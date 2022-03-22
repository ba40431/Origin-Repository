let member_url="/api/user";
let data=null;

function login(){
    let login_box=document.querySelector(".login");
    let register_box=document.querySelector(".register");
    let cover=document.querySelector(".cover");
    login_box.style.display="block";
    cover.style.display="block";
    register_box.style.display="none";
}
function close_login(){
  let login_box=document.querySelector(".login");
  let cover=document.querySelector(".cover");
  login_box.style.display="none";
  cover.style.display="none";
}
function register(){
  let login_box=document.querySelector(".login");
  let register_box=document.querySelector(".register");
  let cover=document.querySelector(".cover");
  login_box.style.display="none";
  register_box.style.display="block";
  cover.style.display="block";
}
function close_register(){
  let login_box=document.querySelector(".login");
  let register_box=document.querySelector(".register");
  let cover=document.querySelector(".cover");
  login_box.style.display="none";
  register_box.style.display="none";
  cover.style.display="none";
}
  
function check_login(){
  let login_email=document.getElementById("login-email").value;
  let login_password=document.getElementById("login-password").value;
  let headers={"Content-Type": "application/json",}
  let body={
    "email": login_email,
    "password":login_password
  }
  fetch(member_url,{
    method: "PATCH",
    headers: headers,
    body: JSON.stringify(body)
  }).then(function(response){
    return response.json();
  }).then(function(result){
    data=result
    if(data.error==true){
      let login_failed=document.getElementById("login-failed");
      let login_content=document.querySelector(".login-content");
      login_content.style.height="285px";
      login_failed.textContent=data.message;
    }else{
      window.location.replace(location.href) //不可以通過「後退」退回到原頁面
    }
  })
}
function check_register(){
  let register_name=document.getElementById("register-name").value;
  let register_email=document.getElementById("register-email").value;
  let register_password=document.getElementById("register-password").value;
  let headers={
    "Content-Type": "application/json",
    "Accept": "application/json"
  }
  let body={
    "name":register_name,
    "email": register_email,
    "password":register_password
  }
  fetch(member_url,{
    method: "POST",
    headers: headers,
    body: JSON.stringify(body)
  }).then(function(response){
    return response.json();
  }).then(function(result){
    data=result
    let register_failed=document.getElementById("register-failed");
    let register_content=document.querySelector(".register-content");
    if(data.error==true){
      register_content.style.height="340px";
      register_failed.textContent=data.message
    }else{
      register_content.style.height="340px";
      register_failed.textContent="註冊成功"
    }
  })
}

function signout(){
  let headers={
    "Content-Type": "application/json",
    "Accept": "application/json"
  }
  fetch(member_url,{
    method: "DELETE",
    headers: headers,
  }).then(function(response){
    return response.json();
  }).then(function(result){
    data=result
    window.location.replace(location.href) 
  })
}