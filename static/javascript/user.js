// let member_url="/api/user"

function login(){
    let login_box=document.querySelector(".login");
    let register_box=document.querySelector(".register");
    let cover=document.querySelector(".cover");
    login_box.style.display="block";
    cover.style.display="block";
    register_box.style.display="none";
    let login_email=document.getElementById("login-email").value;
    let login_password=document.getElementById("login-password").value;
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
    let register_name=document.getElementById("register-name").value;
    let register_email=document.getElementById("register-email").value;
    let register_password=document.getElementById("register-password").value;
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
    // login_email="";
    // login_password="";
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
    }).then(function(data){
      result=data
    })
  }
  
  function check_register(){
    let register_name=document.getElementById("register-name").value;
    let register_email=document.getElementById("register-email").value;
    let register_password=document.getElementById("register-password").value;
    // register_name="";
    // register_email="";
    // register_password="";
    let headers={"Content-Type": "application/json",}
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
    }).then(function(data){
      result=data
    })
  }
  
  function get_register(){
  
  }