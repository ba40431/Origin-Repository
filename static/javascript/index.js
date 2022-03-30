let page=0;
let page_url="/api/attractions?page=";
let scrolling=true;
let user_url="/api/user";
let login_display=document.querySelector(".login-display");
let signout_display=document.querySelector(".signout-display");
let reserve_display=document.querySelector(".reserve-display");
let search=document.getElementById("search");
search.addEventListener("click",click);

init()

function init(){
	get_login(user_url).then(function(data){
	if(data.data){
		login_display.style.display="none";
		signout_display.style.display="block";
		reserve_display.style.display="block";
	}
	else if(data.data==null){
		login_display.style.display="block";
		signout_display.style.display="none";
		reserve_display.style.display="block";
	}
	})
	get_data(page_url,page).then(function(data){
	for(let i=0; i<data.data.length; i++){
		render_spots(i,page,data)
	};
	let next_page=data.nextPage;
	page=next_page;
	window.addEventListener("scroll",scroll);
	});
}
function get_data(url,page){
	return fetch(url+page)
	.then(function(response){
	return response.json()
	});
};
function get_keyword_data(url,keyword){
	return fetch(url+keyword)
	.then(function(response){
	return response.json()
	});
};
function get_login(url){
	return fetch(url)
	.then(function(response){
	return response.json()
	});
}
function render_spots(i,page,data){
    let box_name=i+page*12;
    let name=data.data[i].name;
    let src=data.data[i].images[0];
    let mrt=data.data[i].mrt;
    let category=data.data[i].category;
    let id=data.data[i].id;
    let img=document.createElement("img");
    let a=document.createElement("a");
    let container=document.getElementById("container"); 
    container.appendChild(a);
    a.setAttribute("class","spot-box");
    a.setAttribute("id","spot-box-"+box_name);
    a.href="/attraction/"+id;
    let spot_box=document.getElementById("spot-box-"+box_name);
    let div_name=document.createElement("div"); 
    let div_info=document.createElement("div"); 
    img.src=src;
    div_name.textContent=name;
    spot_box.appendChild(img);
    spot_box.appendChild(div_name);
    spot_box.appendChild(div_info);
    img.setAttribute("class","spot-img");
    div_name.setAttribute("class","spot-name");
    div_info.setAttribute("class","spot-info");
    div_info.setAttribute("id","spot-info"+box_name);
    let spot_info=document.getElementById("spot-info"+box_name); 
    let div_mrt=document.createElement("div");
    let div_category=document.createElement("div");
    div_mrt.textContent=mrt;
    div_category.textContent=category;
    spot_info.appendChild(div_mrt);
    spot_info.appendChild(div_category);
    div_mrt.setAttribute("class","spot-mrt");
    div_category.setAttribute("class","spot-category"); 
};
function render_keyword_spots(i,keyword_page,data){
    let box_name=i+keyword_page*12;
    let name=data.data[i].name;
    let src=data.data[i].images[0];
    let mrt=data.data[i].mrt;
    let category=data.data[i].category;
    let id=data.data[i].id;
    let img=document.createElement("img");
    let a=document.createElement("a");
    let container=document.getElementById("container-keyword"); 
    container.appendChild(a);
    a.setAttribute("class","keyword-spot-box");
    a.setAttribute("id","keyword-spot-box-"+box_name);
    a.href="/attraction/"+id;
    let spot_box=document.getElementById("keyword-spot-box-"+box_name);
    let div_name=document.createElement("div"); 
    let div_info=document.createElement("div");
    img.src=src;
    div_name.textContent=name;
    spot_box.appendChild(img);
    spot_box.appendChild(div_name);
    spot_box.appendChild(div_info);
    img.setAttribute("class","spot-img");
    div_name.setAttribute("class","spot-name");
    div_info.setAttribute("class","spot-info");
    div_info.setAttribute("id","keyword-spot-info"+box_name);
    let spot_info=document.getElementById("keyword-spot-info"+box_name); 
    let div_mrt=document.createElement("div");
    let div_category=document.createElement("div");
    div_mrt.textContent=mrt;
    div_category.textContent=category;
    spot_info.appendChild(div_mrt);
    spot_info.appendChild(div_category);
    div_mrt.setAttribute("class","spot-mrt");
    div_category.setAttribute("class","spot-category"); 
};
function scroll(){
	let scrollable=document.documentElement.scrollHeight-window.innerHeight;
	let scrolled=window.scrollY;
	if(Math.ceil(scrolled)>=scrollable-5){
	if(scrolling){
		scrolling=false;
		if(page){
			let timeout=window.setTimeout(get_data(page_url,page).then(function(data){
				for(let i=0; i<data.data.length; i++){
				render_spots(i,page,data)
				}
				next_page=data.nextPage;
				page=next_page;
			}),3000);
			window.clearTimeout(timeout);
		};
	};
	}else{
		scrolling=true;
	};
}
function click(){
	let keyword_page=0;
	let keyword=document.getElementById("keyword").value;
	let scrolling=true;
	let keyword_url="/api/attractions?page="+keyword_page+"&keyword=";
	get_keyword_data(keyword_url,keyword).then(function(data){
	if(data.data.length>0){
		document.getElementById("container").style.display="none";
		let element=document.getElementById("container-keyword"); 
		if(document.querySelector(".keyword-spot-box")){
			while (element.firstChild){
				element.removeChild(element.firstChild);
			};
			for(let i=0; i<data.data.length; i++){
			render_keyword_spots(i,keyword_page,data)
			};
			let keyword_next_page=data.nextPage;
			keyword_page=keyword_next_page;
			window.addEventListener("scroll",()=>{
				scroll_keyword(data)
			});
		}
		else if(document.querySelector(".keyword-spot-box")==null){
			element.textContent="";
			// let scrolling=true;
			for(let i=0; i<data.data.length; i++){
				render_keyword_spots(i,keyword_page,data);
			}
			let keyword_next_page=data.nextPage;
			keyword_page=keyword_next_page;
			window.addEventListener("scroll",()=>{
				scroll_keyword()
			});
		};
    }
	else if(data.data.length==0){
		document.getElementById("container").style.display="none";
		let element=document.getElementById("container-keyword"); 
		if(document.querySelector(".keyword-spot-box")){
			while (element.firstChild){
				element.removeChild(element.firstChild);
			};
			element.textContent="查無與【"+keyword+"】的相關景點";
			}
		else{
			element.textContent="查無與【"+keyword+"】的相關景點";
		};
	};
	});
	function scroll_keyword(){
	let scrollable=document.documentElement.scrollHeight-window.innerHeight
	let scrolled=window.scrollY;
	if(Math.ceil(scrolled)>=scrollable-3 & scrolling){
		scrolling=false;
		if(keyword_page){
			keyword_url="/api/attractions?page="+keyword_page+"&keyword=";
			let timeout=window.setTimeout(get_keyword_data(keyword_url,keyword).then(function(data){
				for(let i=0; i<data.data.length; i++){
				render_keyword_spots(i,keyword_page,data)
				};
				keyword_next_page=data.nextPage;
				keyword_page=keyword_next_page;
			}),3000);
			window.clearTimeout(timeout);
		};
	};
	}
}