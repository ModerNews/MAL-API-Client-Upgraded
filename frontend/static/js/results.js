// JavaScript Document

var animes = [
    {
        "id": 1575,
        "title": "Code Geass: Hangyaku no Lelouch",
        "main_picture": {
            "medium": "https://api-cdn.myanimelist.net/images/anime/5/50331.jpg",
            "large": "https://api-cdn.myanimelist.net/images/anime/5/50331l.jpg"
        }
    },
    {
        "id": 19815,
        "title": "No Game No Life",
        "main_picture": {
            "medium": "https://api-cdn.myanimelist.net/images/anime/1074/111944.jpg",
            "large": "https://api-cdn.myanimelist.net/images/anime/1074/111944l.jpg"
        }
    },
    {
        "id": 29803,
        "title": "Overlord",
        "main_picture": {
            "medium": "https://api-cdn.myanimelist.net/images/anime/7/88019.jpg",
            "large": "https://api-cdn.myanimelist.net/images/anime/7/88019l.jpg"
        }
    },
    {
        "id": 30276,
        "title": "One Punch Man",
        "main_picture": {
            "medium": "https://api-cdn.myanimelist.net/images/anime/12/76049.jpg",
            "large": "https://api-cdn.myanimelist.net/images/anime/12/76049l.jpg"
        }
    },
    {
        "id": 34134,
        "title": "One Punch Man 2nd Season",
        "main_picture": {
            "medium": "https://api-cdn.myanimelist.net/images/anime/1247/122044.jpg",
            "large": "https://api-cdn.myanimelist.net/images/anime/1247/122044l.jpg"
        }
    },
    {
        "id": 37430,
        "title": "Tensei shitara Slime Datta Ken",
        "main_picture": {
            "medium": "https://api-cdn.myanimelist.net/images/anime/1694/93337.jpg",
            "large": "https://api-cdn.myanimelist.net/images/anime/1694/93337l.jpg"
        }
    },
    {
        "id": 38000,
        "title": "Kimetsu no Yaiba",
        "main_picture": {
            "medium": "https://api-cdn.myanimelist.net/images/anime/1286/99889.jpg",
            "large": "https://api-cdn.myanimelist.net/images/anime/1286/99889l.jpg"
        }
    },
    {
        "id": 38691,
        "title": "Dr. Stone",
        "main_picture": {
            "medium": "https://api-cdn.myanimelist.net/images/anime/1613/102576.jpg",
            "large": "https://api-cdn.myanimelist.net/images/anime/1613/102576l.jpg"
        }
    },
    {
        "id": 40748,
        "title": "Jujutsu Kaisen",
        "main_picture": {
            "medium": "https://api-cdn.myanimelist.net/images/anime/1171/109222.jpg",
            "large": "https://api-cdn.myanimelist.net/images/anime/1171/109222l.jpg"
        }
    },
    {
        "id": 41487,
        "title": "Tensei shitara Slime Datta Ken 2nd Season Part 2",
        "main_picture": {
            "medium": "https://api-cdn.myanimelist.net/images/anime/1033/118296.jpg",
            "large": "https://api-cdn.myanimelist.net/images/anime/1033/118296l.jpg"
        }
    }
];

var topPreset = '<figure><a href="<LINK>"><img class="img-fluid" src="<IMGSOURCE>" width="300" height="400" alt="<CAPTION>"></a><figcaption><CAPTION></figcaption></figure>';

var mainPreset = '<figure><a href="<LINK>"><img class="ml-3" src="<IMGSOURCE>" width="200" height="300" alt="<CAPTION>" /></a><figcaption><CAPTION></figcaption></figure>';

function Name(str){
	if (str.length>25){
		return str.substring(0,25)+"...";
	}
	else{
		return str;
	}
}

for(var x = 0; x < animes.length; x++){
	var json = animes[x];
	var id = json.id;
	var title = Name(json.title);
	var imgsource = json.main_picture.large;
	if (x == 0) {
		var element = document.getElementById("top-recommendation");
		element.innerHTML = topPreset
			.replace("<LINK>",`https://myanimelist.net/anime/${id}`)
			.replace("<IMGSOURCE>",imgsource)
			.replace("<CAPTION>",json.title)
			.replace("<CAPTION>",json.title);
	}
	else {
		var element = document.getElementById("recommendations");
		element.innerHTML = element.innerHTML + mainPreset
			.replace("<LINK>",`https://myanimelist.net/anime/${id}`)
			.replace("<IMGSOURCE>",imgsource)
			.replace("<CAPTION>",title)
			.replace("<CAPTION>",title);
	}
}
