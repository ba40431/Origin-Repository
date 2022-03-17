const url = new URL(window.location.href)
let string=url.pathname;
let spot_id=string.replace("/attraction/",""); //刪除字串中的特定字串
let open_url="/api/attraction/"+spot_id;

get_data(open_url).then(function(data){
  render(data);
  let images=data.data.images;
  for(i=0;i<images.length;i++){
    render_images(data)
  };
  render_button(data);
});

let select_time= document.querySelectorAll('input[type=radio][name="select-time"]');
select_time.forEach(radio => radio.addEventListener('change', () =>{
  let dollar=document.getElementById("dollar");
  dollar.textContent=radio.value
}));

function get_data(url){
  return fetch(url)
  .then(function(response){
    return response.json()
  });
}
function render(data){
  let name=data.data.name;
  let mrt=data.data.mrt;
  let category=data.data.category;
  let description=data.data.description;
  let address=data.data.address;
  let transport=data.data.transport;
  let spot_name=document.querySelector(".spot-name");
  // let spot_mrt=document.querySelector(".spot-mrt");
  let spot_category=document.querySelector(".spot-category");
  let spot_description=document.querySelector(".spot-description");
  let spot_address=document.querySelector(".spot-address-text");
  let spot_transport=document.querySelector(".spot-transport-text");
  spot_name.textContent=name;
  spot_category.textContent=category+" at "+mrt;
  spot_description.textContent=description;
  spot_address.textContent=address;
  spot_transport.textContent=transport;
}

function render_images(data){
  let images=data.data.images;
  let slider_main=document.getElementById("slider-main");
  let div=document.createElement("div"); 
  let img=document.createElement("img");
  slider_main.appendChild(div);
  div.setAttribute("class","item");
  div.setAttribute("id","item-"+i);
  let item=document.getElementById("item-"+i);
  img.src=images[i];
  item.appendChild(img);
}


function render_button(data){
  let slider=document.getElementById("slider");
  let slider_main=document.getElementById("slider-main");
  let allboxs=slider_main.children;
  let next=document.getElementById("next");
  let prev=document.getElementById("prev");
  let slider_button=document.getElementById("slider-button");
  let now=0;
  for(let i=0;i<allboxs.length;i++){
      let label=document.createElement("label");
      if(i===0){
          label.className="slider-button-icon current";
      }else{
        label.className="slider-button-icon";
      }
      slider_button.appendChild(label)
  };
  let scroll_w=parseInt(window.getComputedStyle(slider,null).getPropertyValue("width"));/*轉換成數值*/
  for(let j=1;j<allboxs.length;j++){
      allboxs[j].style.left=scroll_w+"px";
  }
  next.onclick=function(){
      allboxs[now].style.left=-scroll_w+"px";
      now=now+1;
      if(now>=allboxs.length){
          now=0;
      }
      allboxs[now].style.left=scroll_w+"px";
      allboxs[now].style.left=0;
      change_button();
  }
  prev.onclick=function(){
      allboxs[now].style.left=scroll_w+"px";
      now=now-1;
      if(now<0){
          now=allboxs.length-1;
      }
      allboxs[now].style.left=-scroll_w+"px";
      allboxs[now].style.left=0;
      change_button();
  }
  function change_button(){
      for(let i=0;i<slider_button.children.length;i++){
        slider_button.children[i].className="slider-button-icon";
      }
      slider_button.children[now].className="slider-button-icon current";

  }
}