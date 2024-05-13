
const slides = document.querySelectorAll(".slide")
var counter = 0 ; 

const leftButton = document.querySelector(".left-arrow");
const rightButton = document.querySelector(".right-arrow");


slides.forEach( 
    (slide,index) => {
        slide.style.left = `${index * 100}%`
    }
) 

const moveRight = () => {
    if(counter<slides.length -1){
    counter++
    slideImage();
    }
}

const moveLeft = () => {
    if(counter>0){
    counter--
    slideImage()
    }
}


const slideImage = () => {
    slides.forEach(
        (slide) => {
            slide.style.transform = `translateX(-${counter*100}%)`;
        }
    )
}


 /*   selectElement = document.getElementById('uibedroom');
    output = selectElement.value;
    console.log(output);
*/

const dropdowns = [
    document.getElementById("uibedroom"),
    document.getElementById("uibathroom"),
    document.getElementById("uibalcony"),
    document.getElementById("uilift"),
    document.getElementById("uikitchen"),
    document.getElementById("uiparking")
  ];
  
  for (let i = 0; i < dropdowns.length; i++) {
    for (let j = 1; j <= 10; j++) {
      const option = document.createElement("option");
      option.value = j;
      option.text = j;
      dropdowns[i].appendChild(option);
    }
  }

function PredictPrice() {
    var data = {
        area: parseFloat(document.getElementById("uiArea").value),
        bed: parseFloat(document.getElementById("uibedroom").value),
        bath: parseFloat(document.getElementById("uibathroom").value),
        balc: parseFloat(document.getElementById("uibalcony").value),
        status: parseInt(document.getElementById("uistatus").value),
        parking: parseFloat(document.getElementById("uiparking").value),
        furn: parseInt(document.getElementById("uifurnished").value),
        lift: parseFloat(document.getElementById("uilift").value),
        price_sqft: parseFloat(document.getElementById("uiprice_sq_ft").value),
        kitc: parseInt(document.getElementById("uikitchen").value),
        neworold: document.getElementById("uicondition").value,
        building_type: document.getElementById("uitype").value,
        pincode: parseInt(document.getElementById("uipincode").value)
    };

    var url = "http://127.0.0.1:5000/predict_home_price";

    $.ajax({
        type: "POST",
        url: url,
        data: JSON.stringify(data),
        contentType: "application/json",
        success: function(data, status) {
            var estPrice = document.getElementById('uiEstimatedPrice');
            estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " ₹</h2>";
        },
        error: function(xhr, textStatus, errorThrown) {
            console.log(xhr.responseText);
        }
    });
}

// Function to fetch and populate average price per square feet for the selected pincode
function populatePricePerSqFt() {
    var selectedPincode = document.getElementById("uipincode").value;
    var url = "http://127.0.0.1:5000/get_avg_price?pincode=" + selectedPincode;

    $.get(url,function(data,status){
        console.log("got response for avg price request");
        if(data && data.avg_price){
            document.getElementById("uiprice_sq_ft").value = data.avg_price;
        }
    });
}

function onPageLoad(){
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_pincodes";
    console.log("Request URL: ", url)
    $.get(url,function(data,status){
        console.log("got response for pincode request");
        if(data && data.pincodes){
            var pincodes = data.pincodes;
            var datalist = document.getElementById("browsers");
            datalist.innerHTML = ""; // Clear existing options
            pincodes.forEach(function(pincode) {
                var option = document.createElement("option");
                option.value = pincode;
                datalist.appendChild(option);
            });
        }
    });
}




window.onload = onPageLoad;
