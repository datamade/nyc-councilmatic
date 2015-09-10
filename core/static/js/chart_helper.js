var ChartHelper = {};
ChartHelper.donations = function(el, title, sourceTxt, yaxisLabel, data, pointInterval) {
  // console.log("rendering to: #chart_" + iteration);
  // console.log("title: " + title);
  // console.log("sourceTxt: " + sourceTxt);
  // console.log("yaxisLabel: " + yaxisLabel);
  // console.log(dataArray);
  // console.log("startDate: " + startDate);
  // console.log("pointInterval: " + pointInterval);
  // console.log(start_date);
  // console.log(Date.parse(start_date))
  // console.log(data)

  // var selected = data.indexOf(Date.parse(start_date));
  // console.log(selected);

  var color = '#007F00';
  
  var seriesData = [{
      color: color,
      data: data,
      name: title,
      showInLegend: false,
      lineWidth: 2
  }];

  //$("#charts").append("<div class='chart' id='chart_grouping_" + iteration + "'></div>")
  return new Highcharts.Chart({
      chart: {
          renderTo: el,
          type: "column",
          marginRight: 10,
          marginBottom: 25
      },
      legend: {
        backgroundColor: "#ffffff",
        borderColor: "#cccccc",
        floating: true,
        verticalAlign: "top"
      },
      credits: { 
        enabled: false 
      },
      title: null,
      xAxis: {
          dateTimeLabelFormats: { year: "%Y" },
          type: "datetime"
      },
      yAxis: {
          title: yaxisLabel,
          min: 0
      },
      plotOptions: {
        line: {
          animation: false
        },
        series: {
          point: {
            events: {
              click: function() {
                var date = moment.utc(new Date(this.x)).format('YYYY-MM-DD');
                window.location.href = '/donations?date=' + date;
              }
            }
          },
          marker: {
            fillColor: color,
            radius: 0,
            states: {
              hover: {
                enabled: true,
                radius: 5
              }
            }
          },
          shadow: false,
          states: {
             hover: {
                lineWidth: 2
             }
          }
        }
      },
      tooltip: {
          crosshairs: true,
          formatter: function() {
            var s = "<strong>" + ChartHelper.toolTipDateFormat(pointInterval, this.x) + "</strong>";
            $.each(this.points, function(i, point) {
              s += "<br /><span style='color: " + point.series.color + "'>" + point.series.name + ":</span> $" + Highcharts.numberFormat(point.y, 0, '.', ',');
            });
            return s;
          },
          shared: true
      },
      series: seriesData
    });
  }

ChartHelper.netfunds = function(el, title, sourceTxt, yaxisLabel, data) {
  var color = '#007F00';
  
  var seriesData = [{
          color: color,
          data: data[0],
          name: "Funds available"
        }, {
          color: "#b28d00",
          data: data[1],
          name: "Investments"
        }, {
          color: "#cc0000",
          data: data[2],
          name: "Debts"
        }
      ]

  //$("#charts").append("<div class='chart' id='chart_grouping_" + iteration + "'></div>")
  return new Highcharts.Chart({
      chart: {
          renderTo: el,
          type: "column",
          marginRight: 10,
          marginBottom: 25
      },
      legend: {
        backgroundColor: "#ffffff",
        borderColor: "#cccccc",
        floating: true,
        verticalAlign: "top"
      },
      credits: { 
        enabled: false 
      },
      title: null,
      xAxis: {
          dateTimeLabelFormats: { year: "%Y" },
          type: "datetime"
      },
      yAxis: {
          title: null
      },
      plotOptions: {
        line: {
          animation: false
        },
        series: {
          stacking: 'normal',
          marker: {
            fillColor: color,
            radius: 0,
            states: {
              hover: {
                enabled: true,
                radius: 5
              }
            }
          },
          shadow: false
        }
      },
      tooltip: {
          crosshairs: true,
          formatter: function() {
            var s = "<strong>" + ChartHelper.toolTipDateFormat("quarter", this.x) + "</strong>";
            $.each(this.points, function(i, point) {
              s += "<br /><span style='color: " + point.series.color + "'>" + point.series.name + ":</span> $" + Highcharts.numberFormat(point.y, 0, '.', ',');
            });
            return s;
          },
          shared: true
      },
      series: seriesData
    });
  }

ChartHelper.donation_expenditure = function(el, title, sourceTxt, yaxisLabel, data) {
  var color = '#007F00';
  
  var seriesData = [{
          color: color,
          data: data[0],
          name: "Donations"
        },{
          color: "#cc0000",
          data: data[1],
          name: "Expenditures"
        }
      ]

  //$("#charts").append("<div class='chart' id='chart_grouping_" + iteration + "'></div>")
  return new Highcharts.Chart({
      chart: {
          renderTo: el,
          type: "column",
          marginRight: 10,
          marginBottom: 25
      },
      legend: {
        backgroundColor: "#ffffff",
        borderColor: "#cccccc",
        floating: true,
        verticalAlign: "top"
      },
      credits: { 
        enabled: false 
      },
      title: null,
      xAxis: {
          dateTimeLabelFormats: { year: "%Y" },
          type: "datetime"
      },
      yAxis: {
          title: null
      },
      plotOptions: {
        line: {
          animation: false
        },
        series: {
          stacking: 'normal',
          marker: {
            fillColor: color,
            radius: 0,
            states: {
              hover: {
                enabled: true,
                radius: 5
              }
            }
          },
          shadow: false
        }
      },
      tooltip: {
          crosshairs: true,
          formatter: function() {
            var s = "<strong>" + ChartHelper.toolTipDateFormat("quarter", this.x) + "</strong>";
            $.each(this.points, function(i, point) {
              s += "<br /><span style='color: " + point.series.color + "'>" + point.series.name + ":</span> $" + Highcharts.numberFormat(point.y, 0, '.', ',');
            });
            return s;
          },
          shared: true
      },
      series: seriesData
    });
  }

ChartHelper.initQualityChart = function(el) {
  $('#' + el).highcharts({
      chart: {
          type: 'bar'
      },
      credits: {
        enabled: false
      },
      title: {
          text: null
      },
      xAxis: {
        title: null,
          labels: {
            enabled: false
          }
      },
      yAxis:{
          title: null,
          min: 1989,
          max: 2015,
          labels: {
            formatter: function() { return parseInt(this.value); }
          }
      },
      plotOptions: {
          series: {
              stacking: 'true',
              events: {
                legendItemClick: function () {
                  return false; 
              }
            }
          }
      },
      tooltip: {
        borderColor: "#ccc",
        formatter: function() {
          return this.series.name;
        }
      },
      legend: { reversed: true },
      series: [
        {
          name: '2000 on: Electronic filings',
          data: [ 15 ],
          color: "#43ac6a",
        },
        {
          name: '1999: Incomplete',
          data: [ 1 ],
          color: "#d9edf7"
        },
        {
          name: '1994 - 1999: Manually entered',
          data: [ 5 ],
          color: "#43ac6a"
        }, 
        {
          name: '1989 - 1994: Bad entries',
          data: [ 1994 ],
          color: "#d9edf7"
        }
      ]
  });
}

ChartHelper.pointInterval = function(interval) {
  if (interval == "year")
    return 365 * 24 * 3600 * 1000;
  if (interval == "quarter")
    return 3 * 30.4 * 24 * 3600 * 1000;
  if (interval == "month") //this is very hacky. months have different day counts, so our point interval is the average - 30.4
    return 30.4 * 24 * 3600 * 1000;
  if (interval == "week")
    return 7 * 24 * 3600 * 1000;
  if (interval == "day")
    return 24 * 3600 * 1000;
  if (interval == "hour")
    return 3600 * 1000;
  else
    return 1;
}

ChartHelper.toolTipDateFormat = function(interval, x) {
  if (interval == "year")
    return Highcharts.dateFormat("%Y", x);
  if (interval == "quarter")
    return Highcharts.dateFormat("%B %Y", x);
  if (interval == "month")
    return Highcharts.dateFormat("%B %Y", x);
  if (interval == "week")
    return Highcharts.dateFormat("%e %b %Y", x);
  if (interval == "day")
    return Highcharts.dateFormat("%e %b %Y", x);
  if (interval == "hour")
    return Highcharts.dateFormat("%H:00", x);
  else
    return 1;
}

