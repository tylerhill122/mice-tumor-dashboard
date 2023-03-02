const bar_url = "/barchart_data"

d3.json(bar_url).then((data) => {
    console.log(data);
    Bar(data.item, data.value)
});

function Bar(x, y) {
    var data = [{
        type: 'bar',
        text: y.map(String),
        textposition: 'auto',
        hoverinfo: 'none',
        orientation: 'v',
        x: x,
        y: y,
        marker: {
            color: 'rgb(50,93,121)',
            width: 1
          }
    }];

    var layout = {
        plot_bgcolor: "rgba(0,0,0,0)",
        paper_bgcolor: "rgba(0,0,0,0)",
        title: {
            text:'Number of Data Points For Each Drug Regimen',
            font: {
                family: 'Courier New, monospace',
                size: 20,
                color: "#325D79"
            },
            xref: 'paper',
        },
        yaxis: {
            title: {
                text: 'Number of Data Readings',
                font: {
                    family: 'Courier New, monospace',
                    size: 16,
                    color: "#325D79"
                }
            },
            range: [120, 220],
            autorange: true,
        },
        xaxis: {
            title: {
                text: 'Drug Regimen',
                font: {
                    family: 'Courier New, monospace',
                    size: 16,
                    color: "#325D79"
                }
            },
        },
        font: {
            size: 12,
            color: "#325D79"
        }
      };

    Plotly.newPlot('barChart', data, layout);
};

const pie_url = "/piechart_data"

d3.json(pie_url).then((data) => {
    console.log(data);
    Pie(data.value, data.item)
});

function Pie(values, labels) {
    var data = [{
        values: values,
        labels: labels,
        type: 'pie',
    }];
      
    var layout = {
        height: 400,
        width: 500
    };
      
    Plotly.newPlot('pieChart', data, layout);
};