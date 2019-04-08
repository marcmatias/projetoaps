/**
* Script com charts e chamadas do banco Firebase
*/
const monthNames = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
  "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
];

// Captura sala preenchida no select da pagina chart  
function functionSelect() {
    accessDatabase(document.getElementById("select_sala").value);
    for (let el of document.querySelectorAll('.hiddenJS')) el.style.visibility = 'visible';
}

// Initialize Firebase
const config = {
    apiKey: "AIzaSyB1ZE5-ppifq6BFPBsTsFaWeiw2FOLniHY",
    authDomain: "consumo-51508.firebaseapp.com",
    databaseURL: "https://consumo-51508.firebaseio.com",
    stordataBucket: "consumo-51508.appspot.com",
}

firebase.initializeApp(config);

function accessDatabase(estPreSal){
    firebase.database().ref('consumo').orderByChild("estpresal").equalTo(estPreSal).on('value', function(snapshot) {
        dataConsumoEConsumoTotal = snapshotToArrayDataConsumo(snapshot, daysBefore()[0], daysBefore()[1]);
        dateConsumptionMonthNow = snapshotToArrayDataConsumo(snapshot, daysBefore()[2], daysBefore()[3]);
        dateConsumptionMonthBefore = snapshotToArrayDataConsumo(snapshot, daysBefore()[4], daysBefore()[5]);
        dateConsumption2MonthBefore = snapshotToArrayDataConsumo(snapshot, daysBefore()[6], daysBefore()[7]);
        dateConsumption3MonthBefore = snapshotToArrayDataConsumo(snapshot, daysBefore()[8], daysBefore()[9]);
        dateConsumption4MonthBefore = snapshotToArrayDataConsumo(snapshot, daysBefore()[10], daysBefore()[11]);
        dateConsumption5MonthBefore = snapshotToArrayDataConsumo(snapshot, daysBefore()[12], daysBefore()[13]);
        dateConsumption6MonthBefore = snapshotToArrayDataConsumo(snapshot, daysBefore()[14], daysBefore()[15]);

        month = [monthNames[daysBefore()[14].getMonth()], monthNames[daysBefore()[12].getMonth()], monthNames[daysBefore()[10].getMonth()],
         monthNames[daysBefore()[8].getMonth()], monthNames[daysBefore()[6].getMonth()],
         monthNames[daysBefore()[4].getMonth()],  monthNames[daysBefore()[2].getMonth()]];
        consumptions = [dateConsumption6MonthBefore.itemConsumototal,
             dateConsumption5MonthBefore.itemConsumototal, dateConsumption4MonthBefore.itemConsumototal,
             dateConsumption3MonthBefore.itemConsumototal, dateConsumption2MonthBefore.itemConsumototal,
             dateConsumptionMonthBefore.itemConsumototal, dateConsumptionMonthNow.itemConsumototal];

        chartinfo = daysConsumption(dataConsumoEConsumoTotal.data, dataConsumoEConsumoTotal.consumo);
        chartJS(chartinfo.data, chartinfo.consumo, month, consumptions);
    });
}

function snapshotToArrayDataConsumo(snapshot, dateStart, dateEnd) {
    var data_Consumo_Snapshot = [];
    var itemConsumototal = 0;
    
    snapshot.forEach(function(childSnapshot) {
        var item = childSnapshot.val();

        if (item.data_hora >= dateStart.yyyymmdd() && item.data_hora <= dateEnd.yyyymmdd()) {
            itemConsumototal += item.kwh;
            data_Consumo_Snapshot.push({data : item.data_hora, consumo : item.kwh});
        }
    });

    result = dateConsuptionToArray(data_Consumo_Snapshot);
    return {data : result.data, consumo : result.consumo, itemConsumototal : itemConsumototal};
}

function dateConsuptionToArray(arrayDateConsumption){
    var data = [];
    var consumo = [];
    for (const [key, value] of Object.entries(arrayDateConsumption)){
        var dataFind = data.find(function(e){return e == value.data ? true : false});
        if (dataFind){
            consumo[data.indexOf(value.data)] = consumo[data.indexOf(value.data)] + value.consumo;
        }else {
            data.push(value.data);
            consumo.push(value.consumo);
        }
    }
    return {data : data, consumo : consumo}
}

function daysBefore(){
    var now = new Date();
    var date = (now.getFullYear() + "-" + (now.getMonth() + 1) + "-" + now.getDate());
    var dateMonthBeforeVar = (now.getFullYear() + "-" + (now.getMonth()) + "-" + 1);
    var dateNow = new Date(date);
    
    // 60 dias atras
    var dateSixtyDaysBefore = new Date(date);
    dateSixtyDaysBefore.setDate(dateSixtyDaysBefore.getDate()-59);
    var dateMonthNow = new Date(date);
    dateMonthNow.setDate(1);
    var dateMonthNowLastDay = new Date(dateMonthNow);
    dateMonthNowLastDay.setMonth(dateMonthNowLastDay.getMonth()+1);
    dateMonthNowLastDay.setDate(0);
    // Dia primeiro do mes passado
    var dateMonthBefore = new Date(dateMonthBeforeVar);
    var dateMonthBeforeLastDay = new Date(dateMonthBefore);
    dateMonthBeforeLastDay.setMonth(dateMonthBeforeLastDay.getMonth()+1);
    dateMonthBeforeLastDay.setDate(0);
    // Dia primeiro do mes antepeasado
    var date2MonthBefore = new Date(dateMonthBefore);
    date2MonthBefore.setMonth(date2MonthBefore.getMonth()-1);
    var date2MonthBeforeLastDay = new Date(date2MonthBefore);
    date2MonthBeforeLastDay.setMonth(date2MonthBeforeLastDay.getMonth()+1);
    date2MonthBeforeLastDay.setDate(0);
    // Dia primeiro do mes 3 meses atras
    var date3MonthBefore = new Date(date2MonthBefore);
    date3MonthBefore.setMonth(date3MonthBefore.getMonth()-1);
    var date3MonthBeforeLastDay = new Date(date3MonthBefore);
    date3MonthBeforeLastDay.setMonth(date3MonthBeforeLastDay.getMonth()+1);
    date3MonthBeforeLastDay.setDate(0); 
    // Dia primeiro do mes 4 meses atras
    var date4MonthBefore = new Date(date3MonthBefore);
    date4MonthBefore.setMonth(date4MonthBefore.getMonth()-1);
    var date4MonthBeforeLastDay = new Date(date4MonthBefore);
    date4MonthBeforeLastDay.setMonth(date4MonthBeforeLastDay.getMonth()+1);
    date4MonthBeforeLastDay.setDate(0);
    // Dia primeiro do mes 5 meses atras
    var date5MonthBefore = new Date(date4MonthBefore);
    date5MonthBefore.setMonth(date5MonthBefore.getMonth()-1);
    var date5MonthBeforeLastDay = new Date(date5MonthBefore);
    date5MonthBeforeLastDay.setMonth(date5MonthBeforeLastDay.getMonth()+1);
    date5MonthBeforeLastDay.setDate(0);
    // Dia primeiro do mes 6 meses atras
    var date6MonthBefore = new Date(date5MonthBefore);
    date5MonthBefore.setMonth(date5MonthBefore.getMonth()-1);
    var date6MonthBeforeLastDay = new Date(date6MonthBefore);
    date6MonthBeforeLastDay.setMonth(date6MonthBeforeLastDay.getMonth()+1);
    date6MonthBeforeLastDay.setDate(0);

    return [dateSixtyDaysBefore, dateNow, dateMonthNow, dateMonthNowLastDay, dateMonthBefore,
        dateMonthBeforeLastDay, date2MonthBefore, date2MonthBeforeLastDay, date3MonthBefore, date3MonthBeforeLastDay,
        date4MonthBefore, date4MonthBeforeLastDay, date5MonthBefore, date5MonthBeforeLastDay, date6MonthBefore, date6MonthBeforeLastDay];
}

function daysConsumption(data, consumo){

    var datas = [];
    var consumos = [];

    for (let index = daysBefore()[0]; index <= daysBefore()[1]; index.setDate(index.getDate()+1)) {
        var dataExist = data.find(function(e){return e == index.yyyymmdd() ? true : false});
        if (dataExist){
            datas.push(index.yyyymmdd());
            consumos.push(consumo[data.indexOf(index.yyyymmdd())]);
        } else {
            datas.push(index.yyyymmdd());
            consumos.push(0);
        }
    }
    return {data : datas, consumo: consumos};
}

// Formatação de data em Ano-Mes-Dia
Date.prototype.yyyymmdd = function() {
    var mm = this.getMonth() + 1; // getMonth() is zero-based
    var dd = this.getDate();
  
    return [this.getFullYear()+ "-",
            (mm>9 ? '' : '0') + mm + "-",
            (dd>9 ? '' : '0') + dd
           ].join('');
}

/*Function to update the bar chart*/
function updateAreaGraph(chart, listaConsumo) {
    chart.data.datasets.pop();
    chart.data.datasets.push({
        label: "kwh",
        lineTension: 0.3,
        backgroundColor: "rgba(2,117,216,0.2)",
        borderColor: "rgba(2,117,216,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(2,117,216,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(2,117,216,1)",
        pointHitRadius: 20,
        pointBorderWidth: 2,
        data: listaConsumo,
    });
    chart.update();
}

function updateBarGraph(chart, ConsumptionTotal) {
    chart.data.datasets.pop();
    chart.data.datasets.push({
        label: "Consumo",
        backgroundColor: "rgba(2,117,216,1)",
        borderColor: "rgba(2,117,216,1)",
        data: ConsumptionTotal
    });
    chart.update();
}

var myLineChart;
var myLineChartBar;
function chartJS(listDataConsumo, listaConsumo, Month, ConsumptionTotal) {

    // -- Area Chart Example
    if(myLineChart){
        updateAreaGraph(myLineChart, listaConsumo);
    } else{
        var ctx = document.getElementById("myAreaChart");
        myLineChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: listDataConsumo,
                datasets: [{
                    label: "kwh",
                    lineTension: 0.3,
                    backgroundColor: "rgba(2,117,216,0.2)",
                    borderColor: "rgba(2,117,216,1)",
                    pointRadius: 5,
                    pointBackgroundColor: "rgba(2,117,216,1)",
                    pointBorderColor: "rgba(255,255,255,0.8)",
                    pointHoverRadius: 5,
                    pointHoverBackgroundColor: "rgba(2,117,216,1)",
                    pointHitRadius: 20,
                    pointBorderWidth: 2,
                    data: listaConsumo
                }],
            },
            options: {
                scales: {
                    xAxes: [{
                        time: {
                            unit: 'date'
                        },
                        gridLines: {
                            display: false
                        },
                        ticks: {
                            maxTicksLimit: 7
                        }
                    }],
                    yAxes: [{
                        ticks: {
                            min: 0,
                            max: 40000,
                            maxTicksLimit: 5
                        },
                        gridLines: {
                            color: "rgba(0, 0, 0, .125)",
                        }
                    }],
                },
                legend: {
                    display: false
                },
                animation: {
                    duration: 0
                }
            }
        });
    }
    if(myLineChartBar){
        updateBarGraph(myLineChartBar, ConsumptionTotal);
    } else {
        // -- Bar Chart Example
        var ctx = document.getElementById("myBarChart");
        myLineChartBar = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: Month,
                datasets: [{
                    label: "Consumo",
                    backgroundColor: "rgba(2,117,216,1)",
                    borderColor: "rgba(2,117,216,1)",
                    data: ConsumptionTotal
                }],
            },
            options: {
                scales: {
                    xAxes: [{
                    time: {
                        unit: 'month'
                    },
                    gridLines: {
                        display: false
                    },
                    ticks: {
                        maxTicksLimit: 6
                    }
                    }],
                    yAxes: [{
                    ticks: {
                        min: 0,
                        max: 140000,
                        maxTicksLimit: 7
                    },
                    gridLines: {
                        display: true
                    }
                    }],
                },
                legend: {
                    display: false
                },
                animation: {
                    duration: 0
                }
            }
        });
    }


    // Criar função
    var node = document.getElementById('ConsumptionMonthNow');
    var node1 = document.getElementById('ConsumptionMonthBefore');
    var node2 = document.getElementById('Consumption2MonthBefore');
    node.innerHTML = "";
    node1.innerHTML = "";
    node2.innerHTML = "";
    var newNode = document.createElement('p');
    var newNode1 = document.createElement('p');
    var newNode2 = document.createElement('p');
    newNode.appendChild(document.createTextNode('KWH ' + ConsumptionTotal[ConsumptionTotal.length - 1]));
    newNode1.appendChild(document.createTextNode('KWH ' + ConsumptionTotal[ConsumptionTotal.length - 2]));
    newNode2.appendChild(document.createTextNode('KWH ' + ConsumptionTotal[ConsumptionTotal.length - 3]));
    node.appendChild(newNode);
    node1.appendChild(newNode1);
    node2.appendChild(newNode2);
}

