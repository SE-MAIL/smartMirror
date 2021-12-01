$(document).ready(function(){
    $.ajax({
        url: 'http://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=b1728d069e54127789c1cc83a3b05ef9&units=metric',
        dataType: 'json',
        type: 'GET',
        success: function(data){
            var $Icon = (data.weather[0].icon);
            var $Temp = Math.floor(data.main.temp) + 'º';
            var $city = data.name;

             $('.CurrIcon').append('http://openweathermap.org/img/wn/'+ $Icon + '@2x.png');
             $('.CurrTemp').prepend($Temp);
             $('.City').append($city);
        }
    })
});