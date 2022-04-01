const member_url="/api/user";
const booking_url="/booking";
let data=null;
let login_box=document.querySelector(".login");
let register_box=document.querySelector(".register");
let cover=document.querySelector(".cover");
let login_email=document.getElementById("login-email");
let login_password=document.getElementById("login-password");
let register_name=document.getElementById("register-name");
let register_email=document.getElementById("register-email");
let register_password=document.getElementById("register-password");
login_email.addEventListener("input",email_input)
login_password.addEventListener("input",password_input)
register_name.addEventListener("input",input)
register_email.addEventListener("input",email_input)
register_password.addEventListener("input",password_input)

function login(){
	login_box.style.display="block";
	cover.style.display="block";
	register_box.style.display="none";
}
function close_login(){
	login_box.style.display="none";
	cover.style.display="none";
}
function register(){
	login_box.style.display="none";
	register_box.style.display="block";
	cover.style.display="block";
}
function close_register(){
	login_box.style.display="none";
	register_box.style.display="none";
	cover.style.display="none";
}
  
function check_login(){
	let login_email=document.getElementById("login-email");
	let login_password=document.getElementById("login-password");
	let login_failed=document.getElementById("login-failed");
	let login_content=document.querySelector(".login-content");
	if(login_email.value && login_password.value){
		let headers={"Content-Type": "application/json"}
		let body={
			"email": login_email.value,
			"password":login_password.value
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
				login_content.style.height="285px";
				login_failed.textContent=data.message;
			}else{
				window.location.replace(location.href) //不可以通過「後退」退回到原頁面
			}
		})
	}else{
		login_content.style.height="285px";
		login_failed.textContent="請輸入電子信箱和密碼";
	}
}
function check_register(){
	let register_failed=document.getElementById("register-failed");
	let register_content=document.querySelector(".register-content");
	if(register_email.value.match(/^([\w\.\-]){1,64}\@([\w\.\-]){1,64}$/) && register_password.value.match(/^[0-9a-zA-Z_]+$/)){
		let headers={
			"Content-Type": "application/json",
			"Accept": "application/json"
		}
		let body={
			"name":register_name.value,
			"email": register_email.value,
			"password":register_password.value
		}
		fetch(member_url,{
			method: "POST",
			headers: headers,
			body: JSON.stringify(body)
		}).then(function(response){
			return response.json();
		}).then(function(result){
			data=result
		if(data.error==true){
			register_content.style.height="340px";
			register_failed.textContent=data.message
		}else{
			register_content.style.height="340px";
			register_failed.textContent="註冊成功"
		}
		})
	}else if(register_name.value=="" || register_email.value=="" || register_password.value==""){
		register_failed.textContent="請輸入姓名、電子郵件和密碼";
		register_content.style.height="340px";
	}else if(!register_email.value.match(/^([\w\.\-]){1,64}\@([\w\.\-]){1,64}$/)){
		register_failed.textContent="電子信箱格式須包含「@」";
		register_content.style.height="340px";
	}else{
		register_failed.textContent="請勿在密碼輸入特殊符號";
		register_content.style.height="340px";
	}
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

function reserve(){
  get_login(member_url).then(function(data){
      if(data.data){
        login_display.style.display="none";
        signout_display.style.display="block";
        reserve_display.style.display="block";
        location.href=booking_url;
      }
      else if(data.data==null){
        login_display.style.display="block";
        signout_display.style.display="none";
        reserve_display.style.display="block";
        login()
      }
  })
}

function email_input (e) {
	if(e.target.value.match(/^([\w\.\-]){1,64}\@([\w\.\-]){1,64}$/)){
		e.target.classList.remove("invalid");
		e.target.classList.add("valid");
	}else{
		e.target.classList.add("invalid");
	}
}
function password_input (e) {
	if(e.target.value.match(/^[0-9a-zA-Z_]+$/)){
		e.target.classList.remove("invalid");
		e.target.classList.add("valid");
	}else{
		e.target.classList.add("invalid");
	}
}
function input (e) {
	if(e.target.value){
		e.target.classList.add("valid");
	}else{
		e.target.classList.add("invalid");
	}
}