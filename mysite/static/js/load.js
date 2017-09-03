function Close_load(){
    var shield = document.getElementById("shield");
    var alertFram = document.getElementById("alertFram");
    document.body.removeChild(shield);
    document.body.removeChild(alertFram);
    document.body.onselectstart = function(){return true};
    document.body.oncontextmenu = function(){return true};
}

function Show_load(message){
    var shield = document.createElement("DIV");
    shield.id = "shield";
    shield.style.position = "absolute";
    shield.style.left = "0px";
    shield.style.top = "0px";
    shield.style.width = "100%";
    shield.style.height = ((document.documentElement.clientHeight>document.documentElement.scrollHeight)?document.documentElement.clientHeight:document.documentElement.scrollHeight)+"px";
    shield.style.background = "#333";
    shield.style.textAlign = "center";
    shield.style.zIndex = "10000";
    shield.style.filter = "alpha(opacity=0)";
    shield.style.opacity = 0;

    var alertFram = document.createElement("DIV");
    var height="50px";
    alertFram.id="alertFram";
    alertFram.style.position = "absolute";
    alertFram.style.width = "0px";
    alertFram.style.height = "0px";
    alertFram.style.left = "65%";
    alertFram.style.top = "24%";

    alertFram.style.background = "#fff";
    alertFram.style.textAlign = "center";
    alertFram.style.lineHeight = height;
    alertFram.style.zIndex = "10001";

    strHtml =""
    alertFram.innerHTML=strHtml;
    document.body.appendChild(alertFram);
    document.body.appendChild(shield);

    this.setOpacity = function(obj,opacity){
        if(opacity>=1)opacity=opacity/100;
        try{ obj.style.opacity=opacity; }catch(e){}
        try{ 
            if(obj.filters.length>0&&obj.filters("alpha")){
            obj.filters("alpha").opacity=opacity*100;
            }else{
            obj.style.filter="alpha(opacity=\""+(opacity*100)+"\")";
            }
        }
        catch(e){}
    }

    var c = 0;
    this.doAlpha = function(){
    if (++c > 20){clearInterval(ad);return 0;}
    setOpacity(shield,c);
    }
    var ad = setInterval("doAlpha()",1);

    document.body.onselectstart = function(){return false;}
    document.body.oncontextmenu = function(){return false;}
}