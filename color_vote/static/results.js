$(document).ready(function(){
	let canvases = $('canvas');
	for(let c of canvases){
		let _color = $(c),
			_red = _color.attr('data-red'),
			_green = _color.attr('data-green'),
			_blue = _color.attr('data-blue'), 
			ctx = c.getContext('2d');
		let myChart = new Chart(ctx, {
			type: 'horizontalBar',
			data: {
				labels: ['red', 'green', 'blue'],
				datasets: [{
					backgroundColor: ['rgba(220, 35, 55, 0.5)', 'rgba(20, 125, 20, 0.5)', 'rgba(0, 20, 255, 0.5)'],
					data: [_red, _green, _blue]
				}]
			},
			options: {
				scales: {
					xAxes: [{
						ticks: {
							beginAtZero:true,
							max: 300
						},
						maxBarThickness: 1
					}]
				},
				legend: {
					display: false
				},
				elements: {
					rectangle: {
						borderWidth: 2
					}
				},
			}
		});
	}
});