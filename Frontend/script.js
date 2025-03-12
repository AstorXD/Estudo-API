let country;
let city;
let apidata;

const forms = document.getElementById("forms");
const refresh = document.getElementById("refresh");

refresh.addEventListener("click", function (event) {
    event.preventDefault();
    layoutbusca();
});

forms.addEventListener("submit", function (event) {
  event.preventDefault();
  country = document.getElementById("country").value;
  city = document.getElementById("city").value;
  getweather(country, city);
});

function getweather(country, city) {
  fetch(`http://127.0.0.1:8080/weather?cidade=${city}&pais=${country}`)
    .then(async (response) => {
        if (!response.ok) {
            const errordata = await response.json();
            throw new Error(errordata.error || "Erro desconhecido")
    }
    return response.json();
    })
    .then((data) => {
      apidata = data;
      console.log(apidata);
      printdata(apidata);
    })
    .catch((error) => {
        console.error(error);
    });
}

function printdata(apidata) {
  layoutresultado();
  
  document.getElementById("cityname").textContent = apidata.name; //nome da cidade
  document.getElementById("countrycode").textContent = apidata.sys.country; //código do país
  document.getElementById("weathername").textContent = apidata.weather[0].main; //nome do clima
  document.getElementById("description").textContent = apidata.weather[0].description; //desc do clima
  document.getElementById("temp").textContent = Number(parseFloat(apidata.main.temp - 273.15).toFixed(1))+"°C"; // temperatura em Cº arredondado para 1 casa decimal
  document.getElementById("feelslike").textContent = Number(parseFloat(apidata.main.feels_like - 273.15).toFixed(1))+"°C"; //sensação térmica em Cº arredondado para 1 casa decimal
  document.getElementById("humidity").textContent = apidata.main.humidity+"%";  // umidade relativa 
  document.getElementById("windspeed").textContent = apidata.wind.speed+"m/s"; // velocidade do vento em m/s
  document.getElementById("cloudpercent").textContent = apidata.clouds.all+"%"; //porcentagem de nuvens
}

function layoutresultado() {
  const { 
    maincontainer: container,
    busca: botaobusca,
    city: cityplaceholder,
    country: countryplaceholder,
    mainimg: mainimg,
    formcontainer: formcontainer,
    weathercontainer: weathercontainer
  } = Object.fromEntries(
    ['maincontainer', 'busca', 'city', 'country', 'mainimg', 'formcontainer', 'weathercontainer']
      .map(id => [id, document.getElementById(id)])
  );

  [container, refresh, weathercontainer].forEach(id => (id).classList.add("active"));
  [botaobusca, cityplaceholder, countryplaceholder, mainimg].forEach(id => (id).classList.remove("active"));
  setTimeout(() => {
    formcontainer.style.display = "none";
    weathercontainer.style.display = "flex";
  }, 1000);
}

function layoutbusca() {

  const { 
    maincontainer: container,
    busca: botaobusca,
    city: cityplaceholder,
    country: countryplaceholder,
    mainimg: mainimg,
    formcontainer: formcontainer,
    weathercontainer: weathercontainer
  } = Object.fromEntries(
    ['maincontainer', 'busca', 'city', 'country', 'mainimg', 'formcontainer', 'weathercontainer']
      .map(id => [id, document.getElementById(id)])
  );

  setTimeout(() => {
    [container, refresh, weathercontainer].forEach(id => (id).classList.remove("active"));
    [botaobusca, cityplaceholder, countryplaceholder, mainimg].forEach(id => (id).classList.add("active"));
  });
  setTimeout(() => {
    weathercontainer.style.display = "none";
    formcontainer.style.display = "flex";
  });
}

