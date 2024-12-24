$('body').on('click', '.chekker', function(){
	if ($(this).is(':checked')){
		$('#vvod').attr('type', 'text');
	} else {
		$('#vvod').attr('type', 'password');
	}
});
function plane1(newTheme) {
    let p = document.getElementById("Kvass1");
    let a = document.getElementById("Palka69")
    document.getElementById("FedorTiLoh").style.visibility = "hidden";
    let enterBtn = document.getElementsByClassName("Enter")[0];
    //let registerBtn = document.getElementsByClassName("Register")[0];
    let btnList = $('.authForm').find('button');
    let inputList = $('input');
    let themeBtn = document.getElementsByTagName("button")[0];

    if (newTheme === 'white') { // светлая тема
        $('body').attr('data-theme', 'white');
        p.style.backgroundImage = 'url("static/Backround.png")';
        a.style.backgroundColor = 'rgb(190, 190, 190)';
        b.style.color = '#b9c1e9';
        Name.style.backgroundColor = "rgba(135, 177, 185, 0.4)";
        Name.style.color = "#0c2239";

        E[0].style.backgroundColor = 'rgb(223, 223, 223, 0)';
        for (const item of inputList) {
            item.style.backgroundColor = 'rgba(37,92,202,0.5)';
        }
        if ($('select').length > 0)
            $('select').css('backgroundColor', 'white');
    } else if (newTheme === 'black') { // тёмная тема
        $('body').attr('data-theme', 'black');
        MI.style.backgroundImage = 'url("static/logo 2.png")';
        p.style.backgroundImage = 'url("static/Night Backround.jpg")';
        a.style.backgroundColor = 'rgb(66, 73, 86)';
        b.style.color = '#003aae';
        E[0].style.backgroundColor = 'rgba(100, 100, 100, 0)'
        Name.style.backgroundColor = "rgba(27, 26, 58, 0.6)";
        Name.style.color = "rgb(145, 145 ,145)"
        for (const item of btnList) {
            item.style.backgroundColor = 'grey';
        }
        for (const item of inputList) {
            item.style.backgroundColor = 'darkgray';
        }
        if ($('select').length > 0)
            $('select').css('backgroundColor', 'darkgray');
    }
}

function getTheme() {
    console.log('setThemeFunction in JS')
    $.ajax({
        url: '/getTheme',
        method: 'get',
        success: function (res) {
            plane1(res.newTheme);
            return res.newTheme;
        }
    });
}

function getTheme() {
    console.log('setThemeFunction in JS')
    $.ajax({
        url: '/getTheme',
        method: 'get',
        success: function (res) {
            plane1(res.newTheme);
            return res.newTheme;
        }
    });
}
function setTheme() {
    let newTheme = $('body').attr('data-theme') === 'black' ? 'white' : 'black';
    $.ajax({
        url: '/setTheme',
        data: JSON.stringify({'newTheme': newTheme}),
        dataType: 'json',
        contentType: 'application/json;charset=UTF-8',
        method: 'post',
        success: function (res) {
            plane1(newTheme)
        }
    })
}


getTheme();

