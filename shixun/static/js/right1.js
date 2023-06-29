
var ec_right1 = echarts.init(document.getElementById('right1'), "dark");

var ec_right1_Option = {
	//标题样式
	title: {
    text: '每天专业就业人数'
  },
  tooltip: {
    trigger: 'axis'
  },
  legend: {
    data: ['HTML', 'JAVA', 'Python', 'C#', 'Go']
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  toolbox: {
    feature: {
      saveAsImage: {}
    }
  },
  xAxis:[ {
    type: 'category',
    boundaryGap: false,
    data: []
  }],
  yAxis:[ {
    type: 'value'
  }],
  series: [
    {
      name: 'HTML',
      type: 'line',
      stack: 'Total',
      data: []
    },
    {
      name: 'JAVA',
      type: 'line',
      stack: 'Total',
      data: []
    },
    {
      name: 'Python',
      type: 'line',
      stack: 'Total',
      data: []
    },
    {
      name: 'C#',
      type: 'line',
      stack: 'Total',
      data: []
    },
    {
      name: 'Go',
      type: 'line',
      stack: 'Total',
      data: []
    }
  ]
};
ec_right1.setOption(ec_right1_Option)
