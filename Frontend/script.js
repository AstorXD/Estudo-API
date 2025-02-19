let country
let city

let apidata

const forms = document.getElementById("forms");
const container = document.getElementById("maincontainer");
forms.addEventListener("submit", function(event) {
    event.preventDefault();

    country = document.getElementById("country").value;
    city = document.getElementById("city").value;
    getweather(country, city);
});

function getweather(country, city){
    fetch(`http://127.0.0.1:8080/weather?cidade=${city}&pais=${country}`)
     .then(response => response.json())
     .then(data => {
        apidata = data;
        console.log(data)
        printdata(apidata);
      })
     .catch(error => {
        console.error('Error:', error);
      });
}

function printdata(apidata) {
    container.classList.toggle('active');
    console.log(apidata.name); //nome da cidade
    console.log(apidata.weather[0].main); //nome do clima
    console.log(apidata.weather[0].description); //desc do clima
    console.log(Number(parseFloat(apidata.main.temp - 273.15).toFixed(2))); // temperatura em Cº arredondado para 2 casas decimais
    console.log(apidata.wind.speed); // velocidade do vento em m/s
    console.log(apidata.sys.country); // país
    console.log(Number(parseFloat(apidata.main.feels_like - 273.15).toFixed(2))); //sensação térmica
    console.log(apidata.main.humidity); // umidade relativa
    console.log(apidata.clouds.all); //porcentagem de nuvens

}