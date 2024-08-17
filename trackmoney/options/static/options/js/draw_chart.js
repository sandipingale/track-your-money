var options = {
  series: [{
    name: "Profit",
    //data: [2500,2500,2500,2500,2500,2500,2500,2500,2500,1250,0,-1250,-2500,-3750,-5000]
    data: [-2500,-2500,-2500,-2500,-2500,-2500,-2500,-1250,0,1250,2500,3750,5000,6250,7500]
}],
  chart: {
  height: 350,
  type: 'line',
  zoom: {
    enabled: false
  }
},
dataLabels: {
  enabled: false
},
stroke: {
  curve: 'straight'
},
title: {
  text: 'Product Trends by Month',
  align: 'left'
},
grid: {
  row: {
    colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
    opacity: 0.5
  },
},
xaxis: {
  categories: [24300,24350,24400,24450,24500,24550,24600,24650,24700,24750,24800,24850,24900,24950,25000],
},
yaxis:{
  min: -5000,
  stepSize: 1000
},
annotations: {
  xaxis: [{
    x: 24750,
    x2: 25000,
    fillColor: '#B3F7CA',
    opacity: 0.4,
    label: {
      borderColor: '#B3F7CA',
      style: {
        fontSize: '10px',
        color: '#fff',
        background: '#00E396',
      },
      offsetY: -10,
      text: 'Profit',
    }
}]
}
};

var chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();