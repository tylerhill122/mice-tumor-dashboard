const url = "/barchart_data"

d3.json(url).then((data) => {
    console.log(data);
    Bar(data.drug, data.value)
})

function Bar(x, y) {
    var data = [{
        type: 'bar',
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
                size: 24,
                color: "#325D79"
            },
            xref: 'paper',
        },
        yaxis: {
            title: {
                text: 'Number of Data Readings',
                font: {
                    family: 'Courier New, monospace',
                    size: 20,
                    color: "#325D79"
                }
            },
            range: [120, 210],
        },
        xaxis: {
            title: {
                text: 'Drug Regimen',
                font: {
                    family: 'Courier New, monospace',
                    size: 20,
                    color: "#325D79"
                }
            },
        },
        font: {
            size: 14,
            color: "#325D79"
        }
      };

    Plotly.newPlot('barChart', data, layout);
}