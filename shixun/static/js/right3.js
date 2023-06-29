var ec_right3 = echarts.init(document.getElementById('right3'), "dark");
var ec_right3_Option ={
    title: {
		text: "全国计算机专业累增人数",
		textStyle: {
			// color: 'white',
		},
		left: 'left',
	},
	legend: {
		data: ['累计就业', '年度增加', "幸福度高", "累计失业"],
		left: "right",
		top:25
	},
	grid: {
		left: '4%',
		right: '6%',
		bottom: '4%',
		top: 50,
		containLabel: true
	},
	tooltip: {
		trigger: 'axis',
		//指示器
		axisPointer: {
			type: 'line',
			lineStyle: {
				color: '#7171C6'
			}
		},
	},
  xAxis:[ {
    type: 'category',
    data: []
  }],
  yAxis:[ {
    type: 'value'
  }],
  series: [
    {
      data: [],
      type: 'bar',
      //smooth: true
      showBackground: true,
      backgroundStyle: {
        color: 'rgba(180, 180, 180, 0.2)'
      }
    }
  ]

};
ec_right3.setOption(ec_right3_Option)


