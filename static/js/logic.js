const bar_url = "/barchart_data"

d3.json(bar_url).then((data) => {
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
    Pie(data.value, data.item)
});

function Pie(values, labels) {
    var data = [{
        values: values,
        labels: labels,
        type: 'pie',
    }];
      
    var layout = {
        title: {
            text:'Distribution of Subjects (Male vs. Female)',
            font: {
                family: 'Courier New, monospace',
                size: 14,
                color: "#325D79"
            },
            xref: 'paper',
        },
    };
      
    Plotly.newPlot('pieChart', data, layout);
};

const line_url = "/line_data"
const traces = []

function deleteTrace(){
    Plotly.deleteTraces('linePlot', [0,1,2,3,4]);
  };
function Line() {
    d3.json(line_url).then((data) => {
        for (let x in data.name) {
          let mouseName = data.name[x];
          let time = data.time[x];
          let tv = data.tv[x];
          traces.push({
            type: 'scatter',
            x: time,
            y: tv,
            name: mouseName,
          });
        };

    var layout = {
        title: 'Tumor Volume over time for 5 random mice treated with Capomulin',
        xaxis: {
            title: 'Time (in days)',
            showgrid: false,
            zeroline: false
        },
        yaxis: {
            title: 'Tumor Volume (mm3)',
            showline: false
        }
    };
    Plotly.newPlot('linePlot', traces, layout)
    });
};
Line();