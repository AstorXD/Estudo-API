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

  //todo

  
  console.log(apidata.name); //nome da cidade
  console.log(apidata.weather[0].main); //nome do clima
  console.log(apidata.weather[0].description); //desc do clima
  console.log(Number(parseFloat(apidata.main.temp - 273.15).toFixed(2))); // temperatura em Cº arredondado para 2 casas decimais
  console.log(apidata.wind.speed); // velocidade do vento em m/s
  console.log(apidata.sys.country); // país
  console.log(
    Number(parseFloat(apidata.main.feels_like - 273.15).toFixed(2))
  ); //sensação térmica
  console.log(apidata.main.humidity); // umidade relativa
  console.log(apidata.clouds.all); //porcentagem de nuvens
  
}

function layoutresultado() {
  const { 
    maincontainer: container,
    busca: botaobusca,
    city: cityplaceholder,
    country: countryplaceholder,
    mainimg: mainimg,
    formcontainer: formcontainer
  } = Object.fromEntries(
    ['maincontainer', 'busca', 'city', 'country', 'mainimg', 'formcontainer']
      .map(id => [id, document.getElementById(id)])
  );

  [container, refresh].forEach(id => (id).classList.add("active"));
  [botaobusca, cityplaceholder, countryplaceholder, mainimg].forEach(id => (id).classList.remove("active"));
  setTimeout(() => {
    formcontainer.style.display = "none";
  }, 1000);
}

function layoutbusca() {

  const { 
    maincontainer: container,
    busca: botaobusca,
    city: cityplaceholder,
    country: countryplaceholder,
    mainimg: mainimg,
    formcontainer: formcontainer
  } = Object.fromEntries(
    ['maincontainer', 'busca', 'city', 'country', 'mainimg', 'formcontainer']
      .map(id => [id, document.getElementById(id)])
  );
  setTimeout(() => {
    [container, refresh].forEach(id => (id).classList.remove("active"));
    [botaobusca, cityplaceholder, countryplaceholder, mainimg].forEach(id => (id).classList.add("active"));
  });
  formcontainer.style.display = "flex";
}
