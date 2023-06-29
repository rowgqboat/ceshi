var ec_left3 = echarts.init(document.getElementById('left3'), "dark");
var ec_left3_Option ={
xAxis: [{
    type: 'value'
  }],
  yAxis: [{
    type: 'category',
    data: []

  }],
  series: [
    {
      data: [],
      type: 'bar',
      showBackground: true,
      backgroundStyle: {
        color: 'rgba(180, 180, 180, 0.2)'
      }
    }
  ]
}
ec_left3.setOption(ec_left3_Option)