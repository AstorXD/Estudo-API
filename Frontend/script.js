let country
let city
let apidata

const forms = document.getElementById("forms");

forms.addEventListener("submit", function(event){
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
        console.log(apidata)
        printdata(apidata);
        
      })
     .catch(error => {
        console.error('Error:', error);
      });
}

function printdata(apidata) {
    layoutresultado();
    
    //todo
    
    if (apidata.error != null) {
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
    setTimeout(()=>{
        layoutbusca();
    },1000)

}

function layoutresultado(){
    const container = document.getElementById("maincontainer");
    const botaobusca = document.getElementById("busca");
    const cityplaceholder = document.getElementById("city");
    const countryplaceholder = document.getElementById("country");
    const mainimg = document.getElementById("mainimg");
    const formcontainer = document.getElementById("formcontainer");
    container.classList.add('active');
    botaobusca.classList.remove('active');
    cityplaceholder.classList.remove('active');
    countryplaceholder.classList.remove('active');
    mainimg.classList.remove('active');
    setTimeout(() => {
        botaobusca.style.display = 'none';
        cityplaceholder.style.display = 'none';
        countryplaceholder.style.display = 'none';
        mainimg.style.display = 'none';
        formcontainer.style.display = 'none';
    }, 1000)
}

function layoutbusca() {
    const container = document.getElementById("maincontainer");
    const botaobusca = document.getElementById("busca");
    const cityplaceholder = document.getElementById("city");
    const countryplaceholder = document.getElementById("country");
    const mainimg = document.getElementById("mainimg");
    const formcontainer = document.getElementById("formcontainer");
    
    setTimeout(() => {
        container.classList.remove('active');
        botaobusca.classList.add('active');
        cityplaceholder.classList.add('active');
        countryplaceholder.classList.add('active');
        mainimg.classList.add('active');
    })
    botaobusca.style.display = 'block';
    cityplaceholder.style.display = 'block';
    countryplaceholder.style.display = 'block';
    mainimg.style.display = 'block';
    formcontainer.style.display = 'flex';  
  
}